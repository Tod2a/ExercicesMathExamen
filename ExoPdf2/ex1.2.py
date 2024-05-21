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
#                           Exercice 1.2                               #
#                         Début sans NumPy                             #                                                          
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
#                   en python sans utiliser numpy                      #         
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques                       
#-----------------------------------------------------------------------

#import csv                                                             # nécessaire pour sauver les données en csv pour lire le fichier des paramètres
#import time
#import sys
#import os
#import numpy as np                                                     # bibliothèque mathématique
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

#add doit être considéré comme un bool, à 1 cela additionne et à 0 cela soustrait
def AddOrSoustractMatrix(grid1, grid2, add):
    if (len(grid1) == len(grid2) and len(grid1[0]) == len(grid2[0])):
        grid = []
        if add:
            for i in range (len(grid1)):
                row = []
                for j in range (len(grid1[i])):
                    row.append(grid1[i][j] + grid2[i][j])
                grid.append(row)
            return grid
        else:
            for i in range (len(grid1)):
                row = []
                for j in range (len(grid1[i])):
                    row.append(grid1[i][j] - grid2[i][j])
                grid.append(row)
            return grid
    else:
        print("Addition/soustraction impossible!")

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\n---------------------------------------------\n")
print("Voici les deux matrice: ")
print("\n A:")
print(A)
print("\n B:")
print(B)
print("\n tentavie de A+B: ")
print(A + B)
print("Cela concatène les deux listes l'une après l'autre")
print("\nAddition correcte des deux matrices selon les règles du calculs matriciel: ")
print(AddOrSoustractMatrix(A, B, 1))
print("\n---------------------------------------------\n")


#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
