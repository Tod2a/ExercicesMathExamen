# En Python, créer un programme qui additionne/soustrait deux matrices après avoir vérifié que l’addition est possible. 
# Les matrices sont entrées au clavier élément par élément
# Copin Thomas

def CreateGrid():
    grid = []
    rows = int(input("Combien de lignes"))
    cols = int(input("Combien de colonnes"))
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input("donnez une valeur à rentrer dans la matrice")))
        grid.append(row)
    return grid

#add doit être considéré comme un bool, à 1 cela additionne et à 0 cela soustrait
def AddOrSoustractMatrix(grid1, grid2, add):
    if (len(grid1) == len(grid2) and len(grid1[0]) == len(grid2[0])):
        grid = []
        if add:
            for i in range (len(grid1)):
                row = []
                for j in range (len(grid1[i])):
                    row.append(grid1[i][j] + grid2[i][j])
                grid.append(row)
            return grid
        else:
            for i in range (len(grid1)):
                row = []
                for j in range (len(grid1[i])):
                    row.append(grid1[i][j] - grid2[i][j])
                grid.append(row)
            return grid
    else:
        print("Addition/soustraction impossible!")

def PrintGrid(grid):
    for i in range(len(grid)):
        print(grid[i])  


firstGrid = CreateGrid()
secondGrid = CreateGrid()

print("#################")
print("Premiere matrice:")
PrintGrid(firstGrid)
print("#################")

print("#################")
print("Seconde matrice")
PrintGrid(secondGrid)
print("#################")

print("#################")
print("Addition des deux:")
AddedGrid = AddOrSoustractMatrix(firstGrid, secondGrid, 1)
PrintGrid(AddedGrid)
print("#################")

print("#################")
print("Soustraction des deux:")
Sousgrid = AddOrSoustractMatrix(firstGrid, secondGrid, 0)
PrintGrid(Sousgrid)
print("#################")