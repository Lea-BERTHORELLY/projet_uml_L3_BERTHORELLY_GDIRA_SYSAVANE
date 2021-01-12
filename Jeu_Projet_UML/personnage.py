import pygame
from pygame.locals import *



######### création des prsonnages #################################################
class personnage(object):
    #méthode __init__ avec 4 arguments (sans compter self !)
    def __init__(self, Vie, VieMax, Hydratation, HydratationMax, Satiete, SatieteMax, Moral, MoralMax, Type):
        self.image = pygame.image.load("imagesProjet/perso.png").convert_alpha()
        self.vie=Vie
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

    def deplacementPied(self):
        self.deplacement=1

    def deplacementVehicule(self):
        for event in pygame.event.get():
            self.deplacement=2 ## 2=vélo
            if self.type!=2 and event.key==K_c:
                self.deplacement=3 ## 3= voiture
            elif self.type!=2 and event.key==K_b:
                self.deplacement=2
    
    def isHeDead(self):
        if (self.vie) ==0:
            return True
        elif (self.moral)==0:
            return True
        elif (self.hydratation)==0:
            return True
        elif (self.satiete)==0:
            return True
        return False


            
