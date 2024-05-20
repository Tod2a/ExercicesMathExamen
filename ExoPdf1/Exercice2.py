# En Python, créer un programme qui génère 
# une matrice unité, 
# une matrice diagonale, 
# une matrice triangulaire, 
# une matrice creuse, 
# une matrice nulle. La taille de la matrice est entrée au clavier
# Copin Thomas
import random

def GenerateGridZero(lin, coln):
    grid = []
    for i in range(lin):
        row = [0] * coln
        grid.append(row)
    return grid

def GenerateGridUnit(lin, coln):
    grid = GenerateGridZero(lin, coln)

    for i in range(min(lin, coln)):
        grid[i][i] = 1

    return grid

def GenerateGridDiagonal(lin, coln):
    grid = GenerateGridZero(lin, coln)
    if lin < coln:
        for i in range(lin):
            grid[i][i] = random.randint(-9,9)
    else:
        for i in range(coln):
            grid[i][i] = random.randint(-9,9)
    return grid


def GenerateGridTriangular(lin, coln):
    grid = []
    for i in range(lin):
        row = []
        for j in range(coln):
            if j >= i:
                row.append(random.randint(-9, 9))
            else:
                row.append(0)
        grid.append(row)
    return grid


def GenerateGridHollow(lin, coln):
    grid = []
    for i in range(lin):
        row = []
        for i in range(coln):
            row.append(random.randint(0,1))
        grid.append(row)
    return grid


def PrintGrid(grid):
    for i in range(len(grid)):
        print(grid[i])  




inpRows = int(input('Combien de lignes?'))
inpCol = int(input('Combien de Colonnes?'))

print("")
print("Matrice Unité:")
gridunit = GenerateGridUnit(inpRows, inpCol)
PrintGrid(gridunit)

print("")
print("Matrice diagonale:")
gridDiagonal = GenerateGridDiagonal(inpRows, inpCol)
PrintGrid(gridDiagonal)

print("")
print("Matrice triangulaire(supérieure)")
gridTriangular = GenerateGridTriangular(inpRows, inpCol)
PrintGrid(gridTriangular)

print("")
print("Matrice creuse:")
gridHollow = GenerateGridHollow(inpRows, inpCol)
PrintGrid(gridHollow)

print("")
print("Matrice nulle:")
gridzero = GenerateGridZero(inpRows, inpCol)
PrintGrid(gridzero)