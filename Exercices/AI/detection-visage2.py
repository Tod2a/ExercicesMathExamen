import cv2
import os
import sys
image = cv2.imread("girl.jpg")
print("Dimensions de l'image: ",image.shape)

# on convertit l'image en noir et blanc
# l'algorithme que nous allons utilisé a besoin de ce pretraitement
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("new2.jpg", image_gray)
cv2.imshow('imgage',image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# on a besoin de ce fichier on ne fait ici
# que la prédiction, pas le training 
#https://github.com/opencv/opencv/tree/master/data/haarcascades

# on charge notre modèle
#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#cascPath = sys.argv[0]
#print(cascPath)
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print(cv2.data.haarcascades)
# on verifie que le modèle a bien été chargée
if face_cascade.empty()==True:
	print("Le fichier n'est pas chargé: ", face_cascade.empty())
else:
	print("Le fichier est chargé.")

# On cherche tous les visages disponibles dans l'image
faces = face_cascade.detectMultiScale(image_gray, 1.1, 5)
# on écrit dans la console le nombre de visages que  l'algorithme a détecté
print(f"{len(faces)} visages detectés dans l'image.")

# on dessine un rectangle autour de chaque visage
for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

print ("C'est tout bon!")

# on sauvegarde l'image
#cv2.imwrite("new.jpg", image)
#cv2.imshow('imgage',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
