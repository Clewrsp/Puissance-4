##############################################################
# Auteurs : Clément Crespin, Anatole Joris, Faustine Passerat
##############################################################

######################
# Import des librairies

import tkinter as tk
import random as rd

#############################################
########################
# Constantes

LARGEUR = 800
HAUTEUR = 600

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
