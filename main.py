import pygame
import random
import time

# Init pygame
pygame.init()

# Create screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


# RUNNING VARIABLE
RUNNING = True

# Load images
iconsnake = pygame.image.load("images/snake_icon1.png")

# Configure window
pygame.display.set_caption("Snake")
pygame.display.set_icon(iconsnake)

# Border variables
screenDistance = 10
borderWidht = 2
# Setup music
pygame.mixer.music.load("soundtrack/Prof Oak.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

# Snake position and movement
snake_block = 10
x = random.randint(screenDistance + borderWidht,
                   (screen_width - screenDistance - borderWidht)/2)
y = random.randint(screenDistance + borderWidht,
                   (screen_height - screenDistance - borderWidht)/2)
direction = 0  # 0 - horizontal direita 1 - vertical baixo 2 - horizontal esquerda 3 - vertical cima
speed = 4

# Food
food_block = 10
fx = 0
fy = 0


def generateFood():
    global fx
    global fy
    fx = random.randint(screenDistance + borderWidht,
                        screen_width - screenDistance - borderWidht)
    fy = random.randint(screenDistance + borderWidht,
                        screen_height - screenDistance - borderWidht)


generateFood()

# FPS
fps = 60
clock = pygame.time.Clock()


# RUNNING LOOP
while RUNNING:

    # FPS
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 3
            if event.key == pygame.K_DOWN:
                direction = 1
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 2


    # --------------- GameLoop -------------------

    # Clear Screen
    screen.fill((0, 0, 0))

    # Borders
    pygame.draw.line(screen, purple, (screen_width - screenDistance,
                                      screen_height - screenDistance), (screenDistance, screen_height - screenDistance), borderWidht)
    pygame.draw.line(screen, purple, (screenDistance, screen_height - screenDistance),
                     (screenDistance, screenDistance), borderWidht)
    pygame.draw.line(screen, purple, (screen_width - screenDistance,
                                      screen_height - screenDistance), (screen_width - screenDistance, screenDistance), borderWidht)
    pygame.draw.line(screen, purple, (screen_width - screenDistance, screenDistance),
                     (screenDistance, screenDistance), borderWidht)

    # Move Snake
    if direction == 0:
        x += speed
    elif direction == 1:
        y += speed
    elif direction == 2:
        x -= speed
    elif direction == 3:
        y -= speed

    # Kill Snake
    if x >= screen_width - screenDistance - borderWidht or x <= screenDistance + borderWidht or y >= screen_height - screenDistance - borderWidht or y <= screenDistance - borderWidht:
        RUNNING = False
        continue
    
    # Draw Snake
    pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])

    # Draw food
    pygame.draw.rect(screen, red, [fx, fy, food_block, food_block])

    # Update Screen
    pygame.display.flip()


