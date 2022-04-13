##############################################################
# Auteurs : Clément Crespin, Anatole Jooris, Faustine Passerat
##############################################################

######################
# Import des librairies

import tkinter as tk
import random as rd

#############################################
########################
# Constantes
AUCUN = 0
ROUGE = 1
JAUNE = 2

LARGEUR = 800
HAUTEUR = 600
NB_CASE_HAUTEUR = 6
NB_CASE_LARGEUR = 7
PREMIER_JOUEUR = "ROUGE"

class Jeu():
    """Contient toutes les informations de la grille de jeu
        -la grille : grille[i][j]
        -le joueur actuel : joueurActif
        """
    __slots__ = ( 
        "grille",
        "joueurActif"
    )
    def __init__(self):
        self.grille = [[AUCUN] * NB_CASE_HAUTEUR for i in range(NB_CASE_LARGEUR)]
        self.joueurActif = PREMIER_JOUEUR

#############################################
###################
# Fonctions




############################
# programme principal

racine = tk.Tk()
racine.title("La balleuh")
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

racine.mainloop()
