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
#                           Ex Labyrinthe1                             #
#                                                                      #                                                         
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques
#-----------------------------------------------------------------------

import matplotlib.pyplot as plt
import random														   # génération de nombre aléatoires
from Dijkstra import dijkstra, construct_path

#-----------------------------------------------------------------------
# encodage des fonctions 
#-----------------------------------------------------------------------

def neighbors(summit, length, width):
    #return à list with all eligible neighbors of the summit
    summits = [left(summit), right(summit), bottom(summit), high(summit)]
    return [s for s in summits if eligible(s, length, width)]


def left(summit):
	#return the location of the left neighbor
    x, y = summit
    return (x - 1, y)


def right(summit):
    x, y = summit
    return (x + 1, y)


def bottom(summit):
    x, y = summit
    return (x, y - 1)


def high(summit):
    x, y = summit
    return (x, y + 1)


def eligible(summit, length, width):
	# verify than summit is valid
    x, y = summit
    return x >= 0 and x < length and y >= 0 and y < width


def mix(summits):
    l = len(summits)
    for i in range(l):
        j = random.randint(i, l-1)
        summits[j], summits[i] = summits[i], summits[j]


def set_lab(start, length, width):
    visits = set([start])
    s = [start]
    fathers = {}
    graph = {start: neighbors(start, length, width)}
    
    while s != []:
        summit = s.pop()
        near = neighbors(summit, length, width)
        mix(near)
        if summit not in graph:
            graph[summit] = []
        for t in near:
            if t not in visits:
                visits.add(t)
                s.append(t)
                fathers[t] = summit
                if t not in graph:
                    graph[t] = []
                graph[summit].append(t)
                graph[t].append(summit)
    
    return fathers, graph


def plot_labyrinth(fathers, length, width, lab=True):
    d = 0.5
    plt.axis([-1, length, -1, width])
    for x in range(length + 1):
        plt.plot((x - d, x - d), (-d, width - d), 'k')
    for y in range(width + 1):
        plt.plot((-d, length - d), (y - d, y - d), 'k')
        for (x, y) in fathers:
            (a, b) = fathers[(x, y)]
            if a == x + 1: plt.plot((x+d,x+d),(y-d,y+d),'w')
            elif a == x - 1: plt.plot((x-d,x-d),(y-d,y+d),'w')
            elif b == y + 1: plt.plot((x-d,x+d),(y+d,y+d),'w')
            elif b == y - 1: plt.plot((x-d,x+d),(y-d,y-d),'w')
            if lab: plt.plot((x,a), (y,b), 'r')
    #plt.show()


def show_path(fathers, length, width, path):
    plot_labyrinth(fathers, length, width)
    for k in range(len(path) - 1):
        (x, y) = path[k]
        (a, b) = path[k + 1]
        plt.plot((x, a), (y, b), 'g')
    plt.show()


#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

m = int(input("largeur du Labyrinthe?\n")) 								# largeur du labyrinthe

n = int(input("longueur du Labyrinthe?\n"))								# Longueur du labyrinthe

px = int(input("x du Point de départ?\n"))
py = int(input("y du Point de départ?\n"))
qx = int(input("x du Point d'arrivée?\n"))
qy = int(input("y du Point d'arrivée?\n"))

start = (px, py)
end = (qx, qy)

fathers, graph = set_lab((m // 2, n // 2), m, n)

previous_vertices = dijkstra(graph, start)
path = construct_path(previous_vertices, end)

show_path(fathers, m, n, path)


