import cv2
import os
import sys

nom_image= "cats2"

image = cv2.imread("images/"+nom_image+".jpg")
print("Dimensions de l'image "+nom_image+".jpg : ",image.shape,"\n")

# on convertit l'image en noir et blanc
# l'algorithme que nous allons utilisé (cascades de Haar) a besoin de ce pretraitement pour bien fonctionner
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# on a besoin des fichiers xml résultats de l'entrainement car on ne fait ici
# que la prédiction, pas le training 
# https://github.com/opencv/opencv/tree/master/data/haarcascades

# on charge notre modèle

#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default_extended.xml")
cascPath = sys.argv[0]
print(cascPath)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface_extended.xml')
print(cv2.data.haarcascades)
print(cv2.data.haarcascades+ 'haarcascade_frontalcatface.xml')
print(face_cascade)
# on verifie que le modèle a bien été chargée
if face_cascade.empty()==True:
	print("Le fichier n'est pas chargé: \n", face_cascade.empty())
else:
	print("Le fichier est chargé.\n")

# On cherche tous les visages de chat disponibles dans l'image
faces = face_cascade.detectMultiScale(image_gray, 1.1, 5) #1,1 est le facteur d'échelle et n=5 donne le nombre de detection sur le même endroit
# on écrit dans la console le nombre de visages que  l'algorithme a détecté
print(f"{len(faces)} visages detectés dans l'image.\n")
print("Coordonnées des faces détectées:\n")
print(faces)
# on dessine un rectangle autour de chaque visage
for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    cv2.putText(image, 'Tete de chat detectee', (x, y-7),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

print ("\nC'est tout!")

# on sauvegarde l'image et on l'affiche
cv2.imwrite("new.jpg", image)
cv2.imshow('imgage',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
