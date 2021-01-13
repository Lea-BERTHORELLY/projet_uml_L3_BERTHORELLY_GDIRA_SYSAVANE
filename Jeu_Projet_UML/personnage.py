import pygame
from pygame.locals import *



######### création des prsonnages #################################################
class personnage(object):
    #méthode __init__ avec 4 arguments (sans compter self !)
    def __init__(self, Vie, VieMax, Hydratation, HydratationMax, Satiete, SatieteMax, Moral, MoralMax, Type):
        self.image = pygame.image.load("imagesProjet/perso.png").convert_alpha()
        self.vie = Vie
        self.maxVie = VieMax
        self.hydratation = Hydratation
        self.maxHydratation = HydratationMax
        self.satiete = Satiete
        self.maxSatiete = SatieteMax
        self.moral = Moral
        self.maxMoral = MoralMax
        self.nbDiplome = 0
        self.deplacement = 1 ##1 = à pied
        self.type = Type

    

    def perdrePoints(self,Moral,Vie,Hydratation,Satiete):
        self.moral-=Moral
        self.vie-=Vie
        self.hydratation-=Hydratation
        self.satiete-=Satiete

    def perdrePointsDeps(self,Moral,Vie,Hydratation,Satiete):
        self.moral-=Moral
        self.vie-=Vie
        self.hydratation-=Hydratation
        self.satiete-=Satiete


            
