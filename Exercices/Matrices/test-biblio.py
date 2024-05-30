#!/usr/bin/env python
#-*- coding: latin1 -*-

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
#                             2023-2024                                #                      
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                                                                      #
#           Test de la présence des bibliothèques nécessaires          #
#                    pour la programmation en Python                   #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                      Source: Gérard Barmarin                         #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#   Ce progamme teste la présence des bibliothèques dont vous aurez    #
#   besoin pour faire les exercices du cours et indique les versions   #
#   installées ainsi que la version de Python utilisée                 #
#   Exécutez ce programme pour voir quelles bibliothèque manquent.     #
#   Chargez-les avec sudo apt install python3-nom-de-la-bib (Linux)    #
#   ou avec pip install                                                #
#   Relancez ensuite le programme pour vérifier que c'est bien chargé! #
#                                                                      #                                                                      #
#----------------------------------------------------------------------#

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Modules normalement inclus dans l'installation de base de Python qu'il
# ne faudra généralement pas charger
#-----------------------------------------------------------------------

print("--------------------------------------------------\n")
print("Bibliothèques et modules nécessaires installés")
print("\n--------------------------------------------------\n")
# module de gestion du temps
try:
	import time
	print("Le module time est installé")
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE time...\n")

# module permettant l'utilisation de commades de la console via Python
try:
	import sys
	print("Le module sys est installé")
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE sys...\n")

# module permettant la gestion des fichiers et de leur arborescence
try:
	import os
	print("Le module os est installé")
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE os...\n")

# Bibliothèque de traitement/conversion des espaces de Couleurs
try:
	import colorsys
	print("Le module colorsys est installé")
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE colorsys...\n")
	
# Tool Kit Interface
try:
	import tkinter
	print("Le module tkinter est installé")
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE tkinter...\n")


#-----------------------------------------------------------------------					
# Module à installer
#-----------------------------------------------------------------------


# Biliothèque de calcul Numérique en Python
try:
	import numpy
	print("version de numpy:		",numpy.__version__)
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE numpy...\n")

# Python Image Library
try:
	import PIL
	print("version de PIL: 		",PIL.__version__)
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE pillow (PIL)...\n")
		
# Module de manipulation des fichiers au format Coma Separated 
try:
	import csv		
	print("version de csv: 		",csv.__version__)
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE csv...\n")

# Bibliothèque de calcul Scientifique en Python
try:
	import scipy
	print("version de scipy: 		",scipy.__version__)
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE scipy...\n")
	
# Mathematics plotting Library					
try:
	import matplotlib					
	print("version de matplotlib: 		",matplotlib.__version__)
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE matplotlib...\n")

# Module de matplotlib equivalent à Matlab
try:
	import matplotlib.pyplot as plt	
	print("Le module pyplot de matplotlib est installé")	
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE matplotlib.pyplot...\n")
	
# Module de gestion des images de la Mathematics plotting Library
try:
	import matplotlib.image as mpimg
	print("Le module image de matplotlib est installé")	
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE matplotlib.image...\n")
	
# (Open) Computer Vision
try:
	import cv2							
	print("version de OpenCV: 		",cv2.__version__)
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE OpenCV (cv2)...\n")

#-----------------------------------------------------------------------					
# Modules optionnels
#-----------------------------------------------------------------------

# module skimage	
try:
	import skimage
	print("version de skimage: 		",skimage.__version__)
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE skimage...\n")

# module sklearn
try:
	import sklearn
	print("version de sklearn: 		",sklearn.__version__)
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE sklearn...\n")

# module de Gestion des Couleurs reconnues pour le Web
try:
	import webcolors
	print("version de webcolors: 		",webcolors.__version__)
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE webcolors...\n")
	
# module pandas
try:
	import pandas
	print("version de pandas: 		",pandas.__version__)
except ModuleNotFoundError:
	print("\nIL MANQUE LA LIBRAIRIE pandas...\n")
			
#-----------------------------------------------------------------------
# Modules propres au Raspberry pi
#-----------------------------------------------------------------------

# Gestion de la Camera sur Raspberry Pi

#import picamera					


#----------------------------------------------------------------------#
#                         Version de Python                            #
#----------------------------------------------------------------------#

print("\n--------------------------------------------------")
print("Version de Python : \n")
os.system("python --version")
print("--------------------------------------------------\n")
print ("Fin du programme de test\n")

#-----------------------------------------------------------------------

