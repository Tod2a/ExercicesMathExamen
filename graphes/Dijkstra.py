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
import random														   # génération de nombre aléatoires

#-----------------------------------------------------------------------
# encodage des fonctions 
#-----------------------------------------------------------------------

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

#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

#