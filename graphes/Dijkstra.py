#-*- coding: utf8 -*-
########################################################################
'''
  _   __    _   _____  _   _                         _   _
 |  \/  |  /_\ |_   _|| |_| | (_) _  _   ____  _  _ | |_| |_   ___  _ _
 | |\/| | / _ \  | |  |  _  | | || \| | |  _ \| || ||  _| _ \ / _ \| \ |
 |_|  |_|/_/ \_\ |_|  |_| |_| |_||_|\_| |  __/\_, /  \__|_||_|\___/|_\_|
                                        |_|   |__/
'''
########################################################################


#----------------------------------------------------------------------#
#                                                                      #
#             Cours de Mathématiques pour BAC Info chap. 2             #
#                      Opérations sur les graphes                      #
#                            G. Barmarin                               #
#                             2023-2024                                #
#                                                                      #
#----------------------------------------------------------------------#


#----------------------------------------------------------------------#
#                                                                      #
#                       Algorithme de Dijkstra                         #
#                Fonction à imporer dans d'autres fichier              #                                                         
#                   pour résoudre les labyrinthes                      #
#                                                                      #
#                            Copin Thomas                              #
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques
#-----------------------------------------------------------------------

import matplotlib.pyplot as plt

#-----------------------------------------------------------------------
# encodage des fonctions 
#-----------------------------------------------------------------------

def dijkstra(graph, start):
    # Initialisation des distances : chaque sommet a une distance infinie, sauf le sommet de départ qui a une distance de 0.
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Initialisation des prédécesseurs : chaque sommet n'a pas de prédécesseur au début.
    previous_vertices = {vertex: None for vertex in graph}
    
    # Liste des sommets à visiter, initialisée avec tous les sommets du graphe.
    vertices = list(graph.keys())
    
    # Boucle principale : tant qu'il y a des sommets à visiter.
    while vertices:
        # Sélection du sommet avec la plus petite distance parmi les sommets non visités.
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])
        
        # Retrait du sommet sélectionné de la liste des sommets à visiter.
        vertices.remove(current_vertex)
        
        # Si la plus petite distance est infinie, les sommets restants sont inaccessibles, donc on arrête la boucle.
        if distances[current_vertex] == float('infinity'):
            break
        
        # Parcours de tous les voisins du sommet actuel.
        for neighbor in graph[current_vertex]:
            # Calcul de la distance alternative pour atteindre le voisin.
            # Note : ici, on suppose que le poids de chaque arête est 1 (ce n'est pas générique pour des graphes pondérés).
            alternative_route = distances[current_vertex] + 1
            
            # Si la distance alternative est plus courte, on met à jour la distance et le prédécesseur du voisin.
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_vertices[neighbor] = current_vertex
    
    # Renvoie le dictionnaire des prédécesseurs pour permettre la reconstruction des chemins.
    return previous_vertices

def construct_path(previous_vertices, target):
    # Initialisation du chemin vide.
    path = []
    
    # Commence par le sommet cible.
    current_vertex = target
    
    # Remonte les prédécesseurs jusqu'à atteindre le sommet de départ (None).
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    
    # Le chemin est reconstruit à l'envers, on le renverse pour obtenir l'ordre correct.
    path.reverse()
    
    # Renvoie le chemin reconstruit.
    return path


#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

#