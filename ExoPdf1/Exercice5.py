# En Python, créer un programme qui exécute le produit d’une matrice aléatoire par un scalaire entré au clavier. La 
# matrice de départ, le scalaire et le produit sont affichés à l’écran.
# Copin Thomas
import random

def GenerateGridInt(lin, coln):
    grid = []
    for i in range(lin):
        row = []
        for i in range(coln):
            row.append(random.randint(-9, 9))
        grid.append(row)
    return grid

def MultiplyGrid(grid, value):
    newgrid = []
    for i in range (len(grid)):
        row = []
        for j in range (len(grid[i])):
            row.append(value * grid[i][j])
        newgrid.append(row)
    return newgrid

def PrintGrid(grid):
    for i in range(len(grid)):
        print(grid[i])  



MyGrid = GenerateGridInt(5 , 5)

print("##############")
print("Matrice aléatoire:")
PrintGrid(MyGrid)
print("##############")

ValueToMultiply = int(input("Par combien voulez vous multiplier"))
MultipliedGrid = MultiplyGrid(MyGrid, ValueToMultiply)

print("##############")
print("Matrice multipliée par le chiffre " +  str(ValueToMultiply) + ":")
PrintGrid(MultipliedGrid)
print("##############")