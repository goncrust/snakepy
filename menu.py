import pygame
from Images.imageLoader import *

class Menu:
    def __init__(self, screen):
        
        
        self.selected = []
        self.screen = screen
        self.screenSizeX = screen.get_width()
        self.screenSizeY = screen.get_height()
        self.playbuttonX = self.screenSizeX/8
        self.playbuttonY = self.screenSizeY/3
        self.settingsbuttonX = (self.screenSizeX/8)*3.5
        self.settingsbuttonY = self.screenSizeY/3
        self.exitbuttonX = (self.screenSizeX/8)*6
        self.exitbuttonY = self.screenSizeY/3
        self.playbutton_whidth = playbutton.get_width()
        self.playbutton_height = playbutton.get_height()
        self.settingsbutton_whidth = settingsbutton.get_width()
        self.settingsbutton_height = settingsbutton.get_height()
        self.exitbutton_whidth = exitbutton.get_width()
        self.exitbutton_height = exitbutton.get_height()
        
        self.playbutton = pygame.transform.scale(playbutton, (round(self.screenSizeX/6.4), round(self.screenSizeY/4.8)))
        self.settingsbutton = pygame.transform.scale(settingsbutton, (round(self.screenSizeX/6.4), round(self.screenSizeY/4.8)))
        self.exitbutton = pygame.transform.scale(exitbutton, (round(self.screenSizeX/6.4), round(self.screenSizeY/4.8)))

        self.playbuttonselected = pygame.transform.scale(playbuttonselected, (round(self.screenSizeX/6.4), round(self.screenSizeY/4.8)))
        self.settingsbuttonselected = pygame.transform.scale(settingsbuttonselected, (round(self.screenSizeX/6.4), round(self.screenSizeY/4.8)))
        self.exitbuttonselected = pygame.transform.scale(exitbuttonselected, (round(self.screenSizeX/6.4), round(self.screenSizeY/4.8)))

    def selectbutton(self, mosX, mosY):

        if mosX >= self.playbuttonX and mosX <= self.playbuttonX + self.playbutton_whidth and mosY >= self.playbuttonY and mosY <= self.playbuttonY + self.playbutton_height:
            self.selected = 1
        if mosX >= self.settingsbuttonX and mosX <= self.settingsbuttonX + self.settingsbutton_whidth and mosY >= self.settingsbuttonY and mosY <= self.settingsbuttonY + self.settingsbutton_height:
            self.selected = 2
        if mosX >= self.exitbuttonX and mosX <= self.exitbuttonX + self.exitbutton_whidth and mosY >= self.exitbuttonY and mosY <= self.exitbuttonY + self.exitbutton_height:
            self.selected = 3

    def menuScreen(self):
    
        if self.selected == 1:
            self.screen.blit(self.playbuttonselected, (self.playbuttonX, self.playbuttonY))
        else:
            self.screen.blit(self.playbutton, (self.playbuttonX, self.playbuttonY))
        if self.selected == 2:
            self.screen.blit(self.settingsbuttonselected, (self.settingsbuttonX, self.settingsbuttonY))
        else:
            self.screen.blit(self.settingsbutton, (self.settingsbuttonX, self.settingsbuttonY))
        if self.selected == 3:
            self.screen.blit(self.exitbuttonselected, (self.exitbuttonX, self.exitbuttonY))
        else:
            self.screen.blit(self.exitbutton, (self.exitbuttonX, self.exitbuttonY))

    
