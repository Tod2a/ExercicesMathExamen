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
#                           Exercice 1.1                               #
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

def PrintGrid(grid):
    for i in range(len(grid)):
        print(grid[i])  

def GetFirstCol(grid):
    newgrid = []
    for i in range(len(grid)):
        newgrid.append(grid[i][0])
    return newgrid

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

M = [[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]]

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\n---------------------------------------------\n")
print("Voici la matrice: ")
PrintGrid(M)
print("\nVoici l'élément m23: ")
print(M[1][2])
print("\nVoici la 3eme ligne: ")
print(M[2])
print("\nVoici la première colonne: ")
print(GetFirstCol(M))
print("\n---------------------------------------------\n")


#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
