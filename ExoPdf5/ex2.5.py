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
#                           Exercice 2.5                               #
#                   Résolution d'un système d'équation                 #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#             Ce programme utilise les fonction de l'ex2.4             #
#            pour résudre un système d'équation à l'aide de matrices   #         
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

def CreateMatrix(rows, cols):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                value = input(f"Introduisez la valeur numéro {j+1} de l'équation numéro {i+1}? ")
                if value == '':
                    print("\nAttention, vous avez introduit une valeur nulle!")
                else:
                    try:
                        value_int = int(value)
                        row.append(value_int)
                        break
                    except ValueError:
                        print("\nAttention, vous devez entrer un nombre entier.")
        grid.append(row)
    return grid

#réutilisation d'une fonction des exercices du Pdf1

def BuildGridMultiplied(grid1, grid2):
    grid = []
    for i in range(len(grid1)):
        row = []
        for j in range(len(grid2[0])):
            value = 0
            for k in range(len(grid2)):
                value += grid1[i][k] * grid2[k][j]
            row.append(value)
        grid.append(row)
    return grid

#réutilisation des fonctions de l'exercice 2.4 
def substract_linesByAlpha(A, k, i, alpha):
    for j in range(len(A[k])):
        value = A[i][j]*alpha
        A[k][j] = A[k][j]-value

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
    return inverse_matrix.tolist()

def solve(A, T):
    #Utilisation de la fonction de numpy pour éviter les problèmes d'arrondis avec la fonction de base
    inv_A = np.linalg.inv(A)
    X = BuildGridMultiplied(inv_A, T)
    return X
#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------


# Encodez votre programme ici!
print("\n---------------------------------------------\n")
print("\nRésolution d'un système d'équiation à l'aide des matrices\n")
print("\n---------------------------------------------\n")

while True:
    print("\nveuillez d'abord définir vos équations.")
    col = int(input("\nCombien d'équations contient votre système?"))
    lin = int(input("\nCombien de variables contiennent vos équations?"))
    if col != lin:
        print("\nIl faut que le nombre de variables soit égal au nombre d'équations, sinon la résolution du système n'est pas possible car la matrice ne sera pas carrée")
    else:
        break

print("\n veuillez entrer les valeurs des coefficients")
coef = CreateMatrix(lin, col)

print("\nVeuillez introduire les valeurs des termes indépendants de vos équations:")
t = CreateMatrix(lin, 1)

print("\nVoici donc les Coefficients et les termes indépendants de vos équations:")
print_matrice(coef)
print_matrice(t)

print("\nVoici les valeurs des variables de votre système, les valeurs se lisent de haut en bas")

start = time.time()

x = solve(coef, t)

end = time.time()

print_matrice(x)

print("\nVérification avec Numpy:")

a = np.array(coef)
b = np.array(t)

x = np.linalg.solve(a, b)

print_matrice(x)        

print("\n---------------------------------------------\n")

print("\nvous avez résolu votre système d'équation, l'opération vous a pris: ", end-start, " secondes")

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
