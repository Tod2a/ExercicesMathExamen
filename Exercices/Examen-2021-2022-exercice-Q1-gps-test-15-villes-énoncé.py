##!/usr/bin/python
#-*- coding: utf8 -*-

#----------------------------------------------------------------------#
#                                                                      #
#                Cours de Mathématiques pour BAC Info                  #
#                          Examen 2021-2022                            #
#                            G. Barmarin                               #
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                                                                      #
#                  Exercice Mini GPS avec 15 villes                    #
#                                                                      #                                                         
#----------------------------------------------------------------------#

#-----------------------------------------------------------------------
# Importation des bibliothèques
#-----------------------------------------------------------------------


import numpy as np                                                     # bibliothèque mathématique


#-----------------------------------------------------------------------
# encodage des fonctions 
#-----------------------------------------------------------------------






	
#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

print ("\nCe programme fonctionne comme un mini-GPS: \nil calcule le chemin le plus court entre deux villes, \nsa longueur et les villes par où on doit passer")

Inf = np.inf 															# fonction infini en python numpy

Z = np.array([
"Paris",	"Lyon",	"Nice",	"Nantes",	"Strasbourg",	"Montpellier",	"Lille",	"Rennes",	"Reims",	"Saint-Étienne",	"Angers",	"Grenoble",	"Nîmes",	"Aix-en-Provence",	"Brest"
])

P = np.array ( [ 
[ 0	, Inf, Inf,	Inf, Inf, Inf, 204,	309, 130, Inf, 265,	Inf, Inf, Inf, Inf ],
[ Inf,	0,	299,	Inf,	384,	250,	Inf,	Inf,	394,	49,	Inf,	95,	217,	253,	Inf ],
[ Inf,	299,	0,	Inf,	Inf,	273,	Inf,	Inf,	Inf,	299,	Inf,	205,	234,	148,	Inf ],
[ Inf,	Inf,	Inf,	0,	Inf,	Inf,	Inf,	100,	Inf,Inf,	81,	Inf,	Inf,	Inf,	255 ],
[ Inf,	384,	Inf,	Inf,	0,	Inf,	Inf,	Inf,	282,	Inf,	Inf,	Inf,	Inf,	Inf,	Inf ],
[ Inf,	250,	273,	Inf,	Inf,	0,	Inf,	Inf,	Inf,	207,	Inf,	228,	46,	127,	Inf ],
[ 204,	Inf,	Inf,	Inf,	Inf,	Inf,	0,	Inf,	167,	Inf,	Inf,	Inf,	Inf,	Inf,	Inf ],
[ 309,	Inf,	Inf,	100,	Inf,	Inf,	Inf,	0,	Inf,	Inf,	110,	Inf,	Inf,	Inf,	210 ],
[ 130,	394,	Inf,	Inf,	282,	Inf,	167,	Inf,	0,	Inf,	392,	471,	Inf,	Inf,	Inf ],
[ Inf,	49,	299,	Inf,	Inf,	207,	Inf,	Inf,	Inf,	0,	Inf,	109,	178,	229,	Inf ],
[ 265,	Inf,	Inf,	81,	Inf,	Inf,	Inf,	110,	392,	Inf,	0,	Inf,	Inf,	Inf,	310 ],
[ Inf,	95,	205,	Inf,	Inf,	228,	Inf,	Inf,	471,	109,	Inf,	0,	185,	185,	Inf ],
[ Inf,	217,	234,	Inf,	Inf,	46,	Inf,	Inf,	Inf,	178,	Inf,	185,	0,	94,	Inf ],
[ Inf,	253,	148,	Inf,	Inf,	127,	Inf,	Inf,	Inf,	229,	Inf,	185,	94,	0,	Inf ],
[ Inf,	Inf,	Inf,	255,	Inf,	Inf,	Inf,	210,	Inf,	Inf,	310,	Inf,	Inf,	Inf,	0 ]
])

print ("\nListe des villes:\n\n",Z, "\n")
print ("Matrice des poids (distances en km)\n\n",P, "\n")

N = np.size(P,0)

print("\nNombre de sommets: ",N,"\n\n")
