#Millen -- 2201797531
#L1AC
#---------------------------------

from pygame import *    #import the pygame with *
from pygame.sprite import *    #also to import sprite with *

class Jet(Sprite):
    """initialize the jet"""

    def __init__(self, screen): #defines a function for the jet
        Sprite.__init__(self)
        """initialize the Jet"""
        self.image = image.load("battlejet.png")    #adds battlejet image
        self.image = pygame.transform.scale(self.image, (90, 50)) #the size of jet that show in game
        self.rect = self.image.get_rect()      #the jet spawn place
        self.rect.x = 10    #the coordination left to right
        self.rect.y = 50    #the coordination up to down
        self.screen = screen
        self.move_speed = 6     #how fast the jet move
        """bullet"""
        self.firerates = 2      #how fast the bullet move

    def moveleft(self):
        self.rect.x -= self.move_speed  #how fast the jet move to left
        display.update()

    def moveright(self):
        self.rect.x += self.move_speed #how fast the jet move to right
        display.update()

    def moveup(self):
        self.rect.y -= self.move_speed  #how fast the jet move to up
        display.update()

    def movedown(self):
        self.rect.y += self.move_speed  #how fast the jet move to down
        display.update()





class Star_bg:      #background setting
    def __init__(self,background):
        self.background=image.load(background)  #to set the background
        self.background=pygame.transform.scale(self.background,(800,600))   #to set the size of the background
        self.background_size=self.background.get_size()     #to get the background size
        self.background_rect=self.background.get_rect()     #to get the background ract
        self.width,self.height=self.background_size
    def draw(self,screen,x,y):
        screen.blit(self.background,(x,y))      #calling the background image so it will show in the game

class Bullet(Sprite):
    def __init__(self,screen, startx, starty):
        Sprite. __init__(self)
        self.startx = startx
        self.starty = starty

        self.speedx = 20        #speed pf the backgrounf to move in horizontal

        self.image = pygame.image.load("bullets.png")       #to add bullets image
        self.image = pygame.transform.scale(self.image,(40,40)) #to set the size of the bullets
        self.rect=self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty
        self.rect.center = (startx,starty)
        self.screen = screen
    def movement(self):
        #self.screen.blit(self.image,[self.startx,self.starty])
        self.rect.left += self.speedx   #to set the speed movement of the jet

class Asteroid(Sprite):
    """initialize the Asteroid"""
    def __init__(self, screen, width, height, speedx, startx, starty):
        Sprite.__init__(self)
        self.startx = startx
        self.starty = starty

        self.speedx = speedx

        self.image = pygame.image.load("meteor.png")    #to add meteor image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty
        self.screen = screen

    def movement(self):
        """method to move the Asteoid"""
        self.rect.left -= self.speedx   #to set the speed of the asteroid


class Button(Sprite):
    """initialize the button"""
    def __init__(self,image):
        Sprite. __init__(self)
        self.button=pygame.image.load(image)        #load button image
        self.button=pygame.transform.scale(self.button,(300,150))       #set the size of the button
