#Millen -- 2201797531
#L1AC
#---------------------------------

from pygame import *      #import the pygame with *
import sys               #import sys so we can end the game
import pygame           #to run the game with pygame

def menu_screen(Button,run_game):
    """make the screen for menu"""

    screen = pygame.display.set_mode((800, 600))    #size of the screen
    pygame.display.set_caption("Jet Mission")       #name of the game
    #object button for quit and start
    start_button = Button("New Piskel.png")     #summon start button and consider as start_button
    quit_button = Button("quit button.png")     # summon quit button and consider as quit_button
    #image for the menu's backgound
    bg_image=pygame.image.load("asteroid_wall2.jpg") #load the asteroid_wall and consider as bg_image
    bg_image=pygame.transform.scale(bg_image, (800, 600))


    pygame.init()

    while True:
        rect_start= draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) #set the color and the size of rect_start
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150)) #set the color and the size of rect_quit
        screen.blit(bg_image,(0,0))

        screen.blit(start_button.button,(250,200))  #call and set the size of the start button
        screen.blit(quit_button.button,(250,300))   #call and set the size of the quit button

        ev=event.wait()     #pause the game and consider it as ev variable

        if ev.type == MOUSEBUTTONDOWN: #looping for clicking the mouse button
            if rect_start.collidepoint(mouse.get_pos()): #start the game when click the start button
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()): #quit the game when clik the quit button
                sys.exit()

        if ev.type == QUIT: #quit when click the close button "X"
            sys.exit()

        display.update()

def pause_menu(Button,run_game):
    """pause_menu"""
    #make the screen display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Jet Mission")
    # object button for quit and start
    start_button = Button("quit button.png")
    return_button = Button("pause button.png")

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall2.jpg")
    bg_image = pygame.transform.scale(bg_image, (800, 600))


    pygame.init()
    paused=True #pause flag
    while paused:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_return = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image, (0, 0))

        screen.blit(start_button.button, (250, 200))
        screen.blit(return_button.button, (250, 300))

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):    #when clicking the start button it will start the game in the same time before pausing the game
                menu_screen(Button,run_game)
            if rect_return.collidepoint(mouse.get_pos()):
                paused = False              #flag become  False

        if ev.type == QUIT:
            sys.exit()


        display.update()

def lose_menu(Button,run_game,score):
    """make the screen for menu"""
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Jet Mission")
    font=pygame.font.SysFont("times new roman",100) #size and type of the font
    text=font.render("   Replay?",True,(255,0,0))   #it will show in the lose screen on the top and colored
    score_text=font.render("score:"+str(score),True,(255,0,0))  #it will show in the lose screen on the top and colored

    # object button for quit and start
    start_button = Button("New Piskel.png") #summon New Piksel and consider as Start_button
    quit_button = Button("quit button.png") #summon quit button and consider as quit_button

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall2.jpg")   #load asteroid_wall image and consider as bg_image
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    pygame.init()

    while True:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) #set the position and color of rect_start
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))  #set the position and color of rect_quit
        screen.blit(bg_image, (0, 0))   #call the background image
        screen.blit(text,(200,10))      #put the position
        screen.blit(start_button.button, (250, 200))
        screen.blit(quit_button.button, (250, 300))
        screen.blit(score_text,(200,400))

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()): #start when clicking the start button
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()): #quit when cliking the quit button
                sys.exit()

        if ev.type == QUIT:
            sys.exit()

        display.update()
