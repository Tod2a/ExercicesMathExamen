from tkinter import *
from PIL import Image, ImageTk
import numpy as np 


img = "ima_cache-2022-2023.bmp"

img_in = Image.open(img)
image = np.asarray(img_in)

image = image.copy()


nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]


for i in range(nb_lignes):
    for j in range(nb_colonnes):
        for k in range(3):
            image[i,j,k] = image[i,j,k]%16

for i in range(nb_lignes):
    for j in range(nb_colonnes):
        for k in range(3):
            image[i,j,k] = image[i,j,k]*16

Image.fromarray(image).save("resultat.png")

root=Tk()

empty_line0 = Label(root, text="")
empty_line0.pack()
empty_line00 = Label(root, text="EXAMEN DE MATH: TRAITEMENT D'IMAGES")
empty_line00.pack()
empty_line2 = Label(root, text="")
empty_line2.pack()

champ_label_result1 = Label(root, text="Message décodé : ")
champ_label_result1.pack() 
image_in = Image.open("resultat.png")
photo = ImageTk.PhotoImage(image_in)

canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo)
canvas.pack()

empty_line3 = Label(root, text="")
empty_line3.pack()
bouton_valider = Button(root, text="Quit", command=root.destroy)
bouton_valider.pack()
empty_line4 = Label(root, text="")
empty_line4.pack()
root.mainloop()