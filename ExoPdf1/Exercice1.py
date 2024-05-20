# Réaliser un programme qui génère une matrice aléatoire dont les éléments sont des entiers 
# La taille doit être entrée au clavier et le résultat affiché à l'écran
# Copin Thomas
import random

def GenerateGridInt(lin, coln):
    grid = []
    for i in range(lin):
        row = []
        for i in range(coln):
            row.append(random.randint(-9, 9))
        grid.append(row)
    for i in range(len(grid)):
        print(grid[i])
    return grid

def GenerateGridReal(lin, coln):
    grid = []
    for i in range(lin):
        row = []
        for i in range(coln):
            row.append(random.randint(0, 9))
        grid.append(row)
    for i in range(len(grid)):
        print(grid[i])
    return grid


inpRows = int(input('Combien de lignes'))
inpCol = int(input('Combien de colonnes'))
grid = GenerateGridInt(inpRows,inpCol)
grid = GenerateGridReal(inpRows,inpCol)