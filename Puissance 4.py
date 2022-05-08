#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:34:43 2022

@author: jp
"""
from tkinter import *

NB_CASE_HAUTEUR = 6
NB_CASE_LONGUEUR = 7

COTE_CASE = 100
LONGUEUR = NB_CASE_LONGUEUR * COTE_CASE
HAUTEUR = NB_CASE_HAUTEUR * COTE_CASE

VIDE = 0
JAUNE = 1
ROUGE = 2

grille = [[VIDE]*NB_CASE_HAUTEUR for i in range(NB_CASE_LONGUEUR)]
joueur_actif = "ROUGE"
    


fenetre = Tk()
fenetre.title("Puissance 4")

jeu = Canvas(fenetre,width = LONGUEUR, height = HAUTEUR)

fenetre.mainloop()
