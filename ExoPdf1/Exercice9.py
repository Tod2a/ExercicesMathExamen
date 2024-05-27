# En Python, créer un programme qui calcule et affiche la nème puissance d’une matrice carrée aléatoire de manière 
# « économique 
# Copin Thomas
import random
import keyboard     

def mat_mult(A, B):

    #Multiplie deux matrices carrées A et B.

    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(size))
    return result

def mat_identity(size):

    #Crée une matrice identité de taille donnée.
  
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def matrix_power(matrix, power):
    #Calcule la x-ème puissance d'une matrice carrée en utilisant l'exponentiation rapide.
    size = len(matrix)
    result = mat_identity(size)
    base = matrix

    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        power //= 2

    return result

def random_matrix(size):
    
    #Génère une matrice carrée aléatoire de taille donnée avec des valeurs entre 0 et 1.
    
    return [[random.random() for _ in range(size)] for _ in range(size)]

def print_matrix(matrix):
    
    #Affiche une matrice de manière lisible.
    
    for i in range(len(matrix)):
        print(matrix[i]) 

def random_matrix_power(n, x):
    #Génère une matrice carrée aléatoire de taille n et calcule sa x-ème puissance.
    matrix = random_matrix(n)
    print("Matrice originale:")
    print_matrix(matrix)

    matrix_x_power = matrix_power(matrix, x)

    print(f"\nMatrice à la puissance {x}:")
    print_matrix(matrix_x_power)


n = 4  
x = 3  
random_matrix_power(n, x)

print("\nPoussez sur la touche q pour fermer cette fenêtre")

while True:
    if keyboard.is_pressed('q'):
        break