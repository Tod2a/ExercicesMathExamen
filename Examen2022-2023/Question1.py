graph = {
    'A': ['B', 'C'],
    'B': ['F', 'H'],
    'C': ['F'],
    'D': ['E', 'F'],
    'E': ['H'],
    'F': ['A', 'C', 'D', 'G'],
    'G': ['A', 'D', 'F'],
    'H': ['B', 'E']
}


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    vertices = list(graph.keys())
    
    while vertices:
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])
        vertices.remove(current_vertex)
        
        if distances[current_vertex] == float('infinity'):
            break
        
        for neighbor in graph[current_vertex]:
            alternative_route = distances[current_vertex] + 1
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_vertices[neighbor] = current_vertex
    
    return previous_vertices

def construct_path(previous_vertices, target):
    path = []
    current_vertex = target
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path.reverse()
    return path


# Fonction pour vérifier si la matrice est symétrique
def is_symmetric(graph):
    for node in graph:
        for neighbor in graph[node]:
            if node not in graph[neighbor]:
                return False
    return True

# Vérification du type de graphe
def graph_type(graph):
    directed = not is_symmetric(graph)
    return "graphe orienté" if directed else "graphe non orienté"

# Vérification de la symétrie de la matrice
def print_symmetry_info(graph):
    if is_symmetric(graph):
        print("La matrice est symétrique.")
        print("Une matrice symétrique signifie que si il y a un chemin de A vers B, il y a aussi un chemin de B vers A.")
    else:
        print("La matrice n'est pas symétrique.")
        print("Une matrice non symétrique signifie que les chemins ne sont pas nécessairement bidirectionnels.")
        
# Modification de la poignée de porte
def modify_graph_for_door(graph):
    if 'H' in graph['B']:
        graph['B'].remove('H')
    return graph



start = 'E'
end = 'C'

previous_vertices = dijkstra(graph, start)
path = construct_path(previous_vertices, end)

print("Chemin le plus court de E à C : ", path)
print("Nombre de pièces intermédiaires : ", len(path) - 2)  # Excluant le point de départ et d'arrivée

# Affichage des informations sur le graphe
print(f"Type de graphe: {graph_type(graph)}")
print_symmetry_info(graph)

# Modification du graphe pour la poignée de porte démontée
modified_graph = modify_graph_for_door(graph.copy())
print("\nAprès avoir démonté la poignée de porte de la Salle informatique vers l'armurerie:")

# Vérification du type de graphe après modification
print(f"Type de graphe modifié: {graph_type(modified_graph)}")
print_symmetry_info(modified_graph)

# Exécution de l'algorithme de Dijkstra sur le graphe modifié
previous_vertices_modified = dijkstra(modified_graph, start)
path_modified = construct_path(previous_vertices_modified, end)
print("Chemin le plus court de E à C (modifié) : ", path_modified)
print("Nombre de pièces intermédiaires (modifié) : ", len(path_modified) - 2)