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
#                           Exercice 2.4                               #
#            Calcul de l'inverse par la méthode du pivot de            #                                                          
#                           Gauss-Jordan                               #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#             Ce programme calcule l'inverse d'une matrice             #
#               à l'aide d'une fonction qui retournera l'inverse       #         
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques                       
#-----------------------------------------------------------------------

import time
import numpy as np
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
    A[[i, j]] = A[[j, i]]

def inverse(A):
    A = np.array(A, dtype=float)  
    n = A.shape[0]
    
    I = np.eye(n)
    augmented_matrix = np.hstack((A, I))

    
    for j in range(n):
        # Rechercher le pivot
        max_row_index = np.argmax(np.abs(augmented_matrix[:, j])) 

        if max_row_index != j:
            switch_lines(augmented_matrix, max_row_index, j)

        augmented_matrix[j] = augmented_matrix[j] / augmented_matrix[j, j]    

        for i in range(n):
            if i != j:
                augmented_matrix[i] = augmented_matrix[i] - augmented_matrix[j]*augmented_matrix[i,j]


    # Extraire l'inverse de la matrice augmentée
    inverse_matrix = augmented_matrix[:, n:]
    inverse_matrix_rounded = np.round(inverse_matrix, decimals=2)
    return inverse_matrix_rounded.tolist()

#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------

matrice = [
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1]
]

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\n---------------------------------------------\n")
print("\nCalcul de l'inverse d'une matrice\n")
print("\n---------------------------------------------\n")

start = time.time()

print("\n Matrice de base: ")
print_matrice(matrice)

print("\n inverse de cette matrice:")
inv = inverse(matrice)
print_matrice(inv)



end = time.time()

print("\n---------------------------------------------\n")

print("\nvous avez calculé l'inverse de la matrice, l'opération vous a prit: ", end-start, " secondes")

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
