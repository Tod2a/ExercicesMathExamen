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
#                           Exercice 12                                #
#                          lisser une image                            #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#       ouvre une image et crée une image lissée de cette image        #
#                                                                      #         
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques                       
#-----------------------------------------------------------------------

import time
from tkinter import *
from PIL import Image, ImageTk
import numpy as np 


#-----------------------------------------------------------------------
# Encodage des fonctions 
#-----------------------------------------------------------------------

def convolution(noyau, lin, col, image):
    valeur = 0
    for i in range(3):
        for j in range(3):
            valeur += noyau[i,j]*image[lin-1+i,col-1+j]
    return valeur
            

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

img = "images/Lenna512.png"

img_in = Image.open(img)
image = np.asarray(img_in)
nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]

noyau = np.ones((3, 3)) / 9.0
noyauG = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]])/16.0

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\nLissage d'une image avec numpy et PIL\n")
print("\n---------------------------------------------\n")

start = time.time()

img_out = np.copy(image)
for ligne in range(nb_lignes):
    for col in range(nb_colonnes):
        if (ligne > 0 and ligne < nb_lignes-1 and col > 0 and col < nb_colonnes-1):
            for i in range(3):
                img_out[ligne, col, i] = convolution(noyau, ligne, col, image[:,:,i])
            

end = time.time()

start2 = time.time()

img_out2 = np.copy(image)
for ligne in range(nb_lignes):
    for col in range(nb_colonnes):
        if (ligne > 0 and ligne < nb_lignes-1 and col > 0 and col < nb_colonnes-1):
            for i in range(3):
                img_out2[ligne, col, i] = convolution(noyauG, ligne, col, image[:,:,i])

end2 = time.time()

print("\nvous avez lissé l'image", img ,", l'opération vous a prit: ", end-start, " secondes")
print("\nvous avez lissé l'image", img ,", l'opération vous a prit: ", end2-start2, " secondes")

print("\n---------------------------------------------\n")

Image.fromarray(image).save("image_entree.png")
Image.fromarray(img_out).save("image_sortie.png")
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
