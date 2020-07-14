import pygame
from Images.imageLoader import *

class Menu:
    def __init__(self, screen):

        self.screen = screen
        self.screenSizeX = screen.get_width()
        self.screenSizeY = screen.get_height()

        self.playbutton = pygame.transform.scale(playbutton, (round(self.screenSizeX/6.4), round(self.screenSizeY/4.8)))
        self.settingsbutton = pygame.transform.scale(settingsbutton, (round(self.screenSizeX/6.4), round(self.screenSizeY/4.8)))
        self.exitbutton = pygame.transform.scale(exitbutton, (round(self.screenSizeX/6.4), round(self.screenSizeY/4.8)))


    def menuScreen(self):

        self.screen.blit(self.playbutton, ((self.screenSizeX/8),(self.screenSizeY/3)))
        self.screen.blit(self.settingsbutton, (((self.screenSizeX/8)*3.5),(self.screenSizeY/3)))
        self.screen.blit(self.exitbutton, (((self.screenSizeX/8)*6), (self.screenSizeY/3)))

    




    
