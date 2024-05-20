# En Python, créer un programme qui calcule et affiche la somme des colonnes d’une matrice aléatoire de deux manières 
# différentes. 
# Copin Thomas
import random

def PrintGrid(grid):
    for i in range(len(grid)):
        print(grid[i])  

def GenerateGridOne(lin, coln):
    grid = []
    for i in range(lin):
        row = [1] * coln
        grid.append(row)
    return grid

def GenerateGridInt(lin, coln):
    grid = []
    for i in range(lin):
        row = []
        for i in range(coln):
            row.append(random.randint(-9, 9))
        grid.append(row)
    return grid

def AddEachCols(grid):
    newgrid = []
    row = []
    for j in range(len(grid[0])):
        count = 0
        for i in range(len(grid)):
            count += grid[i][j]
        row.append(count)
    newgrid.append(row)
    return newgrid

def BuildGridMultiplied(grid1, grid2):
    grid = []
    for i in range(len(grid1)):
        row = []
        for j in range(len(grid2[i])):
            value = 0
            for k in range(len(grid2)):
                value += grid1[i][k] * grid2[k][j]
            row.append(value)
        grid . append(row)
    return grid

MyGrid = GenerateGridInt(5, 5)
MyVector = GenerateGridOne(1, 5)
AddedGrid = AddEachCols(MyGrid)
MultipliedGrid = BuildGridMultiplied(MyVector, MyGrid)

print("#########################################")
print("Voici la matrice générée:")
PrintGrid(MyGrid)
print("#########################################")

print("#########################################")
print("Premiere méthode(addition simple):")
PrintGrid(AddedGrid)
print("#########################################")

print("#########################################")
print("dieuxme methode(multiplication par mutiplication avec un vecteur unité)")
PrintGrid(MultipliedGrid)
print("#########################################")