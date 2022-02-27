from random import randint
import pygame  # necessaire pour charger les images et les sons
import sys # pour fermer correctement le program

pygame.mixer.init()


shot = pygame.mixer.Sound('picture/shot.wav')



class Joueur() : # classe pour créer le vaisseau du joueur
    vie = 3
    position = 0
    image = pygame.image.load('picture/vaisseau.png')
    sens = ''
    score = 0

    def __init__(self) :
        pass

    def deplacer(self,pause,vitesse) :
        if pause: return
        if self.sens == 'gauche' :
            if self.position >=0.2 * vitesse:
                self.position -= 0.2 * vitesse
            else :
                self.sens = "O"
        elif self.sens == 'droite' : 
            if self.position <= (800 - 64) - (0.2 * vitesse):  # cette valeur est la taile de la fenètre moins le taile du déplacement moins la largeur du vaisseau
                self.position += 0.2 * vitesse
            else :
                self.sens = "O"
    def tirer(self,balle) :
            for tir in balle:
                if tir.etat == "chargee" :
                    tir.depart = self.position + 16
                    tir.hauteur = 506
                    shot.play()
                    tir.etat = "tiree"
                    return
    def marquer(self,point) : 
        self.score += point
    
    def est_touché(self):
        if self.vie == 1:
            sys.exit()
        self.vie -= 1
        

class Balle() :
    tireur = ''
    depart = 800
    hauteur = 600
    etat = "chargee"
    image = pygame.image.load('picture/balle.png')
    def __init__(self,player) :
        self.tireur = player
        pass

    def bouger(self,pause,vitesse) :
        if pause: return
        if self.etat == "tiree" :
            if self.hauteur >= 0.2 * vitesse :
                self.hauteur -= 0.2 * vitesse
            else :
                self.hauteur = 600
                self.depart = 800
                self.etat = "chargee"   #je charge la balle en dehor de l'écrant affin de ne pas le mettre dans le vaisseau pour économiser des performences

    def toucher(self,ennemi) :
        if abs(self.depart - ennemi.depart) <= 64 :
            if abs(self.hauteur - ennemi.hauteur) <= 64 :
                self.etat = "chargee"
                self.hauteur = 600
                self.depart = 800
                return 1

        

class Ennemi() :
    NbEnnemis = 5
    depart = 0
    hauteur = 0
    type = 0
    vitesse = 0
    image = 0
    acceleration = 1

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

    def avancer(self,pause,player) :
        if pause:   return
        if self.hauteur  >= 600:
            player.est_touché()
            self.disparaitre()

        self.hauteur += self.vitesse * self.acceleration
        self.acceleration +=  0.000005

    def disparaitre(self) :
        self.__init__()

class upgrade():
    vitesse = 1
    joueur = ''
    def __init__(self,player) :
        self.joueur = player  
        pass

    def add_vitesse(self):
        if self.joueur.score >= 100:
            self.vitesse = self.vitesse * 1.05
            self.joueur.score -=  100

    def add_balle(self,listBalle) :
        if self.joueur.score >= 50:
            listBalle.append(Balle(self.joueur))
            self.joueur.score -=  50

    def add_life(self) :
        if self.joueur.score >= 10:
            self.joueur.score -=  10
            self.joueur.vie += 1