#-*- coding: utf8 -*-

########################################################################
'''
  _   __    _   _____  _   _                         _   _
 |  \/  |  /_\ |_   _|| |_| | (_) _  _   ____  _  _ | |_| |_   ___  _ _
 | |\/| | / _ \  | |  |  _  | | || \| | |  _ \| || ||  _| _ \ / _ \| \ |
 |_|  |_|/_/ \_\ |_|  |_| |_| |_||_|\_| |  __/\_, /  \__|_||_|\___/|_\_|
                                        |_|   |__/
'''
########################################################################
#----------------------------------------------------------------------#
#                                                                      #
#                 Cours de Mathématiques pour BAC Info                 #
#                            G. Barmarin                               #
#                                                                      #                                                        
#                               2022-2023                              #                      
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                                                                      #
#                         Introduction à la                            #
#                      programmation en Python                         #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                      Source: Gérard Barmarin                         #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#   Ce progamme reprend quelques exemples de programmation en Python   #
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques                       
#-----------------------------------------------------------------------

#import csv                                                             # nécessaire pour sauver les données en csv pour lire le fichier des paramètres
#import time
#import sys
#import os
#import numpy as np                                                     # bibliothèque mathématique
#import numpy.linalg as alg
#import PIL
#from PIL import Image, ImageTk											
#import tkinter as tk                                                   # affichage fenêtre graphique
#import colorsys
#import matplotlib                                                      # bibliothèque d'affichage de courbes
#import matplotlib.pyplot as plt
#import scipy
#from scipy.ndimage import convolve
#from scipy import signal
#import cv2
#import skimage
#import sklearn
#import pandas
#import webcolors

#-----------------------------------------------------------------------
# Encodage des fonctions 
#-----------------------------------------------------------------------

# Pas de fonctions définies

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

# Pas d'initialisation de variables

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# ceci est un commentaire sur une seule ligne                           # en Python les commentaires commencent par # 
                                                                        #ou par --- por les commentaires multilignes
'''
ceci
est
un 
commentaire sur plusieurs lignes
'''

#-----------------------------------------------------------------------

# Entrées / Sorties

'''
Pour afficher à l'écran quelque chose, on utilise print()
les textes à afficher doivent se trouver entre les parenthèses et être 
entre guillemets, les variables sont simplement appelées par leur nom 
pour en afficher la valeur, les différentes choses à afficher sur la 
même ligne sont séparées par des virgules dans la même instruction print
mais on peut utiliser n précédé du caractère d'échappement \n pour forcer
le passage à la ligne. Chaque nouvelle instruction print passe d'office 
à une nouvelle ligne
'''

# En Python, le type des variables ne doit pas être déclaré, 
# elles prennent le type de ce que vous mettez dedans

a = 10						# a devient une variable entière
b = 10.						# b devient une variable flottante
c = "avez compris"			# c est une variable de type string

print("\n---------------------------------------------")
print("Python: les sorties à l'écran")
print("---------------------------------------------")
print("\nSi vous",c,"vous avez",b,"/",a,"!\n")

print("---------------------------------------------\n")

#-----------------------------------------------------------------------

'''
Pour entrer au clavier une valeur ou un texte, on utilise input()
Les caractères entrés au clavier sont stockés d'office dans une variable 
string par défaut même si ce sont des chiffres. A vous de la convertir en
nombre entier ou en flottant si nécessaire avec int() ou float(). 
( str() permet à l'inverse de transformer un chiffre en caractères ). 
Le texte dans la parenthèse du input entre guillemets s'affiche à l'écran 
comme instruction pour l'utilisateur.
'''

print("\n---------------------------------------------")
print("Python: les entrées au clavier")
print("---------------------------------------------\n")

var = input("Entrez une valeur svp:\n")
print(var)												# var est d'office du type string car issue d'un input()
print(type(var))
# var = var + 1 provoquerait une erreur parce que var est de type string
var2 = int(input("Entrez une autre valeur svp:\n"))	# var de type string est immédiatement transformée en int
print(type(var2))
# si la personne introduit autre chose qu'un chiffre la conversion en entier sera impossible et vous aurez une erreur

#-----------------------------------------------------------------------

# Les opérateurs

# Addition  + 
# Soustraction -
# Multiplication *
# Division /
# Exponentiation a**3 pour a puissance 3
# // calcule le quotient d’une division euclidienne: 20//6 = 3
# %  calcule le reste d’une division euclidienne: 20%6 = 2
# Opérateurs de comparaison: > , <= , >= , == (égalité), != (différence)
# Opérateurs logiques: not (négation), and (conjonction) et or (disjonction) (en minuscules!)

# Les opérateurs binaires peuvent être suivis du symbole = pour effectuer 
# simultanément une opération et une affectation. 

# Ainsi a += b équivaut à a = a + b
# Ainsi a += 1 incrémente a de 1 : a = a + 1
# Ainsi a *= b équivaut à a = a * b
# Ainsi a **= b équivaut à a = a**b
# Ainsi a %= b équivaut à a = a % b

#-----------------------------------------------------------------------

# if elif else

# Exemple:

print("\n---------------------------------------------")
print("Exemple d'utilisation de if, elif, else")
print("---------------------------------------------\n")

a = int(input("Entrez un chiffre, je vous dirai s'il est pair ou impaire > ou < que 3:\n"))
if a % 2 == 0:
	print(a,'est pair')
elif a > 3:
	print(a,'est impair et strictement supérieur à 3')
else:
	print(a,'est impair et inférieur ou égal à 3')

print("\n---------------------------------------------\n")

#-----------------------------------------------------------------------

# Les boucles

'''
En Python, la condition d'exécution des instructions d'une boucle se termine par ":"
Les instructions à exécuter dans la boucle sont indentées au même niveau (4 espaces)
La fin de l'indentation correspond à la fin des instructions dans la boucle:

for <element> in <iterable>:
    <instruction1>
    <instruction2>

Exemple:
'''
for elt in [1, 'toto', 2.34]:
	print(elt)
for elt in 'blabla':
	print(elt)


print("\n---------------------------------------------")
print("Python: la boucle for avec range()")
print("---------------------------------------------\n")

m = int(input("Entrez un chiffre: "))
# Le range va de 0 à m-1, on affiche 10 valeurs de 0 à 9
# range(3,10) irait de 3 à 9
# range(5,1) irait de 5 à 2: 5, 4, 3, 2
# range(3,10,2) irait de 3 à 9 par pas de 2 soit 3,5,7,9
# range ne fonctionne qu'avec des entiers positifs ou négatifs
# range(4,-3) irait de 4 à -2 en décroissant: 4, 3, .., 0, -1, -2

for j in range(m):
	print(j)

print("\nDans cette boucle for utilisant \"range\", \non parcourt les valeurs de 0 jusqu'au chiffre entré au clavier - 1")

print("\n---------------------------------------------\n")	

print("\n---------------------------------------------")
print("Python: la boucle while")
print("---------------------------------------------\n")

m =10
# On affiche 9 valeurs de 1 à 9
j = 1
while j <m :
	print(j)
	j = j + 1
print("\nDans cette boucle while initialisée à 1,\non parcourt les valeurs de 1 jusqu'au chiffre entré au clavier - 1")

print("\n---------------------------------------------\n")	

#-----------------------------------------------------------------------

# Création de fonctions

print("\n---------------------------------------------")
print("Python: création et appel d'une fonction")
print("---------------------------------------------\n")

'''
Structure de création et d'appel d'une fonction:

def <nom_fonction>(<paramètres>):   # En-tête de la fonction
    <instruction1>
    <instruction2>                  # Corps de la fonction
    ...
    return <valeur>					# renvoi du résultat au programme principal

Pour appeler la fonction:

var = <nom_fonction>(<paramètres>)  # on récupère le résultat de la fonction dans la variable var

Il peut y avoir plusieurs return dans une fonction mais On « sort » de 
la fonction dès qu’on recontre une instruction return : les instructions 
suivant un return ne sont pas exécutées.
Une fonction peut ne pas contenir d’instruction return ou peut ne renvoyer 
aucune valeur. En fait, si on ne renvoie pas explicitement de valeur, 
Python renverra par défaut la valeur particulière None
'''

# Exemple: la fonction factorielle

def factorielle(valeur):
	a = 1
	for k in range(1, valeur+1):
		a *= k
	return a

while True:
	try:
		valeur = int(input("Entrez un entier pour calculer sa factorielle: "))
		fact = factorielle(valeur)
		print("La factorielle de",valeur,"est",fact)
		break
	except ValueError:
		print("Oops!  Ce n'est pas un chiffre valable. Essayez à nouveau...\n")	

# Exemple de fonction avec plusieurs return: 

def test(n):
	if n % 2 == 0:
		return " est un multiple de 2"
	if n % 3 ==0:
		return " est un multiple de 3"
	return " Bon on arrête,",n,"n'est pas un multiple de 2 ou de 3\n"

x = int(input("\nEntrez un entier pour savoir s'il est multiple de 2 ou de 3: "))
print("\n",x,test(x))

'''
On dit que les variables à l’intérieur d’une fonction sont des variables locales. 
Cela signifie en particulier que des opérations effectuées sur une variable 
d’un certain nom à l’intérieur d’une fonction ne modifient pas une variable 
du même nom à l’extérieur de cette fonction.
On ne peut pas accéder à des variables locales à l’extérieur de la fonction où elles sont définies.
On peut néanmoins modifier une variable globale à l’intérieur d’une fonction : 
on utilise alors le mot-clé global pour définir la variable avant de lui affecter une valeur.
Exemple:

global a
a = 2

Note: évitez d'utiliser des variables globales, elles rendent la maintenance du programme + compliquée
'''

print("\n---------------------------------------------\n")	
print("Respectez les bonnes pratiques en appliquant PEP 8!\nPEP = Python Enhancement Proposal")
print("\n---------------------------------------------\n")
print("https://peps.python.org/pep-0008/")
	
'''
BIBLIOGRAPHIE / WEBOGRAPHIE

https://python.doctor/page-pep-8-bonnes-pratiques-coder-python-apprendre
https://peps.python.org/pep-0008/

'''
#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
