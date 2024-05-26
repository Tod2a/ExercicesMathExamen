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
#                           Exercice 2.6                               #
#                     Résolution du prix des pizzas                    #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#             Ce programme utilise les fonction de l'ex2.5             #
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
print("\nTrouvez le prix des pizzas\n")
print("\n---------------------------------------------\n")

start = time.time()

print("\n nous allons trouvez le prix des pizzas en mettant chaque tiquet de caisse sous forme d'équation")
print("\n nous allons définir que chaque variable sera une sorte de pizza comme ceci: ")
print("\n x est la pizza végétarienne")
print("\n y est la pizza Hawai")
print("\n z est la pizza quatre-saisons")
print("\n w est la pizza margherita")
print("\n v est la pizza napolitaine")
print("\n les équations vont donc se présenter comme ceci: x + y + z + w + v = t")
print("\n nous pouvons donc représenter les tickets de caisse comme ceci: ")
print("\nticket 1 : 1x + 0y + 2z + 1w + 0v = 55")
print("\nticket 2 : 1x + 1y + 1z + 2w + 0v = 65.5")
print("\nticket 3 : 2x + 2y + 0z + 1w + 1v = 80")
print("\nticket 4 : 1x + 1y + 2z + 2w + 3v = 117.5")
print("\nticket 5 : 0x + 2y + 0z + 1w + 2v = 63.5")

coef = np.array([
    [1, 0, 2, 1, 0],
    [1, 1, 1, 2, 0],
    [2, 2, 0, 1, 1],
    [1, 1, 2, 2, 3],
    [0, 2, 0, 1, 2]
], dtype=float)

t = np.array([55, 65.5, 80, 117.5, 63.5], dtype=float)
     
print("\nVoici donc la matrice des coefficients: ")
print(coef)
print("\nEt voici la matrice des termes indépendants: ")
print(t)

values = np.linalg.solve(coef, t)

print("\nVoici donc la matrice obtenue en résolvant le système d'équation linéraire:")
print(values)
print(f"\nOn peux donc déduire que la pizza végétatienne vaut {values[0]}")
print(f"\nQue la pizza Hawai vaut {values[1]}")
print(f"\nQue la pizza Quatre-saison vaut {values[2]}")
print(f"\nQue la pizza Margherita vaut {values[3]}")
print(f"\nQue la pizza napolitaine vaut {values[4]}")

end = time.time()

print("\n---------------------------------------------\n")

print("\nvous avez trouvé le prix des pizzas, l'opération vous a pris: ", end-start, " secondes")

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
