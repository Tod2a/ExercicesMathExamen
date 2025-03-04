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
#                           Exercice 2.1                               #
#                         Inversion lignes                             #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#  création d'une fonction (A,i,j) qui inverse les deux lignes i,j     #
#                       dans la matrice A                              #         
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques                       
#-----------------------------------------------------------------------

import time
import keyboard                 #attention il faut installer la bibliothèque avec pip


#-----------------------------------------------------------------------
# Encodage des fonctions 
#-----------------------------------------------------------------------

#ajustement des valeurs i et j afin que l'utilisateur puisse introduire la ligne 3 
#il ne devra pas prendre en compte que informatiquement, l'index des tableau commence à 0
def switch_lines(A, i, j):
    temp = A[i-1]
    A[i-1] = A[j-1]
    A[j-1] = temp

def print_matrice(A):
    for row in A:
        print(row)

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
ligne1 = 2
ligne2 = 3

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\n---------------------------------------------\n")
print("\nInversion de deux lignes au sein d'une matrice\n")
print("\n---------------------------------------------\n")

start = time.time()

print("\nAvant l'inversion:")
print_matrice(matrice)

switch_lines(matrice, 2, 3)

print("\nAprès l'inversion:")
print_matrice(matrice)
end = time.time()

print("\n---------------------------------------------\n")

print("\nvous avez inversé lles lignes", ligne1 , " et ", ligne2 ,", l'opération vous a prit: ", end-start, " secondes")

print("\nPoussez sur la touche q pour fermer cette fenêtre")

print("\n---------------------------------------------\n")

while True:
    if keyboard.is_pressed('q'):
        break





#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
