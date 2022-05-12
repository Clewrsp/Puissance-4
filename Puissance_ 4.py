from tkinter import *
import random

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
OBJETS = []
HISTORIQUE = []
memoire = [[VIDE]*NB_CASE_LARGEUR for i in range(NB_CASE_HAUTEUR)] + [[BORD] * NB_CASE_LARGEUR]

####################################################
#--------------------GESTION FICHIER----------------
####################################################

def enregistrer():
    #enregistre la memoire sur le fichier save
    global memoire
    fic = open("save","w")
    fic.write(str(memoire))
    fic.close
    
def ouvrir():
    #charge la memoire du fichier save
    global memoire
    fic = open("save","r")
    memoire_ouvrir = fic.read()
    memoire = convert(memoire_ouvrir)
    affiche_save()
    fic.close()
    
################################################   
#---------------UTILITAIRE----------------------
################################################
    
def convert(chaine):
    #converti une liste en chaine de caractère en véritable liste
    mem = [[] for i in range(NB_CASE_HAUTEUR)] + [[BORD] * NB_CASE_LARGEUR]
    lig = 0
    while lig != NB_CASE_HAUTEUR :
        for e in chaine:
            if e == "2" or e == "1" or e == "0" :
                mem[lig].append(e)
                if len(mem[lig]) == NB_CASE_LARGEUR :
                    lig += 1
    return mem

def undo():
    #annule les coups joués
    global HISTORIQUE
    global memoire
    if len(OBJETS) != 0:
        zone_dessin.delete(OBJETS[-1])
        del(OBJETS[-1])
        col = HISTORIQUE[-1][1]
        lig = HISTORIQUE[-1][0]   
        memoire[lig][col] = VIDE
        del(HISTORIQUE[-1])
        change_joueur()
    
def change_joueur():
    #change le numéro du tour, pair pour le joueur jaune et impair pour le rouge
    global num_tour
    num_tour += 1
    return num_tour%2 

def test_puissance4():
    #Cette partie du programme est inspiré d'un code trouvé sur open classrooms
    #avec quelque correction apportée car le code d'origine ne fonctionnait pas
    
    #vérifie les colonnes
    colones = [""] * NB_CASE_LARGEUR
    for i in range(NB_CASE_LARGEUR):
         colones[i] = colones[i].join(memoire[i])
    for e in colones :
        if "1111" in e :
            print("ROUGE GAGNE")
        if "0000" in e :
            print("JAUNE GAGNE")
    
    #vérifie les lignes
    lignes = [""] * NB_CASE_HAUTEUR
    for element in colones :
        for i in range(NB_CASE_HAUTEUR):
            lignes[i] = lignes[i] + element[i]
    for e in lignes :
        if "1111"  in e:
            print("ROUGE GAGNE")
        if "0000" in e :
            print("JAUNE GAGNE")
    
    #vérifie les diagonales
    for i in range(3):
        for j in range(4):
            diag = ""
            for h in range(4):
                diag = diag + memoire[j+h][i+h]
            if "1111" in diag:        
                print("ROUGE GAGNE")
            if "0000" in diag :
                print("JAUNE GAGNE")
    for i in range(3):
        for j in range(3,7):
            diag = ""
            for h in range(4):
                diag = diag + memoire[j-h][i+h]
            if "1111" in diag:
                print("ROUGE GAGNE")
            if "0000" in diag :
                print("JAUNE GAGNE")
                
def est_dans_grille(x,y):
    #test si le curceur se trouve dans la grille
    return 0<= x <= LARGEUR and 0<= y <= HAUTEUR

def case_valide(lig,col):
    #verifie si la case de coordonnée lig col est une case valide
    #donc non occupée par un pion et qui se trouve au dessus d'un support
    if memoire[lig][col] == ROUGE or memoire[lig][col] == JAUNE:
        return False
    if memoire[lig+1][col] == VIDE :
        return False
    else :
        return True
    
def recommencer():
    #vide les données du jeu, avec la memoire
    global memoire
    global num_tour
    global HISTORIQUE
    global OBJETS
    memoire = [[VIDE]*NB_CASE_LARGEUR for i in range(NB_CASE_HAUTEUR)] + [[BORD] * NB_CASE_LARGEUR]
    nettoyer_tableau()
    num_tour = 0
    HISTORIQUE = []
    OBJETS = []
    
def recommencer_sans_grille():
    #réinitialise les variables principales, sauf memoire
    global num_tour
    global HISTORIQUE
    global OBJETS
    nettoyer_tableau()
    num_tour = 0
    HISTORIQUE = []
    OBJETS = []
    
def historique(lig,col): 
    #garde un historique des coordonnées des coups joués
    global HISTORIQUE
    HISTORIQUE.append([lig,col])
    
################################################ 
#--------------AFFICHAGE------------------------    
################################################ 
    
def carre(lig,col,taille):
    #crée la grille sous forme de carrée
    x = col*taille
    y = lig*taille
    return zone_dessin.create_rectangle(x,y,x+taille,y+taille,fill='white') 
                
def mise_a_jour(lig,col,couleur):
    # créé le pion dans la case donnée de la couleur donnée
   global OBJETS 
   x0 = COTE*col
   y0 = COTE*lig
   pion = zone_dessin.create_oval(x0,y0,x0+COTE,y0+COTE,fill=couleur,
                           outline=couleur)
   OBJETS.append(pion)

def affiche_save():
    #affiche la sauvegarde à partir du fichier save
    global memoire
    recommencer_sans_grille()
    print("affichage de la précédente .sauvegarde...")
    for i in range(6):
        for j in range(7):
            lig,col = i,j
            if memoire[lig][col] == ROUGE :
                num_tour = change_joueur()
                memoire[lig][col] = ROUGE
                mise_a_jour(lig,col,"red")
                historique(lig,col)
            if memoire[lig][col] == JAUNE :
                num_tour = change_joueur()
                memoire[lig][col] = JAUNE
                mise_a_jour(lig,col,"yellow")
                historique(lig,col)               
    
def bouton():
    #affiche les boutons et leurs assigent une fonctionalité
    button1 = Button(fen, text="Enregistrer",command=enregistrer)
    button2 = Button(fen, text="Ouvrir",command=ouvrir)
    button3 = Button(fen, text="Recommencer",command = recommencer)
    button4 = Button(fen, text="Annuler coup",command=undo)
    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)
    button4.pack(side=LEFT)
    
def nettoyer_tableau():
    #enleve l'ancienne grille pour en remettre une nouvelle vierge
    zone_dessin.create_rectangle(0,0,LARGEUR,HAUTEUR,fill='white')
    carres = [[carre(lig,col,COTE) for col in range(NB_CASE_LARGEUR)] for lig in range(NB_CASE_HAUTEUR)] 

################################################ 
#--------------- LE CLIC--------------------------
################################################

def clic(event):
    #gère la fonctionnalité du clic GAUCHE de la souris
    x = event.x
    y = event.y
    col = x//COTE
    lig = y//COTE
    if est_dans_grille(x,y):
        if case_valide(lig,col) == True: 
            num_tour = change_joueur()
            memoire[lig][col] = COULEURS[num_tour]
            mise_a_jour(lig,col,COLORS[num_tour])
            historique(lig,col)
            test_puissance4()
            fen.configure(bg=COLORS[num_tour])

################################################ 
#--------------- MAIN --------------------------
################################################ 
   
fen = Tk()
num_tour = random.randint(0,1)
fen.title("Puissance 4")
zone_dessin = Canvas(fen,width=7*COTE,height=6*COTE)
zone_dessin.pack(side=TOP)
zone_dessin.bind('<Button-1>',clic)

bouton()

carres = [[carre(lig,col,COTE) for col in range(NB_CASE_LARGEUR)] for lig in range(NB_CASE_HAUTEUR)]
fen.configure(bg=COLORS[num_tour])
fen.mainloop()