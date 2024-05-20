# En Python, créer un programme qui exécute le produit de deux matrices. Les matrices sont entrées au clavier élément par 
# élément. Leur compatibilité est vérifiée avant d’introduire tous les éléments. Les matrices de départ et le produit sont 
# affichés à l’écran.
# Copin Thomas

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


def MultiplyGrid():
    firstRows = int(input("Combien de lignes fait la premiere matrice ?"))
    firstCols = int(input("Combien de colonnes fait la premire matrice ?"))
    secondRows = int(input("Combien de lignes fait la deuxieme matrice ?"))
    secondCols = int(input("Combien de colonnes fait la deuxieme matrice ?"))

    if firstCols == secondRows:
        print("#########################################")
        print("Multiplication validée")
        print("#########################################")
        print("Remplissez la première matrice")
        firstGrid = CreateGrid(firstRows, firstCols)
        print("#########################################")
        print("Remplissez la seconde matrice")
        secondGrid = CreateGrid(secondRows, secondCols)
        finalGrid = BuildGridMultiplied(firstGrid, secondGrid)
        print("#########################################")
        print("#########################################")
        print("#########################################")
        print("première matrice:")
        PrintGrid(firstGrid)
        print("#########################################")
        print("seconde matrice")
        PrintGrid(secondGrid)
        print("#########################################")
        print("Produit des deux:")
        PrintGrid(finalGrid)
        print("#########################################")
    else:
        print("Multiplication impossible, le nombre de colonnes de la premiere matrice doit être égal au nombre de ligne de la deuxieme")


MultiplyGrid()