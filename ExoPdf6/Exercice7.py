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
#                           Exercice 7                                 #
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
#                 utilisation d'un flou basé sur la médiane            #
#                                                                      #  
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques                       
#-----------------------------------------------------------------------

import time
import numpy as np 
from scipy.ndimage import convolve
from tkinter import *
from PIL import Image, ImageTk


#-----------------------------------------------------------------------
# Encodage des fonctions 
#-----------------------------------------------------------------------


def median_filter(image, size):
    height, width, channels = image.shape
    filtered_image = np.zeros_like(image)
    padding = size // 2
    
    for i in range(padding, height - padding):
        for j in range(padding, width - padding):
            for c in range(channels):
                neighborhood = image[i - padding:i + padding + 1, j - padding:j + padding + 1, c]
                filtered_image[i, j, c] = np.median(neighborhood)
    
    return filtered_image


#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

img = "images/Lenna512.png"

img_in = Image.open(img)
image = np.asarray(img_in)

mask = np.array([
    [0, 0, 0],
    [0.7, 0.2, 0.1],
    [0, 0, 0]
])

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------

# Encodez votre programme ici!
print("\nFiltre de flou basé sur la médiane de Lenna avec un masque 3x3\n")
print("\n---------------------------------------------\n")

start = time.time()

img_out1 = median_filter(image, 3)

end = time.time()

print(f"\nLe filtre de flou basé sur la médiane de Lenna est réussi, l'opération vous a pris: {end-start} secondes")

print("\n---------------------------------------------\n")

Image.fromarray(image).save("image_entree.png")
Image.fromarray(img_out1.astype(np.uint8)).save("image_sortie.png")

#-----------------------------------------------------------------------
# Affichage dans tkinter
#-----------------------------------------------------------------------

root = Tk()

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
