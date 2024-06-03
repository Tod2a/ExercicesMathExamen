#!/usr/bin/env python
#-*- coding: utf8 -*-

#----------------------------------------------------------#
#                                                          #
#               Project Math-BacInfo-Python                #
#                      G. Barmarin                         #
#                                                          #
#                       2022-2023                          #
#                                                          #
#----------------------------------------------------------#

#----------------------------------------------------------#
#                Source: Gérard Barmarin                   #
#----------------------------------------------------------#

#----------------------------------------------------------#
#             AI reseau de neurones Classifier             #
#----------------------------------------------------------#

#import numpy as np
import cv2
import sklearn
#from sklearn.datasets import load_iris 
from sklearn import datasets
from sklearn.metrics import accuracy_score
#from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
#from sklearn.feature_extraction import DictVectorizer
#from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
#from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


def extract_digits(image_path):
    # Charger l'image
    image = cv2.imread(image_path)
    
    # Convertir en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Appliquer un seuillage pour obtenir une image binaire
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    
    # Trouver les contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filtrer les contours et extraire les chiffres
    digit_images = []
    for contour in contours:
        # Calculer le rectangle englobant pour chaque contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Filtrer les contours trop petits (éventuels bruits)
        if w >= 10 and h >= 10:  # Ajustez ces valeurs selon vos besoins
            # Extraire la région d'intérêt (ROI) correspondant au chiffre
            digit = gray[y:y+h, x:x+w]
            
            # Redimensionner l'image du chiffre à une taille de 8x8
            digit_resized = cv2.resize(digit, (8, 8))
            digit_images.append(digit_resized)
    
    return digit_images

digits = datasets.load_digits()
y = digits.target
x = digits.images.reshape((len(digits.images), -1))

image_path = "image.png"

# Extraire les chiffres de l'image
digit_images = extract_digits(image_path)

# Charger le modèle de classification MLP préalablement entraîné
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(15,), activation='logistic', alpha=1e-4, solver='sgd', tol=1e-4, random_state=1, learning_rate_init=.1, verbose=True)
mlp.fit(x, y)

# Afficher et prédire chaque chiffre extrait de l'image
predictions = []
for i, digit_image in enumerate(digit_images):
    # Aplatir l'image du chiffre
    digit_flattened = digit_image.reshape(1, -1)
    
    # Faire la prédiction
    prediction = mlp.predict(digit_flattened)
    predictions.append(prediction[0])
    
    # Afficher le chiffre extrait avec sa prédiction
    plt.subplot(1, len(digit_images), i+1)
    plt.imshow(digit_image, cmap='binary')
    plt.title(f'Prediction: {prediction[0]}')
    plt.axis('off')

# Afficher les prédictions pour tous les chiffres
plt.show()

# Afficher les prédictions sous forme de chaîne de caractères
predictions_string = ' '.join(map(str, predictions))
print("Prédictions des chiffres:", predictions_string)

while True:
    pass