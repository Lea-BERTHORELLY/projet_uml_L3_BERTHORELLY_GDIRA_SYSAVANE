#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ghizlane
#
# Created:     30-12-2020
# Copyright:   (c) ghizlane 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame

#classe personnage
class Personnage(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        #self.game = game
        self.vie = 100
        self.maxVie = 100
        self.hydratation = 100
        self.maxHydratation = 100
        self.satiete = 100
        self.maxSatiete = 100
        self.morale = 100
        self.maxMorale = 100
        self.nbDiplome = 0

        self.attack = 10
        self.vitesse = 1
        self.image = pygame.image.load('images/naruto1.png')

        #deplacer l'image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 420
    def deplacement_droit(self):
        self.rect.x += self.vitesse
        #if(self.game.check_collision(self, self.ga))
    def deplacement_gauche(self):
        self.rect.x -= self.vitesse
    def deplacement_haut(self):
        self.rect.y -= self.vitesse
    def deplacement_bas(self):
        self.rect.y += self.vitesse
class PersonnageStandard(pygame.sprite.Sprite):
    def __init__(self):
        self.vie = 75
        self.hydratation = 75
        self.satiete = 75
        self.morale = 75
        self.pseudo = 'standard'
        self.nbDiplome = 0
class PersonnageHippie(pygame.sprite.Sprite):
    def __init__(self):
        self.vie = 75
        self.hydratation = 50
        self.satiete = 50
        self.morale = 100
        self.pseudo = 'hippie'
        self.nbDiplome = 0
class PersonnagePresse(pygame.sprite.Sprite):
    def __init__(self):
        self.vie = 100
        self.hydratation = 75
        self.satiete = 75
        self.morale = 50
        self.pseudo = 'standard'
        self.nbDiplome = 0