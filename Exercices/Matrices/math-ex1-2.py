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
#                 Cours de Mathématiques pour BAC Info                 #
#                            G. Barmarin                               #
#                                                                      #                                                        
#                              2023-2024                               #                      
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                                                                      #
#                Exercice 1.1 Premiers essais sans Numpy               #                                                        
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                      Source: Gérard Barmarin                         #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#                            Ex1.2 Enoncé                              #
#                                                                      #
# Premiers essais sans NumPy: utilisation des listes imbriquées pour   #
# faire la somme de 2 matrices                                         #      
#                                                                      #
#----------------------------------------------------------------------#

#-----------------------------------------------------------------------
# Importation des bibliothèques
#-----------------------------------------------------------------------

#import csv                                                             # nécessaire pour sauver les données en csv pour lire le fichier des paramètres
#import tkinter                                                         # affichage fenêtre graphique
#from PIL import Image                                                  # ouverture de fichiers image
#import numpy as np                                                     # bibliothèque mathématique
#import matplotlib                                                      # bibliothèque d'affichage de courbes

#-----------------------------------------------------------------------
# Encodage des fonctions 
#-----------------------------------------------------------------------

# Pas de fonctions définies

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

# Pas d'initialisation de variables

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


print("Premiers essais avec des listes, sans NumPy")
print("------------------------------------------- \n")
print("Addition de deux matrices \navec les listes imbriquées \n ")

print("Affichage cde la première matrice A: \n")

A= [[1,2,3],[4,5,6],[7,8,9]]

print('A=', A)

print("\nAffichage de la deuxième matrice B: \n")

B= [[9,9,9],[9,9,9],[9,9,9]]

print('B=', B)

print("\nCalcul et affichage de la somme A + B telle quelle: \n")

D = A + B

print("D = ", D, "\n\nOn constate que la somme de deux listes correspond à leur concaténation! \nCe n'est pas ce que l'on cherche!\n")

n=len(A)      # n contient le nombre d'élément de A soit le nombre de lignes
m=len(A[0])   # m contient le nombre d'élément d'un élément de A (ici le premier) soit le nombre de colonnes
print ("La matrice est de dimension "+str(n)+" x "+str(m)+"\n")

C = A  # E recopiant la matrice A dans C, C aura la même taille que A et écrasera son contenu avec la somme calculée

for i in range(0,n):
    for j in range(0,m):
        C[i][j] = A[i][j] + B[i][j]    
print("C = ", C)

print("\nC'est laborieux, vivement NumPy!!!\n")

