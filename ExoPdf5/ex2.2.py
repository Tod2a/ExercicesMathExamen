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
#                           Exercice 2.2                               #
#          soustraction par multiple d'un autre ligne                  #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#  création d'une fonction (A,k,i, alpha) qui soustrait un muliple     #
#            (alpha) de la ligne i à la ligne k                        #         
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
def substract_linesByAlpha(A, k, i, alpha):
    for j in range(len(A[k-1])):
        value = A[i-1][j]*alpha
        A[k-1][j] = A[k-1][j]-value

def print_matrice(A):
    for row in A:
        print(row)

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

matrice = [
    [2, 2, 3],
    [2, 5, 6],
    [1, 8, 9]
]
ligne1 = 2
ligne2 = 3
multiply = 2

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

print("\nAvant la soustraction:")
print_matrice(matrice)

substract_linesByAlpha(matrice, ligne1, ligne2, multiply)

print("\nAprès la soustraction:")
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
