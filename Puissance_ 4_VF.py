#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 21:10:07 2022

@authors: Anatole Jooris, Clément Crespin, Faustine Passerat
"""
from tkinter import *

COTE = 50

NB_CASE_LARGEUR = 7
NB_CASE_HAUTEUR = 6

LARGEUR = NB_CASE_LARGEUR*COTE
HAUTEUR = NB_CASE_HAUTEUR*COTE
VIDE  = "2"
JAUNE = "0"
ROUGE = "1"
BORD = "3"
COULEURS = [JAUNE,ROUGE]
COLORS = ['yellow','red']
memoire = [[VIDE]*NB_CASE_LARGEUR for i in range(NB_CASE_HAUTEUR)] + [[BORD] * NB_CASE_LARGEUR]

def carre(lig,col,taille):
    #crée la grille sous forme de carrée
    x = col*taille
    y = lig*taille
    return zone_dessin.create_rectangle(x,y,x+taille,y+taille,fill='white') 


def est_dans_grille(x,y):
    #test si le curceur se trouve dans la grille
    return 0<= x <= LARGEUR and 0<= y <= HAUTEUR

def case_valide(lig,col):
    #verifie si la case de coordonnée lig col est une case valide
    #donc non occupée par un pion et qui se trouve au dessus d'un support
    if int(memoire[lig][col]) == num_tour%2:
        return False
    if memoire[lig+1][col] == VIDE :
        return False
    else :
        return True
        
        
def mise_a_jour(lig,col,couleur):
    # créé le pion dans la case donnée de la couleur donnée
   x0 = COTE*col
   y0 = COTE*lig
   zone_dessin.create_oval(x0,y0,x0+COTE,y0+COTE,fill=couleur,
                           outline=couleur)

def change_joueur():
    #change le numéro du tour, pair pour le joueur jaune et impair pour le rouge
    global num_tour
    num_tour += 1
    return num_tour%2 

def test_puissance4():
    #Cette partie du programme est inspiré d'un code trouvé sur open classrooms, mais il s'avère qu'elle ne fonctionne pas
    colones = [""] * NB_CASE_LARGEUR
    for i in range(NB_CASE_LARGEUR):
         colones[i] = colones[i].join(memoire[i])
    for e in colones :
        if "1111" in e :
            print("ROUGE GAGNE")
        if "2222" in e :
            print("JAUNE GAGNE")
    
    lignes = [""] * NB_CASE_HAUTEUR
    for element in colones :
        for i in range(NB_CASE_HAUTEUR):
            lignes[i] = lignes[i] + element[i]
    for e in lignes :
        if "1111"  in e:
            print("ROUGE GAGNE")
        if "2222" in e :
            print("JAUNE GAGNE")
    
    for i in range(3):
        for j in range(4):
            diag = ""
            for h in range(4):
                diag = diag + memoire[j+h][i+h]
            if "1111" in element:        
                print("ROUGE GAGNE")
            if "2222" in element :
                print("JAUNE GAGNE")
    for i in range(3):
        for j in range(3,7):
            diag = ""
            for h in range(4):
                diag = diag + memoire[j-h][i-h]
            if "1111" in element:
                print("ROUGE GAGNE")
            if "2222" in element :
                print("JAUNE GAGNE")
        
def clic(event):
    #gère la fonctionnalité du clic droit de la souris
    x = event.x
    y = event.y
    col = x//COTE
    lig = y//COTE
    if est_dans_grille(x,y):
        if case_valide(lig,col) == True: 
            num_tour = change_joueur()
            memoire[lig][col] = COULEURS[num_tour]
            mise_a_jour(lig,col,COLORS[num_tour])
            #test_puissance4()

def nettoyer_tableau():
    #enleve l'ancienne grille pour en remettre une nouvelle vierge
    zone_dessin.create_rectangle(0,0,LARGEUR,HAUTEUR,fill='white')
    carres = [[carre(lig,col,COTE) for col in range(NB_CASE_LARGEUR)] for lig in range(NB_CASE_HAUTEUR)]
        
def recommencer():
    #vide la memoire de la grille
    memoire = 0
    memoire = [[VIDE]*NB_CASE_LARGEUR for i in range(NB_CASE_HAUTEUR)] + [[BORD] * NB_CASE_LARGEUR]
    nettoyer_tableau()
    num_tour = change_joueur()
    
    
def enregistrer():
    #enregistre la memoire sur le fichier save
    fic = open("save","w")
    fic.write(str(memoire))
    fic.close
    
def ouvrir():
    #charge la memoire du fichier save
    fic = open("save","r")
    memoire = fic.read()
    fic.close()
    
#--------------- MAIN --------------------------
fen = Tk()
num_tour = 0
fen.title("Puissance 4")
zone_dessin = Canvas(fen,width=7*COTE,height=6*COTE)
zone_dessin.pack(side=TOP)
zone_dessin.bind('<Button-1>',clic)

button1 = Button(fen, text="Enregistrer",command=enregistrer)
button2 = Button(fen, text="Ouvrir")
button3 = Button(fen, text="Recommencer",command = recommencer)
button4 = Button(fen, text=COULEURS[num_tour])
button1.pack(side=LEFT)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

carres = [[carre(lig,col,COTE) for col in range(NB_CASE_LARGEUR)] for lig in range(NB_CASE_HAUTEUR)]
fen.mainloop()
