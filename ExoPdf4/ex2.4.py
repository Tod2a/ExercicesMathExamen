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
#                           Exercice 2.4                               #
#                           image miroir                               #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#      ouvre une image et crée une image inversée de cette image       #
#                                                                      #         
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques                       
#-----------------------------------------------------------------------

#import csv                                                             # nécessaire pour sauver les données en csv pour lire le fichier des paramètres
import time
#import sys
#import os
import numpy as np                                                     # bibliothèque mathématique
#import numpy.linalg as alg
import PIL
from PIL import Image, ImageTk											
#import tkinter as tk   
from tkinter import *                                                # affichage fenêtre graphique
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

def reverse_horizontal(img):
    img_start = Image.open(img)
    img_array = np.asarray(img_start)
    length = img_array.shape[0]
    width = img_array.shape[1]

    new_array = np.zeros((length, width, 3))  

    for i in range(length):
        for j in range(width):
            reverse_column = width - 1 - j
            new_array[i][j] = img_array[i][reverse_column]

    return Image.fromarray(new_array)

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

img = "images/Lenna512.png"

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\nInversion d'une image avec numpy et PIL\n")
print("\n---------------------------------------------\n")

start = time.time()

img_in = Image.open(img).save("image_entree.png")
img_out = reverse_horizontal(img).save("image_sortie.png")

end = time.time()

print("\nvous avez inversé l'image, l'opération vous a prit: ", end-start, " secondes")

print("\n---------------------------------------------\n")


#-----------------------------------------------------------------------
# Affichage dans tkinter
#-----------------------------------------------------------------------

root=Tk()

empty_line0 = Label(root, text="")
empty_line0.pack()
empty_line00 = Label(root, text="LABO COURS DE MATH: TRAITEMENT D'IMAGES")
empty_line00.pack()
champ_label_result0 = Label(root, text="On affiche l'image avant transformation et après")
champ_label_result0.pack()
empty_line2 = Label(root, text="")
empty_line2.pack()

champ_label_result1 = Label(root, text="Image avant transformation")
champ_label_result1.pack() 
image_in = Image.open("image_entree.png")
photo = ImageTk.PhotoImage(image_in)

image_out = Image.open("image_sortie.png")
photo2 = ImageTk.PhotoImage(image_out)

canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo)
canvas.pack()

champ_label_result2 = Label(root, text="Image après transformation")
champ_label_result2.pack() 

canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo2)
canvas.pack()

empty_line3 = Label(root, text="")
empty_line3.pack()
bouton_valider = Button(root, text="Quit", command=root.destroy)
bouton_valider.pack()
empty_line4 = Label(root, text="")
empty_line4.pack()
root.mainloop()


#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
