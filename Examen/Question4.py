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
#                      Question 4                          #
#----------------------------------------------------------#

import cv2

img_name = "cats2"

img = cv2.imread(f"chat-cache-cache.jpg")
print(f"Dimensions de l'image {img_name}.jpg : {img.shape}\n")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cascPath = "haarcascade_frontalcatface_extended.xml"  # Nom du fichier XML
face_cascade = cv2.CascadeClassifier(cascPath)

# Vérifier que le modèle a bien été chargé
if face_cascade.empty():
    print("Loading error, no file found")
else:
    print("file is loaded\n")

faces = face_cascade.detectMultiScale(img_gray, 1.02, 5) 

print(f"{len(faces)} visages detectés dans l'image.\n")
print("Coordonnées des faces détectées:\n")
print(faces)


x_max, y_max, width_max, height_max = 0, 0, 0, 0
x_min, y_min, width_min, height_min = float('inf'), float('inf'), float('inf'), float('inf')

# Parcourir les coordonnées des faces détectées pour trouver les carrés les plus grands et les plus petits
for x, y, width, height in faces:
    if width * height > width_max * height_max:
        x_max, y_max, width_max, height_max = x, y, width, height
    if width * height < width_min * height_min:
        x_min, y_min, width_min, height_min = x, y, width, height

# Dessiner un cadre autour du plus grand carré détecté (Noirette)
cv2.rectangle(img, (x_max, y_max), (x_max + width_max, y_max + height_max), color=(0, 255, 0), thickness=2)
cv2.putText(img, 'Noirette: "Ou peut-elle bien etre?"', (x_max, y_max + height_max + 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

# Dessiner un cadre autour du plus petit carré détecté (Bianca)
cv2.rectangle(img, (x_min, y_min), (x_min + width_min, y_min + height_min), color=(0, 255, 0), thickness=2)
cv2.putText(img, 'Bianca: "Je suis ici"', (x_min, y_min + height_min + 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)


# on sauvegarde l'image et on l'affiche
cv2.imwrite("catFound.jpg", img)
cv2.imshow('imgage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


while True:
    pass  