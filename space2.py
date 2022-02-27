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
