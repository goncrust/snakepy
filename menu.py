import pygame
from images.image_loader import *


class Menu:
    def __init__(self, screen):

        self.selected = 1

        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.play_button_x = self.screen_width/8
        self.play_button_y = self.screen_height/3
        self.settings_button_x = (self.screen_width/8)*3.5
        self.settings_button_y = self.screen_height/3
        self.exit_button_x = (self.screen_width/8)*6
        self.exit_button_y = self.screen_height/3

        self.play_button_width = round(self.screen_width/6.4)
        self.play_button_height = round(self.screen_height/4.8)
        self.settings_button_width = round(self.screen_width/6.4)
        self.settings_button_height = round(self.screen_height/4.8)
        self.exit_button_width = round(self.screen_width/6.4)
        self.exit_button_height = round(self.screen_height/4.8)

        self.play_button = pygame.transform.scale(
            play_button, (self.play_button_width, self.play_button_height))
        self.settings_button = pygame.transform.scale(
            settings_button, (self.settings_button_width,
                              self.settings_button_height))
        self.exit_button = pygame.transform.scale(
            exit_button, (self.exit_button_width, self.exit_button_height))

        self.play_button_select = pygame.transform.scale(
            play_button_select, (self.play_button_width, self.play_button_height))
        self.settings_button_select = pygame.transform.scale(
            settings_button_select, (self.settings_button_width,
                                     self.settings_button_height))
        self.exit_button_select = pygame.transform.scale(
            exit_button_select, (self.exit_button_width, self.exit_button_height))

    def select_button(self, mos_x, mos_y):

        if mos_x >= self.play_button_x and mos_x <= self.play_button_x + self.play_button_width and mos_y >= self.play_button_y and mos_y <= self.play_button_y + self.play_button_height:
            self.selected = 1
        elif mos_x >= self.settings_button_x and mos_x <= self.settings_button_x + self.settings_button_width and mos_y >= self.settings_button_y and mos_y <= self.settings_button_y + self.settings_button_height:
            self.selected = 2
        elif mos_x >= self.exit_button_x and mos_x <= self.exit_button_x + self.exit_button_width and mos_y >= self.exit_button_y and mos_y <= self.exit_button_y + self.exit_button_height:
            self.selected = 3
        else:
            self.selected = 0

    def menu_screen(self):

        if self.selected == 1:
            self.screen.blit(self.play_button_select,
                             (self.play_button_x, self.play_button_y))
        else:
            self.screen.blit(
                self.play_button, (self.play_button_x, self.play_button_y))
        if self.selected == 2:
            self.screen.blit(self.settings_button_select,
                             (self.settings_button_x, self.settings_button_y))
        else:
            self.screen.blit(self.settings_button,
                             (self.settings_button_x, self.settings_button_y))
        if self.selected == 3:
            self.screen.blit(self.exit_button_select,
                             (self.exit_button_x, self.exit_button_y))
        else:
            self.screen.blit(
                self.exit_button, (self.exit_button_x, self.exit_button_y))

    def menu_option(self):
        if self.selected == 0:
            return
        if self.selected == 1:
            return 1
        if self.selected == 2:
            return 2
        if self.selected == 3:
            return 3
