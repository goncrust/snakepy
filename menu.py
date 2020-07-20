import pygame
from Images.imageLoader import *


class Menu:
    def __init__(self, screen):

        self.selected = 1

        self.screen = screen
        self.screenSizeX = screen.get_width()
        self.screenSizeY = screen.get_height()

        self.playbuttonX = self.screenSizeX/8
        self.playbuttonY = self.screenSizeY/3
        self.settingsbuttonX = (self.screenSizeX/8)*3.5
        self.settingsbuttonY = self.screenSizeY/3
        self.exitbuttonX = (self.screenSizeX/8)*6
        self.exitbuttonY = self.screenSizeY/3

        self.playbutton_width = round(self.screenSizeX/6.4)
        self.playbutton_height = round(self.screenSizeY/4.8)
        self.settingsbutton_width = round(self.screenSizeX/6.4)
        self.settingsbutton_height = round(self.screenSizeY/4.8)
        self.exitbutton_width = round(self.screenSizeX/6.4)
        self.exitbutton_height = round(self.screenSizeY/4.8)

        self.playbutton = pygame.transform.scale(
            playbutton, (self.playbutton_width, self.playbutton_height))
        self.settingsbutton = pygame.transform.scale(
            settingsbutton, (self.settingsbutton_width,
                             self.settingsbutton_height))
        self.exitbutton = pygame.transform.scale(
            exitbutton, (self.exitbutton_width, self.exitbutton_height))

        self.playbuttonselected = pygame.transform.scale(
            playbuttonselected, (self.playbutton_width, self.playbutton_height))
        self.settingsbuttonselected = pygame.transform.scale(
            settingsbuttonselected, (self.settingsbutton_width,
                                     self.settingsbutton_height))
        self.exitbuttonselected = pygame.transform.scale(
            exitbuttonselected, (self.exitbutton_width, self.exitbutton_height))

    def selectbutton(self, mosX, mosY):

        if mosX >= self.playbuttonX and mosX <= self.playbuttonX + self.playbutton_width and mosY >= self.playbuttonY and mosY <= self.playbuttonY + self.playbutton_height:
            self.selected = 1
        if mosX >= self.settingsbuttonX and mosX <= self.settingsbuttonX + self.settingsbutton_width and mosY >= self.settingsbuttonY and mosY <= self.settingsbuttonY + self.settingsbutton_height:
            self.selected = 2
        if mosX >= self.exitbuttonX and mosX <= self.exitbuttonX + self.exitbutton_width and mosY >= self.exitbuttonY and mosY <= self.exitbuttonY + self.exitbutton_height:
            self.selected = 3

    def menuScreen(self):

        if self.selected == 1:
            self.screen.blit(self.playbuttonselected,
                             (self.playbuttonX, self.playbuttonY))
        else:
            self.screen.blit(
                self.playbutton, (self.playbuttonX, self.playbuttonY))
        if self.selected == 2:
            self.screen.blit(self.settingsbuttonselected,
                             (self.settingsbuttonX, self.settingsbuttonY))
        else:
            self.screen.blit(self.settingsbutton,
                             (self.settingsbuttonX, self.settingsbuttonY))
        if self.selected == 3:
            self.screen.blit(self.exitbuttonselected,
                             (self.exitbuttonX, self.exitbuttonY))
        else:
            self.screen.blit(
                self.exitbutton, (self.exitbuttonX, self.exitbuttonY))
