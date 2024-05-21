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
#                           Exercice 2.9                               #
#                       mixage de deux images                          #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#      crée un image qui est le mixe de deux images données            #
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



#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

img1 = "images/Lenna512.png"
img2 = "images/4-2-03.png"

img_in1 = Image.open(img1)
img_in2 = Image.open(img2)
image1 = np.asarray(img_in1)
image2 = np.asarray(img_in2)
nb_lignes1 = image1.shape[0]
nb_colonnes1 = image1.shape[1]
nb_lignes2 = image2.shape[0]
nb_colonnes2 = image2.shape[1]

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\nFusion de deux images avec numpy et PIL\n")
print("\n---------------------------------------------\n")

start = time.time()

img1divide = image1*0.6
img2divide = image2*0.4

imgouttest = img1divide + img2divide

img_out = np.asarray(imgouttest, dtype=np.uint8)

end = time.time()

print("\nvous avez fusionné l'image ", img1 ," avec ", img2 ,"l'opération vous a prit: ", end-start, " secondes")

print("\n---------------------------------------------\n")

Image.fromarray(image1).save("image_entree1.png")
Image.fromarray(image2).save("image_entree2.png")
Image.fromarray(img_out).save("image_sortie.png")


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

champ_label_result1 = Label(root, text="Images que l'on va fusionner")
champ_label_result1.pack() 
image_in = Image.open("image_entree1.png")
photo = ImageTk.PhotoImage(image_in)

image_in2 = Image.open("image_entree2.png")
photo3 = ImageTk.PhotoImage(image_in2)

image_out = Image.open("image_sortie.png")
photo2 = ImageTk.PhotoImage(image_out)

canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo)
canvas.pack()

canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo3)
canvas.pack()

champ_label_result2 = Label(root, text="Image après fusion")
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
