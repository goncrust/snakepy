import pygame
from images.image_loader import *


class Menu:
    def __init__(self, screen):

        # Default selected = 1
        self.selected = 1

        # Handle current menu variables
        self.in_options = False

        # Screen variables
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # --- buttons position ---

        # Main menu
        self.play_button_x = self.screen_width/8
        self.play_button_y = self.screen_height/3
        self.settings_button_x = (self.screen_width/8)*3.5
        self.settings_button_y = self.screen_height/3
        self.exit_button_x = (self.screen_width/8)*6
        self.exit_button_y = self.screen_height/3

        # Options menu
        self.back_button_x = (self.screen_width/8)*3.25
        self.back_button_y = (self.screen_height/5)*2.55
        self.sound_off_button_x = (self.screen_width/8)*3.08
        self.sound_off_button_y = (self.screen_height/5)*1.5
        self.sound_on_button_x = (self.screen_width/8)*3.08
        self.sound_on_button_y = (self.screen_height/5)*1.5

        # --- buttons size ---
        # Variables
        self.play_button_width = round(self.screen_width/6.4)
        self.play_button_height = round(self.screen_height/4.8)
        self.settings_button_width = round(self.screen_width/6.4)
        self.settings_button_height = round(self.screen_height/4.8)
        self.exit_button_width = round(self.screen_width/6.4)
        self.exit_button_height = round(self.screen_height/4.8)

        self.back_button_width = round(self.screen_width/5.57)
        self.back_button_height = round(self.screen_height/12)
        self.sound_off_button_width = round(self.screen_width/4.27)
        self.sound_off_button_height = round(self.screen_height/12)
        self.sound_on_button_width = round(self.screen_width/4.27)
        self.sound_on_button_height = round(self.screen_height/12)

        # Set size
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

        self.back_button = pygame.transform.scale(
            back_button, (self.back_button_width, self.back_button_height))
        self.sound_off = pygame.transform.scale(
            sound_off_button, (self.sound_off_button_width, self.sound_off_button_height))
        self.sound_on = pygame.transform.scale(
            sound_on_button, (self.sound_on_button_width, self.sound_on_button_height))

    # Check selected item
    def select_button(self, mos_x, mos_y):

        # In options
        if (self.in_options):
            if mos_x >= self.sound_on_button_x and mos_x <= self.sound_on_button_x + self.sound_on_button_width and mos_y >= self.sound_on_button_y and mos_y <= self.sound_on_button_y + self.sound_on_button_height:
                self.selected = 1
            elif mos_x >= self.back_button_x and mos_x <= self.back_button_x + self.back_button_width and mos_y >= self.back_button_y and mos_y <= self.back_button_y + self.back_button_height:
                self.selected = 2
            else:
                self.selected = 0
            return

        # In main menu
        if mos_x >= self.play_button_x and mos_x <= self.play_button_x + self.play_button_width and mos_y >= self.play_button_y and mos_y <= self.play_button_y + self.play_button_height:
            self.selected = 1
        elif mos_x >= self.settings_button_x and mos_x <= self.settings_button_x + self.settings_button_width and mos_y >= self.settings_button_y and mos_y <= self.settings_button_y + self.settings_button_height:
            self.selected = 2
        elif mos_x >= self.exit_button_x and mos_x <= self.exit_button_x + self.exit_button_width and mos_y >= self.exit_button_y and mos_y <= self.exit_button_y + self.exit_button_height:
            self.selected = 3
        else:
            self.selected = 0

    # Render menu
    def menu_screen(self, sound):

        # In options
        if (self.in_options):
            if sound:
                self.screen.blit(
                    self.sound_on, (self.sound_on_button_x, self.sound_on_button_y))
            else:
                self.screen.blit(
                    self.sound_off, (self.sound_off_button_x, self.sound_off_button_y))

            self.screen.blit(self.back_button,
                             (self.back_button_x, self.back_button_y))

            return

        # In main menu
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

    # Click item
    def menu_option_click(self):
        if not self.in_options:
            if self.selected == 0:
                return 0, False
            elif self.selected == 1:
                return 1, False
            elif self.selected == 2:
                self.in_options = True
                return 2, False
            elif self.selected == 3:
                return 3, False
        else:
            if self.selected == 0:
                return 0, True
            elif self.selected == 1:
                return 1, True
            elif self.selected == 2:
                self.in_options = False
                return 2, True
