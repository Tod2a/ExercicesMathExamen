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
#                           Exercice 1.4                               #
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

def PrintThridCol(matrice):
    if(len(matrice[0]) >=3):
        for row in matrice:
            print

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

M = np.array([[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]])
A = np.ones((3,3), dtype=int)
B = np.eye(5, dtype=float)
C = np.array([2,4,6,12,24,36]).reshape(3,2)

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\n---------------------------------------------\n")
print("Première matrice: ")
print(M)
print("\nélément m23 de cette matrice:")
print(M[1][2])
print("\nTroisème ligne: ")
print(M[2, :])
print("\nPremière colonne: ")
print(M[ :,0])
print("\nMatrice de 3x3 remplie de 1: ")
print(A)
print("\nMatrice unité diagonale 5x5 de type float: ")
print(B)
print("\nRéorganisation en matrice 3x2: ")
print(C)
print("\n---------------------------------------------\n")


#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
