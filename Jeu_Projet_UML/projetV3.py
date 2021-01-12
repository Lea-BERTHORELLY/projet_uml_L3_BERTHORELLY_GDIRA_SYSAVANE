#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      leabty
#
# Created:     11/12/2020
# Copyright:   (c) leabty 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
from random import *
from personnage import *




########## création de la map ##################################################

hauteur = int(input("Taille de la ville (entre 10 et 15) : "))
largeur = hauteur
while(hauteur<10 or hauteur>15):
    hauteur = int(input("Taille de la ville (entre 10 et 15) : "))
    largeur=hauteur

map=largeur*[0]
for i in range(len(map)):
    map[i]=hauteur*[0]

pygame.init()
pygame.display.set_caption("Ma simulation")
taille_écran = (hauteur*50, largeur*50)
fenetre = pygame.display.set_mode(taille_écran)
################################################################################

########## création des images du jeu ##########################################
fondMenu = pygame.image.load("imagesProjet/menu.jpg").convert()
fond = pygame.image.load("imagesProjet/fond.jpg").convert()
maison = pygame.image.load("imagesProjet/maison.png").convert_alpha()
biblio = pygame.image.load("imagesProjet/biblio.png").convert_alpha()
fastfood = pygame.image.load("imagesProjet/fastfood.png").convert_alpha()
universite = pygame.image.load("imagesProjet/universite.png").convert_alpha()
bar = pygame.image.load("imagesProjet/bar.png").convert_alpha()
perso = pygame.image.load("imagesProjet/perso.png").convert_alpha()
trottoir = pygame.image.load("imagesProjet/trottoir.png").convert_alpha()
foret = pygame.image.load("imagesProjet/foret.png").convert_alpha()
lac = pygame.image.load("imagesProjet/lac.png").convert_alpha()
mur = pygame.image.load("imagesProjet/mur.jpg").convert()
fin = pygame.image.load("imagesProjet/fin.jpg").convert()

fondMenu=pygame.transform.scale(fondMenu,(hauteur*50,largeur*50))
fin= pygame.transform.scale(fin,(hauteur*50,largeur*50))
maison=pygame.transform.scale(maison,(50,50))
biblio=pygame.transform.scale(biblio,(50,50))
fastfood=pygame.transform.scale(fastfood,(50,50))
bar=pygame.transform.scale(bar,(50,50))
universite=pygame.transform.scale(universite,(50,50))
perso=pygame.transform.scale(perso,(50,50))
trottoir=pygame.transform.scale(trottoir,(50,50))
foret=pygame.transform.scale(foret,(50,50))
lac=pygame.transform.scale(lac,(50,50))
mur=pygame.transform.scale(mur,(50,50))

########## Initialisation des bâtiments ########################################

def initBats():
    """ Cette fonction permet de créer les instances des différents éléments et les note dans le tableau map"""

    Maison=0
    while(Maison!=1):
        ligne=colonne=0
        if map[ligne][colonne]==0:
            map[ligne][colonne]=1
            Maison+=1

    bibliotheque=0
    while(bibliotheque!=1):
        ligne=randrange(hauteur)
        colonne=randrange(largeur)
        if map[ligne][colonne]==0:
            map[ligne][colonne]=2
            bibliotheque+=1

    fastFood=0
    while(fastFood!=1):
        ligne=randrange(hauteur)
        colonne=randrange(largeur)
        if map[ligne][colonne]==0:
            map[ligne][colonne]=3
            fastFood+=1

    Bar=0
    while(Bar!=1):
        ligne=randrange(hauteur)
        colonne=randrange(largeur)
        if map[ligne][colonne]==0:
            map[ligne][colonne]=4
            Bar+=1

    Universite=0
    while(Universite!=1):
        ligne=randrange(hauteur)
        colonne=randrange(largeur)
        if map[ligne][colonne]==0:
            map[ligne][colonne]=5
            Universite+=1

    for colonne in range(0,1):
        for ligne in range (hauteur):
            if map[ligne][colonne]==0:
                map[ligne][colonne]=6 ###6 correspond au code pour placer les trottoirs

    for ligne in range(0,1):
        for colonne in range (largeur):
            if map[ligne][colonne]==0:
                map[ligne][colonne]=6 ###6 correspond au code pour placer les trottoirs

    for colonne in range(largeur-1,largeur):
        for ligne in range (hauteur):
            if map[ligne][colonne]==0:
                map[ligne][colonne]=6 ###6 correspond au code pour placer les trottoirs

    for ligne in range(hauteur-1,hauteur):
        for colonne in range (largeur):
            if map[ligne][colonne]==0:
                map[ligne][colonne]=6 ###6 correspond au code pour placer les trottoirs

    for ligne in range (hauteur):
        if map[ligne][largeur//2]==0:
            map[ligne][largeur//2]=6 ###6 correspond au code pour placer les trottoirs

    for colonne in range (largeur):
        if map[ligne][hauteur//2]==0:
            map[ligne][hauteur//2]=6 ###6 correspond au code pour placer les trottoirs

    Forets=0
    while(Forets!=2):
        ligne=randrange(hauteur)
        colonne=randrange(largeur)
        if map[ligne][colonne]==0:
            map[ligne][colonne]=7
            Forets+=1

    Lacs=0
    while(Lacs!=3):
        ligne=randrange(hauteur)
        colonne=randrange(largeur)
        if map[ligne][colonne]==0:
            map[ligne][colonne]=8
            Lacs+=1

    Murs=0
    while(Murs!=5):
        ligne=randrange(hauteur)
        colonne=randrange(largeur)
        if map[ligne][colonne]==0:
            map[ligne][colonne]=9
            Murs+=1


################################################################################
def myMenu():
    fenetre.blit(fondMenu,(0,0))

def initGraphics():
    """ Cette fonction place les différents éléments graphiques aux endroits correspondants, en lisant le tableau map représentant la carte"""
    fenetre.blit(fond,(0,0))

    for colonne in range(largeur):
        for ligne in range(hauteur):
            x=colonne*50
            y=ligne*50
            if(map[ligne][colonne]==1):
                fenetre.blit(maison,(x,y))
            elif(map[ligne][colonne]==2):
                fenetre.blit(biblio,(x,y))
            elif(map[ligne][colonne]==3):
                fenetre.blit(fastfood,(x,y))
            elif(map[ligne][colonne]==4):
                fenetre.blit(bar,(x,y))
            elif(map[ligne][colonne]==5):
                fenetre.blit(universite,(x,y))
            elif(map[ligne][colonne]==6):
                fenetre.blit(trottoir,(x,y))
            elif(map[ligne][colonne]==7):
                fenetre.blit(foret,(x,y))
            elif(map[ligne][colonne]==8):
                fenetre.blit(lac,(x,y))
            elif(map[ligne][colonne]==9):
                fenetre.blit(mur,(x,y))


    pygame.display.flip()
################################################################################

###################### fonctions pour le personnage #############################
def gagnerMoral(personnage):
    if Perso.type!=2:
        if map[ligne][colonne]==1: ##maison
            if ((Perso.maxMoral)-(Perso.moral)>=10):
                Perso.moral +=10
            elif ((Perso.maxMoral)-(Perso.moral)<10):
                Perso.moral +=(Perso.maxMoral-Perso.moral)
            elif((Perso.maxMoral)-(Perso.moral)==0):
                print("Le moral est au maximum")
        elif map[ligne][colonne]==2: ##bibliotheque
            if ((Perso.maxMoral)-(Perso.moral)>=20):
                Perso.moral +=20
            elif ((Perso.maxMoral)-(Perso.moral)<20):
                Perso.moral +=(Perso.maxMoral-Perso.moral)
            elif((Perso.maxMoral)-(Perso.moral)==0):
                print("Le moral est au maximum")
def gagnerHydratation(personnage):
    if map[ligne][colonne]==1: ##maison
        if ((Perso.maxHydratation)-(Perso.hydratation)>=10):
            Perso.hydratation +=10
        elif ((Perso.maxHydratation)-(Perso.hydratation)<10):
            Perso.hydratation +=(Perso.maxHydratation-Perso.hydratation)
        elif((Perso.hydratation)-(Perso.maxHydratation)==0):
            print("L'hydratation est au maximum")
    elif map[ligne][colonne]==4: ##bar
        if ((Perso.maxHydratation)-(Perso.hydratation)>=25):
            Perso.hydratation +=25
        elif((Perso.maxHydratation)-(Perso.hydratation)<25):
            Perso.hydratation +=(Perso.maxHydratation-Perso.hydratation)
        elif((Perso.maxHydratation)-(Perso.hydratation)==0):
            print("L'hydratation est au maximum")

def gagnerSatiete(personnage):
    if map[ligne][colonne]==1: ##maison
        if ((Perso.maxSatiete)-(Perso.satiete)>=10):
            Perso.satiete +=10
        elif ((Perso.maxSatiete)-(Perso.satiete)<10):
            Perso.satiete +=(Perso.maxSatiete-Perso.satiete)
        elif((Perso.satiete)-(Perso.maxSatiete)==0):
            print("La satiété est au maximum")  
    elif map[ligne][colonne]==3: ##fastfood
        if ((Perso.maxSatiete)-(Perso.satiete)>=25):
            Perso.satiete +=25
        elif ((Perso.maxSatiete)-(Perso.satiete)<25):
            Perso.satiete +=(Perso.maxSatiete-Perso.satiete)
        elif((Perso.satiete)-(Perso.maxSatiete)==0):
            print("La satiété est au maximum")

def isHeDead(personnage):
    if Perso.vie <=0 or Perso.moral<=0 or Perso.hydratation<=0 or Perso.satiete<=0:
        end=1

def perdreVie(personnage):
    if (map[ligne][colonne]==3): ## si le personnage va au fast-food il perd 5 pts de vie
        Perso.vie-=5
    elif(map[ligne][colonne]==4): ## si le personnage va au bar il perd 3 pts de vie
        Perso.vie-=3
    
def tomberMalade(personnage):
    n=randint(1,100) ## on génère un nombre au hasard
    if map[ligne][colonne]==7: ##Si le personnage est en forêt
        if n<=10: ## et si la valeur est entre 1 et 10 (donc 10 %), le personnage tombe malade
            Perso.vie-=10 ## et donc il perd 10 pv
    else:
        if n<=5: ## si la valeur est entre 1 et 5 (donc 5 %), le personnage tombe malade
            Perso.vie-=10 ## et donc il perd 10 pv

################################################################################


posPerso= perso.get_rect()
for colonne in range(largeur):
    for ligne in range(hauteur):
        x=colonne*50
        y=ligne*50
        if(map[ligne][colonne]==1):
            fenetre.blit(perso,(x,y))
            posPerso.center=x,y

initBats()

ligne=colonne=0
menu=1
simulation=0
end=0
continuer=1



while(continuer):
    for event in pygame.event.get():

        if menu==1:
            myMenu()
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_1: #Si on appuie sur la touche 1 on lance la simulation avec le personnage standard
                    Perso=personnage(75,75,75,75,75,75,75,75,1) # 1=homme standard
                    menu=0
                    simulation=1
                elif event.key == K_2:
                    Perso=personnage(75,75,50,50,50,50,100,100,2) # 2=homme hippie
                    menu=0
                    simulation=1
                elif event.key == K_3:
                    Perso=personnage(100,100,75,75,75,75,50,50,3) # 3=homme pressé
                    menu=0
                    simulation=1
            pygame.display.flip()
        elif simulation==1:
            fenetre.blit(fond,(0,0))
            initGraphics()
            fenetre.blit(perso,posPerso)

            pygame.display.flip()
            if event.type == QUIT:
                continuer = 0
            elif event.type == KEYDOWN:
                if event.key== K_UP or event.key==K_w : #Le personnage monte
                    if posPerso.top>0 and (map[ligne-1][colonne]!=9):
                        posPerso=posPerso.move(0,-50)
                        ligne=ligne-1
                    initGraphics()
                    fenetre.blit(perso,posPerso)
                    gagnerMoral(Perso)
                    gagnerHydratation(Perso)
                    gagnerSatiete(Perso)
                    if Perso.type==1:
                        Perso.perdrePoints(1,1,1,1)
                        Perso.perdrePointsDeps(1,1,1,1)
                    elif Perso.type==2:
                        Perso.perdrePoints(0,0.5,0.5,0.5)
                        Perso.perdrePointsDeps(0,2,2,2)
                    elif Perso.type==3:
                        Perso.perdrePoints(1,1,1,1)
                        Perso.perdrePointsDeps(2,0,0,0)
                    perdreVie(Perso)
                    tomberMalade(Perso)
                    isHeDead(Perso)


                elif event.key== K_DOWN or event.key==K_s: #Le personnage descend
                    if ligne<hauteur:
                        if posPerso.bottom<(hauteur*50) and (map[ligne+1][colonne]!=9):
                            posPerso=posPerso.move(0,50)
                            ligne=ligne+1
                        initGraphics()
                        fenetre.blit(perso,posPerso)
                        gagnerMoral(Perso)
                        gagnerHydratation(Perso)
                        gagnerSatiete(Perso)
                        if Perso.type==1:
                            Perso.perdrePoints(1,1,1,1)
                            Perso.perdrePointsDeps(1,1,1,1)
                        elif Perso.type==2:
                            Perso.perdrePoints(0,0.5,0.5,0.5)
                            Perso.perdrePointsDeps(0,2,2,2)
                        elif Perso.type==3:
                            Perso.perdrePoints(1,1,1,1)
                            Perso.perdrePointsDeps(2,0,0,0)
                        perdreVie(Perso)
                        tomberMalade(Perso)
                        isHeDead(Perso)


                elif event.key== K_LEFT or event.key==K_a: #Le personnage va à gauche
                    if posPerso.left>0 and (map[ligne][colonne-1]!=9):
                        posPerso=posPerso.move(-50,0)
                        colonne=colonne-1
                    initGraphics()
                    fenetre.blit(perso,posPerso)
                    gagnerMoral(Perso)
                    gagnerHydratation(Perso)
                    gagnerSatiete(Perso)
                    if Perso.type==1:
                        Perso.perdrePoints(1,1,1,1)
                        Perso.perdrePointsDeps(1,1,1,1)
                    elif Perso.type==2:
                        Perso.perdrePoints(0,0.5,0.5,0.5)
                        Perso.perdrePointsDeps(0,2,2,2)
                    elif Perso.type==3:
                        Perso.perdrePoints(1,1,1,1)
                        Perso.perdrePointsDeps(2,0,0,0)
                    perdreVie(Perso)
                    tomberMalade(Perso)
                    isHeDead(Perso)


                elif event.key == K_RIGHT or event.key==K_d: #Le personnage va à droite
                    if colonne<largeur:
                        if posPerso.right<(largeur*50) and (map[ligne][colonne+1]!=9):
                            posPerso=posPerso.move(50,0)
                            colonne=colonne+1
                        initGraphics()
                        fenetre.blit(perso,posPerso)
                        gagnerMoral(Perso)
                        gagnerHydratation(Perso)
                        gagnerSatiete(Perso)
                        if Perso.type==1:
                            Perso.perdrePoints(1,1,1,1)
                            Perso.perdrePointsDeps(1,1,1,1)
                        elif Perso.type==2:
                            Perso.perdrePoints(0,0.5,0.5,0.5)
                            Perso.perdrePointsDeps(0,2,2,2)
                        elif Perso.type==3:
                            Perso.perdrePoints(1,1,1,1)
                            Perso.perdrePointsDeps(2,0,0,0)
                        perdreVie(Perso)
                        tomberMalade(Perso)
                        isHeDead(Perso)
        elif end==1:
            fenetre.blit(fin,(0,0))

pygame.display.flip()
pygame.quit()