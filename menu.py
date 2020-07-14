import pygame
from Images.imageLoader import *

def menuScreen(screen):
    screen.blit(playbutton, (75, 200))
    screen.blit(settingsbutton, (275, 200))
    screen.blit(exitbutton, (475, 200))

playbutton = pygame.transform.scale(playbutton, (100, 100))
settingsbutton = pygame.transform.scale(settingsbutton, (100, 100))
exitbutton = pygame.transform.scale(exitbutton, (100, 100))
    
