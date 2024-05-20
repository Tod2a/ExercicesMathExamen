# En Python, créer un programme qui crée une matrice aléatoire, qui calcule ensuite son opposée, affiche les deux 
# matrices et qui vérifie que leur somme fait bien … (à compléter par vous-même
# Copin Thomas
import random

def GenerateOpositeGrid(grid):
    newgrid = []
    for i in range (len(grid)):
        row = []
        for j in range (len(grid[i])):
            row.append(-1 * grid[i][j])
        newgrid.append(row)
    return newgrid

def GenerateGridInt(lin, coln):
    grid = []
    for i in range(lin):
        row = []
        for i in range(coln):
            row.append(random.randint(-9, 9))
        grid.append(row)
    return grid

def AddGrid (grid1, grid2):
    grid = []
    for i in range (len(grid1)):
        row = []
        for j in range (len(grid1[i])):
            row.append(grid1[i][j] + grid2[i][j])
        grid.append(row)
    return grid


def PrintGrid(grid):
    for i in range(len(grid)):
        print(grid[i])  


MyGrid = GenerateGridInt(5 , 5)
MyOppositeGrid = GenerateOpositeGrid(MyGrid)
AddedGrid = AddGrid(MyGrid, MyOppositeGrid)

print("##############")
print("Matrice aléatoire:")
PrintGrid(MyGrid)
print("##############")

print("##############")
print("Son opposée:")
PrintGrid(MyOppositeGrid)
print("##############")

print("##############")
print("La matrice qui résulte de sa somme:")
PrintGrid(AddedGrid)
print("Il s'agit donc bien d'une matrice nulle")
print("##############")