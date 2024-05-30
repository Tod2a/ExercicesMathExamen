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
#----------------------------------------------------------------------#.pyplot as plt

#-----------------------------------------------------------------------
# Importation des bibliothèques
#-----------------------------------------------------------------------

import matplotlib.pyplot as plt
import random														   # génération de nombre aléatoires

#-----------------------------------------------------------------------
# encodage des fonctions 
#-----------------------------------------------------------------------


def plot_labyrinthe( M, N, lab=True):
    d = 0.5
    plt.axis([-1, M, -1, N])
    for x in range(M + 1):
        print("Ligne verticale",x,"de (x-d,x-d):",(x - d, x - d), "vers (-d,N-d):",(-d, N - d))
        plt.plot((x - d, x - d), (-d, N - d), 'k')						# dessin des bords verticaux en noir (k=black)
																		# distant d'une unité, commençant à -0,5 (0-d) et allant jusqu'à M-0,5 (M-d)
    print("\n")															# verticalement, les traits vont de -0,5 (-d) à N-0,5 (N-d)
    for y in range(N + 1):
        print("Ligne horizontale",y,"de (-d,M-d):",(- d, M - d), "vers (y-d,y-d):",(y - d, y - d))
        plt.plot((-d, M - d), (y - d, y - d), 'b')						# dessin des bords horizontaux en noir (b=blue)
																		# horizontalement, les traits vont de -0,5 (-d) à M-0,5 (M-d)
																		# distant d'une unité, commençant à -0,5 (0-d) et allant jusqu'à N-0,5 (N-d)
    plt.plot((0,2),(2,2),'g')    										# Tracé d'une ligne verte horizontale du cente du carré (0,2) à une hauteur constante de 2
    print("\nTracé d'une ligne verte horizontale du cente du carré (0,2) à une hauteur constante de 2")	
    plt.plot((1,1),(0,2),'yellow')
    print("\nTracé d'une ligne verticale jaune en 1 allant de 0 à 2")		# Tracé d'une ligne verticale jaune en 1 allant de 0 à 2
    plt.show()


#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

M = int(input("largeur du Labyrinthe?\n")) 								# largeur du labyrinthe

N = int(input("longueur du Labyrinthe?\n"))								# Longueur du labyrinthe

print("Ajout des lignes horizontales de la grille",M,"x",N,"\navec la case en bas à gauche centrée en (0,0)\n")

plot_labyrinthe( M, N)													# Dessin de la grille
