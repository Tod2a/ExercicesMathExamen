import numpy as np

print("\nNous allors représenter les prix des bracelets sous forme d'équations")
print("\nX = turquoises, Y = émeraudes, Z = Diamants et W = Rubis")
print("\néquation 1 = 3x + 2y + 0z + 0w = 900")
print("\néquation 2 = 2x + 0y + 3z + 0w = 1400")
print("\néquation 3 = 1x + 2y + 0z + 2w = 1100")
print("\néquation 4 = 1x + 4y + 2z + 0w = 1500")

coef = np.array([
    [3, 2, 0, 0],
    [2, 0, 3, 0],
    [1, 2, 0, 2],
    [1, 4, 2, 0]
], dtype=float)

t = np.array([900, 1400, 1100, 1500], dtype=float)
     
print("\nVoici donc la matrice des coefficients: ")
print(coef)
print("\nEt voici la matrice des termes indépendants: ")
print(t)

values = np.linalg.solve(coef, t)

print("\nVoici donc la matrice obtenue en résolvant le système d'équation linéraire:")
print(values)
print(f"\nOn peux donc déduire que une turquoise vaut {values[0]}")
print(f"\nQue une émeraude vaut {values[1]}")
print(f"\nQue un diamant vaut {values[2]}")
print(f"\nQue un rubis vaut {values[3]}")

print(f"Le prix du bracelet voulu sera de {4*values[0] + 2*values[1] + values[2] + 2*values[3]}")