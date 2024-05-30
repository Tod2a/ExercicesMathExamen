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
#                           Ex Labyrinthe                              #
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

def voisins(p, M, N):
	# renvoie dans s les voisins de tous les sommets admissible de p
    s = [gauche(p), droit(p), bas(p), haut(p)]
    return [v for v in s if admissible(v, M, N)]

def gauche(p):
	#calcule les coordonnées du voisin de gauche
    x, y = p
    return (x - 1, y)

def droit(p):
    x, y = p
    return (x + 1, y)

def bas(p):
    x, y = p
    return (x, y - 1)

def haut(p):
    x, y = p
    return (x, y + 1)

def admissible(v, M, N):
	# vérifie qu'un voisin existe (détection des bords)
    x, y = v
    return x >= 0 and x < M and y >= 0 and y < N

def melanger(s):
	# la fonction mélanger introduit le côté aléatoire pour créér des labyrinthes différents à chaque fois.
    n = len(s)
    for k in range(n):
       j = random.randint(k, n - 1)
       s[j], s[k] = s[k], s[j]
    return s
 

#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

M = int(input("largeur du Labyrinthe?\n")) 								# largeur du labyrinthe

N = int(input("longueur du Labyrinthe?\n"))								# Longueur du labyrinthe

while True:
	print("\nChoisissez un point au hasard:\n")
	z=int(input("valeur de x (< M-1)?"))
	w=int(input("valeur de y (< N-1)?"))
	p=(z,w)
	r=voisins(p, M, N)
	print("Voisins admissibles:                     ",r)	
	m=melanger(r)
	print("Voisins mélangés premier tirage au sort: ",m)
	m=melanger(r)
	print("Voisins mélangés second tirage au sort : ",m)
