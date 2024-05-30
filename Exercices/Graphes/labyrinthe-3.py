#-*- coding: utf8 -*-
########################################################################
'''
  _   __    _   _____  _   _                         _   _
 |  \/  |  /_\ |_   _|| |_| | (_) _  _   ____  _  _ | |_| |_   ___  _ _
 | |\/| | / _ \  | |  |  _  | | || \| | |  _ \| || ||  _| _ \ / _ \| \ |
 |_|  |_|/_/ \_\ |_|  |_| |_| |_||_|\_| |  __/\_, /  \__|_||_|\___/|_\_|
                                        |_|   |__/
'''
########################################################################


#----------------------------------------------------------------------#
#                                                                      #
#             Cours de Mathématiques pour BAC Info chap. 2             #
#                      Opérations sur les graphes                      #
#                            G. Barmarin                               #
#                             2023-2024                                #
#                                                                      #
#----------------------------------------------------------------------#


#----------------------------------------------------------------------#
#                                                                      #
#                           Ex Labyrinthe                              #
#                                                                      #                                                         
#----------------------------------------------------------------------#yplot as plt

#-----------------------------------------------------------------------
# Importation des bibliothèques
#-----------------------------------------------------------------------

import matplotlib.pyplot as plt
import random														   # génération de nombre aléatoires

#-----------------------------------------------------------------------
# encodage des fonctions 
#-----------------------------------------------------------------------

def voisins(p, M, N):
	# renvoie dans s les voisins de tous les sommets admissible de p
    s = [gauche(p), droit(p), bas(p), haut(p)]
    return [v for v in s if admissible(v, M, N)]

def gauche(p):
	#calcule les coordonnées du voisin de gauche
    x, y = p
    return (x - 1, y)

def droit(p):
    x, y = p
    return (x + 1, y)

def bas(p):
    x, y = p
    return (x, y - 1)

def haut(p):
    x, y = p
    return (x, y + 1)

def admissible(v, M, N):
	# vérifie qu'un voisin existe (détection des bords)
    x, y = v
    return x >= 0 and x < M and y >= 0 and y < N

def melanger(s):
	# la fonction mélanger introduit le côté aléatoire pour créér des labyrinthes différents à chaque fois.						
    n = len(s)
    for k in range(n):
       j = random.randint(k, n - 1)
       s[j], s[k] = s[k], s[j]
 

def creer_labyrinthe(p0, M, N):											# crée un labyrinthe de dimension MxN point de départ p0
    visites = set([p0])													# initialisation de la liste des noeuds visités
    s = [p0]															# initialisation de la liste des noeuds découverts?
    print("\nOn part d'un point p0 (ici, le \"milieu\" de la grille):",p0)
    print("et on explore le rectangle à partir de ce point p0 en visitant les voisins de p0 \net en explorant le rectangle à partir de ces voisins de proche en proche.\n")
    print("Chaque fois que l'on rencontre un nouveau sommet lors de l'exploration, \non l'ajoute à visites.")
    print("Liste des visités au départ:",visites)
    print("\nOn crée également une liste s qui contient initialement le sommet p0. Chaque fois que l'on visite un sommet \non l'ajoute à s. \nLa liste s est la liste des sommets à partir desquels une exploration doit être lancée.")
    print("Liste s au départ:",s)
    print("\nOn crée encore un dictionnaire \"peres\". À chaque fois que l'on découvre un voisin v d'un sommet p, \non décrète que p est le père de v ")
    print("\nItérations pour parcourir toutes les cases du rectangles:")
    peres = {}															# initialisation de la liste des pères
    while s != []:
        print("\nListe s:",s)
        #print("On extrait un sommet de la liste s:")
        p = s.pop()														# list.pop(i) Enlève de la liste l'élément situé à la position indiquée et le renvoie en valeur de retour. 
        print("On retire le dernier élément ajouté de la liste s:",p)	# Si aucune position n'est spécifiée, a.pop() enlève et renvoie le dernier élément de la liste
        vs = voisins(p, M, N)											# recherche des voisins de p
        print("On recherche ses voisins:",vs)
        melanger(vs)													# la fonction mélanger introduit le côté aléatoire pour créér des labyrinthes différents à chaque fois.
        print("On mélange les voisins:",vs)
        print("On ajoute les éléments de voisins mélangés qui ne sont pas encore dans la liste visités:",visites)
        for v in vs:
            if v not in visites:
                visites.add(v)
                print("\n")
                print(v,"n'est pas encore dans visites\nOn l'ajoute au début de visites(add):",visites)
                s.append(v)
                print("Et à la fin de s (append):",s)
                peres[v] = p
                print("On ajoute",p," comme peres de:",v,"\nLa liste peres devient:",peres)
            else: print(v,"est déjà dans visites")
    print("\nLa liste s est vide, on s'arrête.\nListe finale des visités :",visites)
    #print("Trajet parcouru (peres):",peres)
    return peres


def plot_labyrinthe(peres, M, N, lab=True):
    d = 0.5
    plt.axis([-1, M, -1, N])
    for x in range(M + 1):
        plt.plot((x - d, x - d), (-d, N - d), 'k')						# dessin des bords verticaux en noir (k=black)
    for y in range(N + 1):
        plt.plot((-d, M - d), (y - d, y - d), 'k')						# dessin des bords horizontaux en noir (k=black)
    for (x, y) in peres:
        (a, b) = peres[(x, y)]
        if lab: plt.plot((x,a), (y,b), 'r')								# Affichage en rouge de l'arbre du labyrinthe
    plt.show()


#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

M = int(input("largeur du Labyrinthe?\n")) 								# largeur du labyrinthe

N = int(input("longueur du Labyrinthe?\n"))								# Longueur du labyrinthe

peres = creer_labyrinthe((M // 2, N // 2), M, N)						# créer le labyrinthe en partant du milieu

print("\nArbre des pères:",peres)
print("\nExemple: (2,1):",peres[(2, 1)]," signifie (2,1) a pour père",peres[(2, 1)]," et ainsi de suite") 
plot_labyrinthe(peres, M, N)											# dessiner le labyrinthe en effacant de la grille les cases qui doivent communiquer
