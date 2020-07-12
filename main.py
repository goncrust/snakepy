import pygame
import random
import time

# Init pygame
pygame.init()

# Create screen
screen_width = 640
screen_height = 480
snake_block = 10
screen = pygame.display.set_mode((screen_width, screen_height))

# RUNNING VARIABLE
RUNNING = True

# Load images
iconsnake = pygame.image.load("images/snake_icon1.png")

# Configure window
pygame.display.set_caption("Snake")
pygame.display.set_icon(iconsnake)

# Setup music
pygame.mixer.music.load("soundtrack/Prof Oak.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

# Borders
lineWidht = 11
pygame.draw.line(screen, purple, (screen_width,
                                  screen_height), (0, screen_height), widht)
pygame.draw.line(screen, purple, (0, screen_height), (0, 0), widht)
pygame.draw.line(screen, purple, (screen_width,
                                  screen_height), (screen_width, 0), widht)
pygame.draw.line(screen, purple, (screen_width, 0), (0, 0), widht)


# Snake position and movement
x = random.randint(0, 427)
y = random.randint(0, 320)
direction = 0  # 0 - horizontal direita 1 - vertical baixo 2 - horizontal esquerda 3 - vertical cima
speed = 4

# FPS
fps = 60
clock = pygame.time.Clock()

# RUNNING LOOP
while RUNNING:

    # FPS
    clock.tick(60)

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # --------------- GameLoop -------------------

    # Clear Screen
    screen.fill((0, 0, 0))

    # Move Snake
    if direction == 0:
        x += speed

    # Draw Snake
    pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])

    # Update Screen
    pygame.display.flip()
