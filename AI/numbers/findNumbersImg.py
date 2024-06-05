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

from findNumbers import extract_digits, train_classifier, predict_digit, show_prediction

img = "images/chiffre5.png"

mlp_model = train_classifier()

digit = extract_digits(img)

prediciton = predict_digit(mlp_model, digit)

show_prediction(prediciton, digit)