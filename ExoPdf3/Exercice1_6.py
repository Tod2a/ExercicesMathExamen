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
#                               2022-2023                              #                      
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                                                                      #
#                           Exercice 1.6                               #
#                         Début avec NumPy                             #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#   Utilisation des arrays pour manipuler des matrices, écrire un pgm  #
#                     en python utilisant numpy                        #         
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques                       
#-----------------------------------------------------------------------

#import csv                                                             # nécessaire pour sauver les données en csv pour lire le fichier des paramètres
#import time
#import sys
#import os
import numpy as np                                                     # bibliothèque mathématique
#import numpy.linalg as alg
#import PIL
#from PIL import Image, ImageTk											
#import tkinter as tk                                                   # affichage fenêtre graphique
#import colorsys
#import matplotlib                                                      # bibliothèque d'affichage de courbes
#import matplotlib.pyplot as plt
#import scipy
#from scipy.ndimage import convolve
#from scipy import signal
#import cv2
#import skimage
#import sklearn
#import pandas
#import webcolors

#-----------------------------------------------------------------------
# Encodage des fonctions 
#-----------------------------------------------------------------------

def TryToMatricialProduct(grid1, grid2):
    if(np.shape(grid1)[1] == np.shape(grid2)[0]):
        return grid1@grid2
    else:
        return "Multiplication impossible car le nombre de colonnes de la premiere matrice n'est pas égal au nombre de lignes de la deuxième"

def TryToAdd(grid1, grid2):
    if(np.shape(grid1) == np.shape(grid2)):
        return grid1+grid2
    else:
        return "Les matrices ne sont pas de taille identique, l'addition n'est donc pas possible." 


#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

# Pas de variables

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\n---------------------------------------------\n")
firstRow = int(input("Combien de lignes doit contenir la premiere matrice"))
firstCol = int(input("Combien de colonnes doit contenir la premiere matrice"))
A = np.empty((firstRow, firstCol), dtype=float)
for i in range(firstRow):
    for j in range(firstCol):
        A[i,j]= float(input(f"Entrer l'élément à la position ({i+1}, {j+1}): "))
secondRow = int(input("Combien de lignes doit contenir la seconde matrice"))
secondCol = int(input("Combien de colonnes doit contenir la seconde matrice")) 
B = np.empty((secondRow, secondCol), dtype=float)
for i in range(secondRow):
    for j in range(secondCol):
        B[i,j]= float(input(f"Entrer l'élément à la position ({i+1}, {j+1}): "))
print("\nVoici votre première matrice: ")
print(A)
print("\nVoici votre seconde matrice: ")
print(B)
print("\nEssai de A@B")
print(TryToMatricialProduct(A, B))
print("\nEssai de B@A")
print(TryToMatricialProduct(B, A))
print("\nEssai de A+B")
print(TryToAdd(A, B))
C = A.transpose()
print("\nTransposition de A")
print(C)
print("\nNombre de lignes et de colonnes de cette transposition:")
print(C.shape)
print("\n---------------------------------------------\n")


#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
