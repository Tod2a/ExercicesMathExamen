# En Python, créer un programme qui calcule et affiche la nème puissance d’une matrice carrée aléatoire de manière 
# « économique 
# Copin Thomas
import random

def PrintGrid(grid):
    for i in range(len(grid)):
        print(grid[i])  

def GenerateSquareGridInt(size):
    grid = []
    for i in range(size):
        row = []
        for i in range(size):
            row.append(random.randint(-9, 9))
        grid.append(row)
    return grid
