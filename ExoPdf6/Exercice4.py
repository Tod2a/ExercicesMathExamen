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
#                           Exercice 1                                 #
#                      Fonction de convolution                         #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#       Crée une fonction qui fait la convolution entre une matrice    #
#                           et un masque                               #  
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques                       
#-----------------------------------------------------------------------

import time
import numpy as np 
import keyboard                 #attention il faut installer la bibliothèque avec pip
from scipy.ndimage import convolve
from tkinter import *
from PIL import Image, ImageTk


#-----------------------------------------------------------------------
# Encodage des fonctions 
#-----------------------------------------------------------------------

def blur_filter(matrix, mask_size):
    mask = np.ones((mask_size, mask_size)) / (mask_size * mask_size)
    # Si l'image est en couleur, appliquer le filtre sur chaque canal séparément
    if matrix.ndim == 3:
        blurred_matrix = np.zeros_like(matrix)
        for i in range(matrix.shape[2]):
            blurred_matrix[:, :, i] = convolve(matrix[:, :, i], mask, mode='constant', cval=0.0)
        return blurred_matrix
    else:
        return convolve(matrix, mask, mode='constant', cval=0.0)


#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

img = "images/Lenna512.png"

img_in = Image.open(img)
image = np.asarray(img_in)

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------

# Encodez votre programme ici!
print("\nFiltre de flou linéaire de Lenna avec un masque 3x3 et 10x10\n")
print("\n---------------------------------------------\n")

start = time.time()

img_out1 = blur_filter(image, 3)      

end = time.time()

print(f"\nle filtre 3x3 de lenna est réussit, l'opération vous a prit: {end-start} secondes")

start2 = time.time()

img_out2 = blur_filter(image, 10)

end2 = time.time()

print(f"\nle filtre 10x10 de lenna est réussit, l'opération vous a prit: {end2-start2} secondes")

print("\n---------------------------------------------\n")

Image.fromarray(image).save("image_entree.png")
Image.fromarray(img_out1).save("image_sortie.png")
Image.fromarray(img_out2).save("image_sortie2.png")


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

image_out2 = Image.open("image_sortie2.png")
photo5 = ImageTk.PhotoImage(image_out2)

canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo)
canvas.pack()

champ_label_result2 = Label(root, text="Image après transformation")
champ_label_result2.pack() 

canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo2)
canvas.pack()

canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo5)
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
