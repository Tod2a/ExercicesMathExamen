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
#                      Question 2                          #
#----------------------------------------------------------#

import math

nom_du_fichier = "message.txt"

with open(nom_du_fichier, 'r', encoding='utf-8') as fichier:
    message = fichier.read()

comptage_lettres = {}
total_lettres = 0

for char in message:
    if char.isalpha():
        char = char.lower()
        if char in comptage_lettres:
            comptage_lettres[char] += 1
        else:
            comptage_lettres[char] = 1
        total_lettres += 1


frequences_lettres = {lettre: (comptage / total_lettres) * 100 for lettre, comptage in comptage_lettres.items()}

frequences_langues = {
    "Albanais": {"A": 7.56, "E": 17.46, "H": 4.19, "I": 9.10, "J": 2.77, "O": 3.93, "R": 7.28, "S": 5.49, "T": 8.37, "U": 3.44},
    "Croate": {"A": 11.27, "E": 8.43, "H": 1.04, "I": 10.04, "J": 5.15, "O": 9.01, "R": 5.47, "S": 5.84, "T": 4.47, "U": 4.33},
    "Estonien": {"A": 14.13, "E": 10.82, "H": 1.81, "I": 9.53, "J": 1.79, "O": 5.61, "R": 2.76, "S": 7.57, "T": 7.51, "U": 5.66},
    "Français": {"A": 8.70, "E": 17.82, "H": 1.08, "I": 6.94, "J": 0.71, "O": 5.27, "R": 6.43, "S": 7.91, "T": 7.11, "U": 6.05},
    "Letton": {"A": 15.87, "E": 7.81, "H": 0.22, "I": 11.25, "J": 2.55, "O": 3.85, "R": 5.58, "S": 8.06, "T": 6.04, "U": 5.16},
    "Tchèque": {"A": 7.20, "E": 11.55, "H": 2.33, "I": 6.54, "J": 2.30, "O": 7.99, "R": 3.40, "S": 4.49, "T": 5.72, "U": 3.17}
}

print("\nVoici les fréquences des lettres de notre texte")
print(frequences_lettres)

distances = {}
for langue, frequences in frequences_langues.items():
    distance = 0
    for lettre, freq in frequences.items():
        freq_texte = frequences_lettres.get(lettre.lower(), 0)
        distance += (freq_texte - freq) ** 2
    distances[langue] = math.sqrt(distance)

# Trouver la langue avec la plus petite distance
langue_probable = min(distances, key=distances.get)

print("\nVoici le tableau des distances euclidiennes:")
print(distances)
print(f"\nLa langue la plus probable est : {langue_probable}")

while True:
    pass
