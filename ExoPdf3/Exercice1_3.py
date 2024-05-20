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
#                           Exercice 1.3                               #
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
#           en python utilisant numpy qui affiche les arrays           #
#                        et calcule A + B                              #         
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

# Pas de fonctions définies

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

A = np.array([[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]])
B = np.array([[1, 1, 0], [1.0, 1, 1], [2, 2, 2]])
sum_array = np.add(A, B)

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\n---------------------------------------------\n")
print("Première matrice: " )
print(A)
print("\n Deuxième matrice: \n",)
print(B)
print("Somme des deux: ")
print(sum_array)
print("\n---------------------------------------------\n")
print("Il s'agit d'une addition élément par élément des deux matrices\n")

#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
