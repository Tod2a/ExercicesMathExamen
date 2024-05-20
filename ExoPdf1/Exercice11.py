# En Python, créer un programme qui calcule et affiche la transposée d’une matrice aléatoire. La matrice de départ et sa 
# transposée sont affichées à l’écran.
#Copin Thomas
import random

def PrintGrid(grid):
    for i in range(len(grid)):
        print(grid[i])  

def GenerateGridInt(lin, coln):
    grid = []
    for i in range(lin):
        row = []
        for i in range(coln):
            row.append(random.randint(-9, 9))
        grid.append(row)
    return grid

def TransposeGrid(grid):
    newgrid = []
    for j in range(len(grid[0])):
        row = []
        for i in range(len(grid)):
            row.append(grid[i][j])
        newgrid.append(row)
    return newgrid

MyGrid = GenerateGridInt(3, 5)
MyGridTransposed = TransposeGrid(MyGrid)


print("#########################################")
print("Voici la matrice générée:")
PrintGrid(MyGrid)
print("#########################################")

print("#########################################")
print("Voici la matrice transposée")
PrintGrid(MyGridTransposed)
print("#########################################")

