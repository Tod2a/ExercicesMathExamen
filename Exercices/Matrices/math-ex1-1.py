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
#                            Ex1.1 Enoncé                              #
#                                                                      #
# Premiers essais sans NumPy: utilisation des listes imbriquées pour   #
# manipuler des matrices                                               #      
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
print("Premiers essais de travail sur les matrices \navec les listes imbriquées \n ")

print("Affichage complet d'une liste imbriquée M: \n")

M= [[1,2,3],[4,5,6],[7,8,9]]
type( M)
print('M=', M)

print("\nAttention, comme toujours en informatique,\nles lignes et les colonnes commencent à 0 et non à 1 \n")
print("Pour afficher l'élément a23 comme dans le cours,\nil faut donc choisir la ligne 1 et la colonne2! \n")

print("Affichage de l'élément a23 (ici 6): \n")

print("a23 = ", M[1][2])

print("\nAffichage de la 3ème ligne:")
print("")
print("3ème ligne = ", M[2])

print("\nAffichage de la colonne [0] avec une boucle: \n")
col =0
col1 = []
for ligne in M:
    col1.append(ligne[col])
print("Première colonne = ", col1)

print("\nce n'est pas très pratique!!!")


#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
