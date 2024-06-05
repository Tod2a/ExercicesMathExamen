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
#                      Question 1                          #
#----------------------------------------------------------#

import numpy as np

print("\nNous allors représenter les prix des tournées sous forme d'équations")
print("\nX = coca, Y = orval, Z = leffe, W = chimay et v = thé")
print("\néquation 1 = 0x + 2y + 2Z + 0w + 1v = 20,4")
print("\néquation 2 = 0x + 1y + 2z + 1w + 1v = 14.6")
print("\néquation 3 = 2x + 0y + 1z + 1w + 1v = 16.8")
print("\néquation 4 = 2x + 0y + 1z + 0w + 2v = 20.6")
print("\néquation 5 = 1x + 0y + 0z + 0w + 1v = 5.3")

coef = np.array([
    [0, 2, 2, 0, 1],
    [0, 1, 2, 1, 1],
    [2, 0, 1, 1, 1],
    [2, 0, 1, 0, 2],
    [1, 0, 0, 0, 1]
], dtype=float)

t = np.array([20.4, 14.6, 16.8, 20.6, 5.3], dtype=float)
     
print("\nVoici donc la matrice des coefficients: ")
print(coef)
print("\nEt voici la matrice des termes indépendants: ")
print(t)

values = np.linalg.solve(coef, t)
values = np.round(values, 1)
print("\nVoici donc la matrice obtenue en résolvant le système d'équation linéraire:")
print(values)
print(f"\nOn peux donc déduire que le coca vaut {values[0]}")
print(f"\nQue l'orval vaut {values[1]}")
print(f"\nQue la leffe vaut {values[2]}")
print(f"\nQue la chimay vaut {values[3]}")
print(f"\nQue le thé vaut {values[4]}")


#En résolvant ce système d'équation nous obtenons des valeurs négatives pour deux valeurs
#Nous devons déterminer le prix des boissons de nos amis, un prix ne peux pas être négatif
#cela prouve bien qu'une erreur à eu lieu dans les tickets des tournées
print(f"On remarque que le prix de la chimay et celui du thé sont négatif avec cette résolution")
print(f"Voici le calcul avec l'erreur de ticket corrigé et les termes indépendant des équations 2 et 4 inversés:")

t = np.array([20.4, 20.6, 16.8, 14.6, 5.3], dtype=float)

values = np.linalg.solve(coef, t)

values = np.round(values, 1)

print("\nVoici donc la matrice obtenue en résolvant le système d'équation linéraire:")
print(values)
print(f"\nOn peux donc déduire que le coca vaut {values[0]}")
print(f"\nQue l'orval vaut {values[1]}")
print(f"\nQue la leffe vaut {values[2]}")
print(f"\nQue la chimay vaut {values[3]}")
print(f"\nQue le thé vaut {values[4]}")

print(f"Le prix de la 6ème tournée aurait été de {values[0] + 2*values[1] + values[2] + values[3]}")


while True:
    pass