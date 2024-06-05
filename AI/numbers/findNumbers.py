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
#                 Source: Copin Thomas                     #
#----------------------------------------------------------#

#----------------------------------------------------------#
#             AI reseau de neurones Classifier             #
#----------------------------------------------------------#

import cv2
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier


def extract_digits(image_path):
    chiffre = cv2.imread("images/chiffre5.png")


    chiffre_grey = cv2.cvtColor(chiffre, cv2.COLOR_BGR2GRAY)
    chiffre_8 = cv2.resize(chiffre_grey,(8,8))
    chiffre_inverse = 255 - chiffre_8
    chiffre_flattened = chiffre_inverse.reshape(1, 64)
    return chiffre_flattened


def train_classifier():
    digits = datasets.load_digits()
    y = digits.target
    x = digits.images.reshape((len(digits.images), -1))
    mlp = MLPClassifier(hidden_layer_sizes=(15,), activation='logistic', alpha=1e-4, solver='sgd', tol=1e-4, random_state=1, learning_rate_init=.1, verbose=True)
    mlp.fit(x, y)
    return mlp


def predict_digit(model, digit_image):
    prediction = model.predict(digit_image)
    return prediction


def show_prediction(prediction, digit_images):
    chiffre_final = digit_images.reshape(8, 8)
    plt.imshow(chiffre_final, cmap = 'binary')
    plt.title(f'cible: {1}, prediction: {prediction}')
    plt.axis('off')
    plt.show()

