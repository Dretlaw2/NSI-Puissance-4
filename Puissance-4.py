#Puissance 4
from turtle import *
from random import randint

#Crée une grille vide
def grille_vide():
    return [[0]*7 for i in range(6)]

#affiche une grille remplie de carrés gris 
def grille_grise(g):
    for l in range(6):
        for c in range(7):
            carre_gris(c,l)

#Affiche la grille
def affiche(g):
    for l in range(6):
        for c in range(7):
            if g[l][c] ==1:
                carre_blanc(c,l)
                rond_bleu(c,l)
            elif g[l][c]==2:
                carre_blanc(c,l)
                rond_rouge(c,l)
      

#Place un carré blanc                
def carre_blanc(c,l):
    up()
    goto(50*c,50*l)
    down()
    color('white')
    begin_fill()
    backward(20)
    for i in range(4):
        forward(40)
        left(90)
    end_fill()

#Place un rond bleu

def rond_bleu(c,l):
    up()
    goto(50*c,50*l)
    down()
    fillcolor('blue')
    begin_fill()
    circle(20,360)
    end_fill()

#Place un carré gris

def carre_gris(c,l):
    up()
    goto(50*c,50*l)
    down()
    fillcolor('grey')
    begin_fill()
    backward(20)
    for i in range(4):
        forward(40)
        left(90)
    end_fill()

#Place un rond rouge
def rond_rouge(c,l):
    up()
    goto(50*c,50*l)
    down()
    fillcolor('red')
    begin_fill()
    circle(20,360)
    end_fill()
    
#coup possible
def coup_possible(g,c):
    if c >= 1 and c <=7:
        c -= 1   
        if g[5][c] == 0:
            return True
        else:
            return False
    else:
        return False

#Jouer
def jouer(g,j,c):    
    l=0
    while g[l][c-1] != 0:
        l +=1
    g[l][c-1] = j  
                
# Vérification Horizontale
def horiz(g,j,l,c):
    if c < 4:
        if g[l][c] == j and g[l][c+1]== j and g[l][c+2]== j and g[l][c+3]== j:
            return True
    
#Vérification Verticale
def vert(g,j,l,c):
    if l < 3:
        if g[l][c] == j and g[l+1][c]== j and g[l+2][c]== j and g[l+3][c]== j:
            return True
    
#Vérification diagonaleshaut                
def diag_haut(g,j,l,c):
    if l < 3 and c < 4:
        if g[l][c] == j and g[l+1][c+1]== j and g[l+2][c+2]== j and g[l+3][c+3]== j:
            return True
    
#Vérification diagonales bas 
def diag_bas(g,j,l,c):
    if l > 2 and c < 4:
        if g[l][c] == j and g[l-1][c+1]== j and g[l-2][c+2]== j and g[l-3][c+3]== j:
            return True
    
#victoire     
def victoire(g,j):
    for l in range(6):
        for c in range(7):
            if horiz(g,j,l,c)==True or vert(g,j,l,c)==True or diag_haut(g,j,l,c)==True or diag_bas(g,j,l,c)==True:
                return True   
            
#match nul       
def match_nul(g,j):
    for c in range(7):
        if g[5][c]==0:
            return False
        
#coup joueur       
def coup_joueur(g,j):
    c = 0
    c=int(numinput(("joueur",j),"entrez une colonne : "))
    while coup_possible(g,c) == False:
        print("coup impossible !")
        c=int(numinput(("joueur",j),"entrez une colonne : "))
        
    jouer(g,j,c)

    #coup aléatoire
def coup_aleatoire(g,j):
    c = randint(1,7)
    while coup_possible(g,c) == False:
        c = randint(1,7)
    jouer(g,j,c)
            

#programme principal
restartGame = 1
while restartGame:
    title("puissance 4")
    hideturtle()
    clear()
    speed(0)
    modeGame = int(numinput(("Mode de Jeu"),"Entrez le mode de jeu voulu (cf: Mode d'emploi) : "))
    while modeGame <0 or modeGame >2:
        clear()
        style = ('Courier', 20, 'bold')
        color('red')
        write('Mode de jeu impossible ! ', font=style, align='center')
        modeGame = int(numinput(("Mode de Jeu"),"Entrez le mode de jeu voulu (cf: Mode d'emploi) : "))
    clear() 
    color('black')
    g=grille_vide()
    grille_grise(g)
    j=2
    while victoire(g,j) != True and match_nul(g,j)==False:
        j=3-j
        if (modeGame == 2) or (modeGame == 1 and j == 1):
            coup_joueur(g,j)
        elif (modeGame == 1 and j != 1) or (modeGame == 0):
            coup_aleatoire(g,j)
        affiche(g) 
    goto(0,0)
    clear()
    color('blue')
    style = ('Courier', 20, 'bold')
    write('Victoire du joueur: '+ str(j) + '!', font=style, align='center')
    restartGame = int(numinput(("Redémarrage de la partie"),"Souhaitez-vous recommencer une partie ? (1 = Oui, 2 = Non)"))
    if (restartGame == 2):
        quit()
    while (restartGame < 1 or restartGame > 2): 
        color('red')
        clear()
        style = ('Courier', 20, 'bold')
        write('Valeur non autorisé ! ', font=style, align='center')
        restartGame = int(numinput(("Redémarrage de la partie"),"Souhaitez-vous recommencer une partie ? (1 = Oui, 2 = Non)"))
