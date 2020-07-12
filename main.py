import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen_width = 640
screen_height = 480
snake_block = 10

RUNNING = True

iconsnake = pygame.image.load("images/snake_icon1.png")
pygame.display.set_caption("Snake")
pygame.display.set_icon(iconsnake)
pygame.mixer.music.load("soundtrack/Prof Oak.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.0)


for event in pygame.event.get():
    if event.type == KEYDOWN or event.type == KEYUP:
        

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

widht = 2
pygame.draw.line(screen, purple, (630, 470), (10, 470), widht)
pygame.draw.line(screen, purple, (10, 470), (10, 10), widht)
pygame.draw.line(screen, purple, (630, 470), (630, 10), widht)
pygame.draw.line(screen, purple, (630, 10), (10, 10), widht)

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    pygame.draw.rect(screen, red, [200, 150, 10, 10])
    pygame.display.flip()

    x1 = screen_width / 2
    y1 = screen_height / 2
    
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, screen_width - snake_block) /10.0)
    foody = round(random.randrange(0, screen_width - snake_block) /10.0)

    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_close = True    


