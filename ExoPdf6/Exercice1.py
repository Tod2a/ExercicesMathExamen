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
#                           Exercice 1                                 #
#                      Fonction de convolution                         #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                       Source: Thomas Copin                           #                 
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                        Que fait ce programme?                        #           
#----------------------------------------------------------------------#
#                                                                      #
#       Crée une fonction qui fait la convolution entre une matrice    #
#                           et un masque                               #  
#                                                                      #
#----------------------------------------------------------------------#


#-----------------------------------------------------------------------
# Importation des bibliothèques                       
#-----------------------------------------------------------------------

import numpy as np 


#-----------------------------------------------------------------------
# Encodage des fonctions 
#-----------------------------------------------------------------------

def rotate_mask_180(mask):
    # Créer une nouvelle matrice pour le masque retourné
    rotated_mask = [[0 for _ in range(len(mask[0]))] for _ in range(len(mask))]
    rows = len(mask)
    cols = len(mask[0])
    
    for i in range(rows):
        for j in range(cols):
            rotated_mask[i][j] = mask[rows - 1 - i][cols - 1 - j]
    
    return rotated_mask


def convolution(noyau, lin, col, image):
    valeur = 0
    for i in range(3):
        for j in range(3):
            valeur += noyau[i, j] * image[lin - 1 + i, col - 1 + j]
    return valeur


def convolve(matrix, mask):
    matrix = np.array(matrix)
    mask = np.array(mask)
    length, width = matrix.shape

    # Retourner le masque (rotation de 180 degrés)
    mask = rotate_mask_180(mask)
    #mask = np.flipud(np.fliplr(mask))

    # Ajouter des bordures de zéros à l'image
    padded_matrix = np.pad(matrix, pad_width=1, mode='constant')

    output = np.zeros((length, width))

    # Appliquer la convolution
    for ligne in range(1, length + 1):
        for col in range(1, width + 1):
            output[ligne - 1, col - 1] = convolution(mask, ligne, col, padded_matrix)
    
    return output
    


#-----------------------------------------------------------------------
# Définition / initialisation des variables               
#-----------------------------------------------------------------------



#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# encodage du programme principal
#
#-----------------------------------------------------------------------





#-----------------------------------------------------------------------
#
#                               Fin
#
#-----------------------------------------------------------------------
