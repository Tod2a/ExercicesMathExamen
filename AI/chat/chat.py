import cv2

img_name = "cats2"

img = cv2.imread(f"images/{img_name}.jpg")
print(f"Dimensions de l'image {img_name}.jpg : {img.shape}\n")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cascPath = "haarcascade_frontalcatface_extended.xml"  # Nom du fichier XML
face_cascade = cv2.CascadeClassifier(cascPath)

# Vérifier que le modèle a bien été chargé
if face_cascade.empty():
    print("Loading error, no file found")
else:
    print("file is loaded\n")

faces = face_cascade.detectMultiScale(img_gray, 1.1, 5) 

print(f"{len(faces)} visages detectés dans l'image.\n")
print("Coordonnées des faces détectées:\n")
print(faces)


for x, y, width, height in faces:
    cv2.rectangle(img, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    cv2.putText(img, 'Chat', (x, y-7),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)


# on sauvegarde l'image et on l'affiche
cv2.imwrite("new.jpg", img)
cv2.imshow('imgage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


while True:
    pass  