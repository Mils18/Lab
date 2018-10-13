#Millen -- 2201797531
#L1AC
#---------------------------------

import pygame           #imports pygame module
import menu             #imports menu module
import random           #imports random module for randomize things

from classes import *   #imports everything from classes.py


def run_game():                                 #defines run_game function
    """game play interface"""
    screen = pygame.display.set_mode((800, 600))#screen resolution
    display.set_caption("Star wars")            #set a caption for this game

    scores = 0                          #scores starts from zero
    theClock = pygame.time.Clock()      #Creates an object to help track time
    bg_image = Star_bg("star.gif")      #imports star gif

    #coordinate of moving background
    x = 0
    y = 0
    x1 = bg_image.width
    y1 = 0

    pygame.init()       #initializes all imported pygame modules


    #creating a jet
    jet1 = Jet(screen)
    Jet_sprites = Group(jet1)

    #create asteroid object group
    asteroid_group = Group()

    #create bullets object Group
    bullets = Group()



    Fps = 50
    asteroid_timer = pygame.time.get_ticks()    #asteroid timer
    while True:             #keep looping while it is true
        theClock.tick(Fps)  #sets up how fast the game should run
        Fps += 0.01         #game phase goes faster after every frame

        """background move"""

        #spawns asteroids from the right
        x -= 5
        x1 -= 5
        bg_image.draw(screen,x,y)
        bg_image.draw(screen,x1, y1)
        if x < -bg_image.width:
            x = 0
        if x1 < 0:
            x1 = bg_image.width

        # create score board
        font=pygame.font.SysFont("Times New Romans",36)
        score_board=font.render("score:"+str(scores),True,(255,255,255))
        # update refered to the word's method
        screen.blit(score_board,(10,550))



        Jet_sprites.draw(screen)    #shows jet

        bullets.draw(screen)        #shows bullets

        asteroid_group.draw(screen)
        display.update()            #keep updating jet and screen view

        event.get()
        """moving the jet according to key pressed"""

        #moves the jet according to key pressed
        key = pygame.key.get_pressed()
        if key[K_LEFT] and jet1.rect.x>0:
            jet1.moveleft()

        if key[K_RIGHT] and jet1.rect.x<=700:
            jet1.moveright()

        if key[K_DOWN] and jet1.rect.y<=500:
            jet1.movedown()

        if key[K_UP] and jet1.rect.y>0:
            jet1.moveup()

        #shows bullets if "space" button is pressed
        if key[K_SPACE] and len(bullets) <= jet1.firerates+(scores/4000):
            bullet = Bullet(screen, jet1.rect.x+50, jet1.rect.y+42)
            bullets.add(bullet)
            pygame.mixer.music.load("Laser_Blast2.wav")
            pygame.mixer.music.play()

        #goes back to menu screen if "esc" key is pressed
        if key[K_ESCAPE]:
            menu.menu_screen(Button,run_game)

        #pauses if "p" button is pressed
        if key[K_p]:
            menu.pause_menu(Button,run_game)


        """generate asteroid randomly"""
        if pygame.time.get_ticks() - asteroid_timer >= 200:
            asteroid = Asteroid(screen, 50, 50, random.randint(1,4)*6, 800, (random.randint(1,28) * 20))
            asteroid_group.add(asteroid)
            asteroid_timer = pygame.time.get_ticks()

        """update the movement of asteroid"""
        for asteroid in asteroid_group:
            asteroid.movement()
            if asteroid.rect.right <= 0:
                asteroid_group.remove(asteroid) #remove after screen
            if groupcollide(Jet_sprites,asteroid_group,dokilla=True,dokillb=True):#collition check
                menu.lose_menu(Button,run_game,scores)

        """update bullet movement on screen"""
        for bullet in bullets:
            bullet.movement()
            if bullet.rect.left > 800:
                bullets.remove(bullet)
            if groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True):
                scores += 100


menu.menu_screen(Button,run_game)

#code is made by Pier,Excel,georgius,William,Nicander,Nicolas,Andy,Guntur,Adrian

"""Acknowledgement:
Laser_Blast2.wav(shooting sound) https://www.youtube.com/watch?v=YeMH2zHrvEA
"""