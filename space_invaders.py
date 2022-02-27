import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
# chargement de l'image de fond

fond = pygame.image.load('picture/background.png')

boutton_image =  pygame.image.load('picture/boutton.png')
vie_image = pygame.image.load('picture/vie.png')
vitesse_image = pygame.image.load('picture/vitesse.png')
chargeur_image = pygame.image.load('picture/chargeur.png')

font = pygame.font.Font("verdana.ttf",30)
BLANC = (255,255,255)


# creation du joueur
player = space.Joueur()
# creation de la balle
upgrade = space.upgrade(player)
# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
listBalle = []
listBalle.append(space.Balle(player))

pause = False

### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))

    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_SPACE : # espace pour tirer
                player.tirer(listBalle)
                                                                                                                                # tir.etat = "tiree"
        elif event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
            if event.button == 1: # 1= clique gauche
                if menu.collidepoint(event.pos):
                    if pause :
                        pause = 0
                    else :
                        pause = 1
                else:
                    if pause:
                        if vie.collidepoint(event.pos):
                            upgrade.add_life()
                        elif vitesse.collidepoint(event.pos):
                            upgrade.add_vitesse()
                        elif chargeur.collidepoint(event.pos):
                            upgrade.add_balle(listBalle)
    ### Actualisation de la scene ###
    # Gestions des collisions
    for ennemi in listeEnnemis:
        for tir in listBalle:
            if tir.toucher(ennemi):
                player.marquer(ennemi.type)
                ennemi.disparaitre()





    # placement des objets
    # le joueur
    player.deplacer(pause,upgrade.vitesse)
    for tir in listBalle:
        screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
        # la balle
        tir.bouger(pause,upgrade.vitesse)
    screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer(pause,player)
        screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur






#               le menu 

    score = font.render(str(f'space coin: {player.score}'), 1, BLANC)
    screen.blit(score, (2,4))

    vie = font.render(str(f'vie: {player.vie}'), 1, BLANC)
    screen.blit(vie, (350,4))

    menu = pygame.Rect((700, 0), (800, 100))
    screen.blit(boutton_image,[700, 0])
  

    if pause :
        menu_fond = pygame.Surface(pygame.Rect((100, 100), (600, 500)).size)
        menu_fond.fill((0,0,0))
        screen.blit(menu_fond,pygame.Rect((100, 100), (600, 500)))


        vie = pygame.Rect((150, 150), (500, 100))
        screen.blit(vie_image,[100, 150])

        chargeur = pygame.Rect((150, 300), (500, 100))
        screen.blit(chargeur_image,[100, 300])

        vitesse = pygame.Rect((150, 450), (500, 100))
        screen.blit(vitesse_image,[100, 450])





        
    pygame.display.update() # pour ajouter tout changement à l'écran