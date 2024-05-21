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
#                           Exercice 1.5                               #
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

def BuildGridMultiplied(grid1, grid2):
    grid = []
    if(np.shape(grid1)[1] == np.shape(grid2)[0]):
        for i in range(len(grid1)):
            row = []
            for j in range(len(grid2[i])):
                value = 0
                for k in range(len(grid2)):
                    value += grid1[i][k] * grid2[k][j]
                row.append(value)
            grid . append(row)
        return np.array(grid)
    else:
        return "Multiplication impossible car le nombre de colonnes de la premiere matrice n'est pas égal au nombre de lignes de la deuxième"

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

A = np.array([[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]])
B = np.array([[1, 1, 0], [1.0, 1, 1], [2, 2, 2]])
C = np.array([[1, 2], [0, 1], [3, 1]])
D = BuildGridMultiplied(A , B)
E = BuildGridMultiplied(A, C)
F = BuildGridMultiplied(C, A)

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\n---------------------------------------------\n")
print("Voici les Trois matrice: ")
print("\n A:")
print(A)
print("\n B:")
print(B)
print("\n C:")
print(C)
print("\nProduit d'Hadamard de AxB: ")
print(A*B)
#print(np.multiply(A,B))
print("\nProduit matriciel de A@B:")
print(A@B)
#print(np.dot(A,B))
print("\nEssai de multiplication de A@B avec ma fonction: ")
print(D)
print("\nEssai de multiplication de A@C avec ma fonction: ")
print(E)
print("\nEssai de multiplication de C@A avec ma fonction: ")
print(F)
print("\n---------------------------------------------\n")




#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
