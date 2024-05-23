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
#                           Exercice 2.3                               #
#          Calcul du déterminant par la méthode du pivot de            #                                                          
#                           Gauss-Jordan                               #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#             Ce programme calcule le déterminant d'une matrice        #
#               à l'aide d'une fonction qui retournera le détermiannt  #         
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

def switch_lines(A, i, j):
    temp = A[i-1]
    A[i-1] = A[j-1]
    A[j-1] = temp

def determinant(A):
    n = len(A)
    det = 1

    for i in range(n):
        #recher le pivot
        if A[i][i] == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    switch_lines(A, i+1, k+1)
                    det *= -1
                    break

        if A[i][i] == 0:
            return 0
        
        for k in range(i+1, n):
            factor = A[k][i] / A[i][i]
            substract_linesByAlpha(A, k+1, i+1, factor)

    for i in range(n):
        det *= A[i][i]

    return det

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

matrice = [
    [-2, 2, -3],
    [-1, 1, 3],
    [2, 0, -1]
]

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\n---------------------------------------------\n")
print("\nCalcul du déterminan d'une matrice\n")
print("\n---------------------------------------------\n")

start = time.time()


print(determinant(matrice))



end = time.time()

print("\n---------------------------------------------\n")

print("\nvous avez calculé le déterminant de la matrice, l'opération vous a prit: ", end-start, " secondes")

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
