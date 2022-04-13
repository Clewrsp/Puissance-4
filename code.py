##############################################################
# Auteurs : Clément Crespin, Anatole Jooris, Faustine Passerat
##############################################################

######################
# Import des librairies

import tkinter as tk
import random as rd

from matplotlib.pyplot import fill

#############################################
########################
# Constantes
AUCUN = 0
ROUGE = 1
JAUNE = 2

LARGEUR = 700
HAUTEUR = 600
NB_CASE_HAUTEUR = 6
NB_CASE_LARGEUR = 7
LARGEUR_CASE = HAUTEUR//NB_CASE_HAUTEUR
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

### Affichage
def affiche_grille():
    for i in range(1,NB_CASE_LARGEUR):
        point = i * LARGEUR_CASE
        ligne = canvas.create_line((point,0),(point,HAUTEUR),fill="red",width=10)
    for i in range(1,NB_CASE_LARGEUR-1):
        point = i * LARGEUR_CASE
        ligne = canvas.create_line((0,point),(LARGEUR,point),fill="red",width=10)
        

def affiche_cercle():  
    return
### Utilitaire

############################
# programme principal

racine = tk.Tk()
racine.title("La balleuh")
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

affiche_grille()

racine.mainloop()