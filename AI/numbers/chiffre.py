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

import numpy as np
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

digits = datasets.load_digits()


'''
La couche d'entrée nécessite un tableau unidimensionnel en entrée, mais nos images ont deux dimensions. 
Il nous faut donc les "aplatir" pour avoir 1797 images aplaties. Les deux dimensions de nos images 8x8 
ont été forcées vers une seule dimension en écrivant les lignes de 8 pixels les unes après les autres. 
La première image que nous avons affichée tout à l'heure est maintenant représentée par un tableau 1D avec 8x8 = 64 cases. 
Vous pouvez vérifier que les valeurs ci-dessous sont les mêmes que dans l'image 2D originale.
'''
y = digits.target
x = digits.images.reshape((len(digits.images), -1))
print(x.shape,"\n")
print(digits.images[0],"\n")
print(x[0],"\n")
chiffre = cv2.imread("image.png")


chiffre_grey = cv2.cvtColor(chiffre, cv2.COLOR_BGR2GRAY)
chiffre_8 = cv2.resize(chiffre_grey,(8,8))
chiffre_inverse = 255 - chiffre_8
chiffre_flattened = chiffre_inverse.reshape(1, 64)

# Print the flattened array
print("Ceci est chiffre (flattened):", chiffre_flattened)

'''
Séparation de l'ensemble en un ensemble d'entraînement contenant 1000 échantillons
et un ensemble de test comprenant le reste 
'''
x_train = x[:500]
y_train = y[:500]
x_test = x[500:]
y_test = y[500:]

'''
Nous pouvons maintenant créer le réseau de neurones. Nous utilisons une couche cachée avec 15 neurones, 
et scikit-learn trouve automatiquement le nombre de neurones à utiliser dans les couches d'entrée et de sortie. 
MLP = perceptron multicouches
'''
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(15,), activation='logistic', alpha=1e-4,solver='sgd', tol=1e-4, random_state=1,learning_rate_init=.1, verbose=True)

'''
Entrainons le reseau et imprimons l'écart à chaque itération
'''
print(mlp.fit(x_train,y_train),"\n")

'''
Testons les prédictions sur les 50 premières images de l'ensemble de test
et comparons-les aux étiquettes des 50 premières images de test:
On constate que presque la totalité des prédictions correspondent à la vérité.
'''
predictions = mlp.predict(chiffre_flattened)
print("Prédictions (50 premiers échantillons du test): \n",predictions,"\n") 
# print("Etiquettes (50 premiers échantillons du test): \n",y_test[:50],"\n")

'''
Affichons le taux de performance
'''
#print("Précision:",100*np.around(accuracy_score(y_test, predictions), decimals=5),"%\n")

# error = (predictions != y_test)
#print (error,"\n")
# print(100*np.around(np.sum(error)/len(y_test),decimals=4),"% d'erreurs\n")

# # x_error = x_test[error].reshape((-1,8,8))
# # #print (x_error,"\n")
# # y_error = y_test[error]
# # print("Etiquettes: \n",y_error,"\n")
# # y_pred_error = predictions[error]
# print("Prédictions erronnées: \n",y_pred_error,"\n")

i = 1
print(np.shape(chiffre_flattened))
print(chiffre_flattened)
chiffre_final = chiffre_flattened.reshape(8, 8)
plt.imshow(chiffre_final, cmap = 'binary')
plt.title(f'cible: {1}, prediction: {predictions}')
plt.axis('off')
plt.show()

while True:
    pass  