import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((640, 480))

RUNNING = True

iconsnake = pygame.image.load("images/snake_icon1.png")
pygame.display.set_caption("Snake")
pygame.display.set_icon(iconsnake)
pygame.mixer.music.load("soundtrack/Prof Oak.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# position
x = random.randint(0, 427)
y = random.randint(0, 320)
pygame.draw.rect(screen, green, [x, y, 10, 10])

# movement
direction = 0  # 0 - horizontal direita 1 - vertical baixo 2 - horizontal esquerda 3 - vertical cima
speed = 4

# fps
fps = 60
clock = pygame.time.Clock()

while RUNNING:

    clock.tick(60)

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # GameLoop
    # Clear Screen
    screen.fill((0, 0, 0))

    if direction == 0:
        x += speed

    pygame.draw.rect(screen, green, [x, y, 10, 10])

    pygame.display.flip()
