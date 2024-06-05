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

import numpy as np

print("Question 1:")
print("Oui ce graphe est connexe, tout les sommets sont reliés par une arrête, il n'y a pas de paire de sommet nont reliée aux autres")
print("Question 2:")
print("Ce n'est pas un arbre car il y à la présence d'un cycle (F-G-E-D-F) et même d'autres")
print("Question 3:")
print("Oui en partant de A on peut tout à fait parcourir le graph en largeur")
print("Question 4:")
print("Oui en peux faire un parcours en profondeur en partant de F")
print("Question 5:")
print("ordre 7 (7 sommets)")
print("Question 6:")
print("Taille 10 (10 arrêtes)")
print("Question 7:")
print("Comme ce graphe possède 7 sommets, 10 arrêtes et 4 faces, le graphe n'est pas plainaire d'après euler (7−10+4!=2)")
print("Question 8:")
print("le degré de F est 4 (4 arrêtes le relient à d'autres sommets)")
print("Question 9:")
print("Oui, il existe une arrête entre E et F ils sont donc adjacents")
print("Question 10:")

matrice = np.array([
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
])

print(matrice)

while True:
    pass