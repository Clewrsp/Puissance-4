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

LARGEUR = 710
HAUTEUR = 610
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
"""Creation de la fonction qui affiche la grille"""
def affiche_grille():
    for i in range(1,NB_CASE_LARGEUR):
        point = i * LARGEUR_CASE
        ligne = canvas.create_line((point,0),(point,HAUTEUR),fill="red",width=5)
    for i in range(1,NB_CASE_LARGEUR-1):
        point = i * LARGEUR_CASE
        ligne = canvas.create_line((0,point),(LARGEUR,point),fill="red",width=5)
    canvas.create_line((0,0),(0, LARGEUR), width= 50, fill = "gray")
    canvas.create_line((HAUTEUR, 0),(HAUTEUR, LARGEUR), width= 5, fill = "white")

def affiche_cercle():

    if event(x,y):
        canvas.create_oval(LARGEUR_CASE-5,LARGEUR_CASE-5, 0, 0, fill = "blue")
    return
 
def pointeur(event):
    chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
                            ", Y =" + str(event.y))
 
    cadre = canvas.create_line(width =200, height =150, bg="light yellow")
    cadre.bind("<Button-1>", pointeur)
    cadre.pack()
    chaine = Label(canvas)
    chaine.pack()
 
### Utilitaire

############################
# programme principal

racine = tk.Tk()
racine.title("La balleuh")
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

affiche_grille()
affiche_cercle()

racine.mainloop()
