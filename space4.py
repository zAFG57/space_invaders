from random import randint
import pygame  # necessaire pour charger les images et les sons






class Joueur() : # classe pour créer le vaisseau du joueur
    position = 0
    image = pygame.image.load('picture/vaisseau.png')
    sens = ''

    def __init__(self) :
        pass

    def deplacer(self) :
        if self.sens == 'gauche' :
            if self.position >=0.2 :
                self.position -= 0.2 
            else :
                self.sens = "O"
        elif self.sens == 'droite' : 
            if self.position <= (800 - 64) - 0.2 :  # cette valeur est la taile de la fenètre moins le taile du déplacement moins la largeur du vaisseau
                self.position += 0.2 
            else :
                self.sens = "O"
    def tirer(self,tir) :
            if tir.etat == "chargee" :
                tir.depart = self.position + 16
                tir.hauteur = 506                   # il sagit de la hauteur depuis laquelle la balle est a l'interieur du vaisseau.
                tir.etat = "tiree"
                return



class Balle() :
    tireur = ''
    depart = 800
    hauteur = 600
    etat = "chargee"
    image = pygame.image.load('picture/balle.png')
    def __init__(self,player) :
        self.tireur = player
        pass

    def bouger(self) :
        if self.etat == "tiree" :
            if self.hauteur >= 0.2:
                self.hauteur -= 0.2
            else :
                self.hauteur = 600
                self.depart = 800
                self.etat = "chargee"   #je charge la balle en dehor de l'écrant affin de ne pas le mettre dans le vaisseau pour économiser des performences



class Ennemi() :
    NbEnnemis = 5
    depart = 0
    hauteur = 0
    type = 0
    vitesse = 0
    image = 0

    def __init__(self) :
        self.hauteur = 0
        self.depart = randint(0,736)
        self.type = randint(1,2)
        if self.type == 2:
            self.vitesse = 0.05
            self.image = pygame.image.load('picture/invader1.png')
        else :
            self.vitesse = 0.02
            self.image = pygame.image.load('picture/invader2.png')
        pass

    def avancer(self) :
        self.hauteur += self.vitesse
