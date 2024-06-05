#!/usr/bin/env python
#-*- coding: utf8 -*-

#----------------------------------------------------------#
#                                                          #
#               Examen Mathématique Bac Info               #
#                      G. Barmarin                         #
#                                                          #
#                       2022-2023                          #
#                                                          #
#----------------------------------------------------------#

#----------------------------------------------------------#
#                 Source: Copin Thomas                     #
#----------------------------------------------------------#

#----------------------------------------------------------#
#                      Question 3                          #
#----------------------------------------------------------#

from tkinter import *
from PIL import Image, ImageTk
import numpy as np 

img = "troll200-encode.png"

img_in = Image.open(img)
image = np.asarray(img_in)

image = image.copy()


nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]

message = ""
for i in range(nb_lignes):

    lower_4_bits = image[i, 0, 0] % 16
    

    upper_4_bits = image[i, -1, 2] % 16
    

    ascii_val = (upper_4_bits << 4) | lower_4_bits
    

    message += chr(ascii_val)


print(f"Message décodé: {message}")


img = "troll200.png"

img_in = Image.open(img)
image = np.asarray(img_in)

image = image.copy()


nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]

message = "Ca dépend quel exercices mais en python, chat GPT est pas très malin"
message = message.ljust(nb_lignes)

for i in range(nb_lignes):
    if i >= len(message):
        break
    char = message[i]
    ascii_val = ord(char)
    
    # Extraire les 4 bits de poids faibles et de poids forts de l'ASCII
    lower_4_bits = ascii_val & 0x0F
    upper_4_bits = (ascii_val >> 4) & 0x0F
    
    # Mettre à jour les pixels de la première et de la dernière colonne avec les bits de poids faibles et forts
    image[i, 0, 0] = (image[i, 0, 0] & 0xF0) | lower_4_bits
    image[i, -1, 2] = (image[i, -1, 2] & 0xF0) | upper_4_bits

modified_img = Image.fromarray(image)
modified_img.save("troll200.png")





while True:
    pass