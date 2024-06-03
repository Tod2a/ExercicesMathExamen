import cv2

img_name = "cats2"

img = cv2.imread(f"images/{img_name}.jpg")
print(f"Dimensions de l'image {img_name}.jpg : {img.shape}\n")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




while True:
    pass  