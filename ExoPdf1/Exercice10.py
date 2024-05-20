# En Python, créer un programme qui exécute le produit de Hadamard de deux matrices. Les matrices sont entrées au clavier 
# élément par élément. Leur compatibilité est vérifiée avant d’introduire tous les éléments. Les matrices de départ et le 
# produit sont affichés à l’écran.
# Copin Thomas

import random

def PrintGrid(grid):
    for i in range(len(grid)):
        print(grid[i])  

def CreateGrid(rows, cols):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input("donnez une valeur à rentrer dans la matrice")))
        grid.append(row)
    return grid

def BuildGridHadamard(grid1, grid2):
    grid = []
    for i in range(len(grid1)):
        row = []
        for j in range(len(grid2[i])):
            row.append(grid1[i][j] * grid2[i][j])
        grid . append(row)
    return grid

def HadamardGrid():
    firstRows = int(input("Combien de lignes fait la premiere matrice ?"))
    firstCols = int(input("Combien de colonnes fait la premire matrice ?"))
    secondRows = int(input("Combien de lignes fait la deuxieme matrice ?"))
    secondCols = int(input("Combien de colonnes fait la deuxieme matrice ?"))

    if firstCols == secondCols and firstRows == secondRows:
        print("#########################################")
        print("Produit de Hadamard validé")
        print("#########################################")
        print("Remplissez la première matrice")
        firstGrid = CreateGrid(firstRows, firstCols)
        print("#########################################")
        print("Remplissez la seconde matrice")
        secondGrid = CreateGrid(secondRows, secondCols)
        finalGrid = BuildGridHadamard(firstGrid, secondGrid)
        print("#########################################")
        print("#########################################")
        print("#########################################")
        print("première matrice:")
        PrintGrid(firstGrid)
        print("#########################################")
        print("seconde matrice")
        PrintGrid(secondGrid)
        print("#########################################")
        print("Produit de Hadamard des deux:")
        PrintGrid(finalGrid)
        print("#########################################")
    else:
        print("Produit de hadamard impossible, les matrices doivent être identiques")


HadamardGrid()