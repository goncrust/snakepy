import pygame
import random
import time
import menu
from Images.imageLoader import *

# Init pygame
pygame.init()

# Create screen
# default = 640x480
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Create menu
menu = menu.Menu(screen)

# RUNNING AND GAMEOVER VARIABLE
RUNNING = True
GAMEOVER = False

# Images
gameover = pygame.transform.scale(gameover, (screen_width, screen_height))
gameoverrect = gameover.get_rect()

# Configure window
pygame.display.set_caption("Snake | Points 0")
pygame.display.set_icon(iconsnake)

# Border variables
screenDistance = 5
borderWidht = 5

# Setup music
pygame.mixer.music.load("soundtrack/Prof Oak.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

# Collision Function


def collision(px, py, ox, oy, object_width, object_height, player_width, player_height):
    if (px < ox + object_width and px >= ox and py >= oy and py < oy + object_height) or (px + player_width > ox and px + player_width < ox + object_width and py + player_height < oy + object_height and py + player_height > oy) or (px < ox + object_width and px >= ox and py + player_height < oy + object_height and py + player_height > oy) or (px + player_width > ox and px + player_width < ox + object_width and py >= oy and py < oy + object_height):
        return True
    else:
        return False


# Snake position and movement
snake = []
snake_block = 10
x = random.randrange(screenDistance + borderWidht + 20,
                     (screen_width - screenDistance - borderWidht - snake_block)/2, 10)
y = random.randrange(screenDistance + borderWidht + 20,
                     (screen_height - screenDistance - borderWidht - snake_block)/2, 10)

snake.append([x, y])
snake.append([x - 10, y])
snake.append([x - 20, y])
directions = [0, 0, 0]
# direction = 0  # 0 - horizontal direita 1 - vertical baixo 2 - horizontal esquerda 3 - vertical cima
speed = 10

# Food
food_block = 10
fx = 0
fy = 0


def generateFood():
    global fx
    global fy
    fx = random.randrange(screenDistance + borderWidht,
                          screen_width - screenDistance - borderWidht - food_block, 10)
    fy = random.randrange(screenDistance + borderWidht,
                          screen_height - screenDistance - borderWidht - food_block, 10)

    for s in snake:
        if (collision(s[0], s[1], fx, fy, food_block, food_block, snake_block, snake_block)):
            generateFood()


generateFood()

# Points
points = 0

# FPS
difficulty = 5
clock = pygame.time.Clock()


# RUNNING LOOP
while RUNNING:

    # FPS
    clock.tick(difficulty)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if directions[0] != 1:
                    directions[0] = 3
            if event.key == pygame.K_DOWN:
                if directions[0] != 3:
                    directions[0] = 1
            if event.key == pygame.K_RIGHT:
                if directions[0] != 2:
                    directions[0] = 0
            if event.key == pygame.K_LEFT:
                if directions[0] != 0:
                    directions[0] = 2
            if event.key == pygame.K_p:
                print("pause")

    # --------------- GameLoop -------------------

    # Clear Screen
    screen.fill((0, 0, 0))

    # Menu
    mosX, mosY = pygame.mouse.get_pos()
    menu.selectbutton(mosX, mosY)
    menu.menuScreen()
    
    

    # Borders
    pygame.draw.rect(screen, purple, [
                     screenDistance, screenDistance, screen_width - screenDistance*2, borderWidht])
    pygame.draw.rect(screen, purple, [
                     screenDistance, screenDistance, borderWidht, screen_height - screenDistance*2])
    pygame.draw.rect(screen, purple, [
                     screenDistance, screen_height - screenDistance - borderWidht, screen_width - screenDistance*2, borderWidht])
    pygame.draw.rect(screen, purple, [
                     screen_width - screenDistance - borderWidht, screenDistance, borderWidht, screen_height - screenDistance*2])

    # Move Snake
    index = 0
    for s in snake:
        if directions[index] == 0:
            s[0] += speed
        elif directions[index] == 1:
            s[1] += speed
        elif directions[index] == 2:
            s[0] -= speed
        elif directions[index] == 3:
            s[1] -= speed

        index += 1

    # Kill Snake
    if (snake[0][0] > screen_width - screenDistance - borderWidht - snake_block) or (snake[0][0] < screenDistance + borderWidht) or (snake[0][1] > screen_height - screenDistance - borderWidht - snake_block) or (snake[0][1] < screenDistance + borderWidht):
        # RUNNING = False
        GAMEOVER = True

    if (GAMEOVER):
        screen.fill((0, 0, 0))
        screen.blit(gameover, (0, 0))
        pygame.display.flip()
        continue

    # Snake eat apple
    if collision(snake[0][0], snake[0][1], fx, fy, food_block, food_block, snake_block, snake_block):
        # Generate new food
        generateFood()

        # Add points
        points += 1
        pygame.display.set_caption("Snake | Points " + str(points))

        # Append snake
        if directions[len(directions) - 1] == 0:
            snake.append([int(snake[len(snake) - 1][0]) - 10,
                          int(snake[len(snake) - 1][1])])
        elif directions[len(directions) - 1] == 1:
            snake.append([int(snake[len(snake) - 1][0]),
                          int(snake[len(snake) - 1][1]) - 10])
        elif directions[len(directions) - 1] == 2:
            snake.append([int(snake[len(snake) - 1][0]) + 10,
                          int(snake[len(snake) - 1][1])])
        elif directions[len(directions) - 1] == 3:
            snake.append([int(snake[len(snake) - 1][0]),
                          int(snake[len(snake) - 1][1]) + 10])

        directions.append(directions[len(directions) - 1])

    # Draw Snake
    for s in snake:
        pygame.draw.rect(
            screen, green, [s[0], s[1], snake_block, snake_block])

    # Draw food
    pygame.draw.rect(screen, red, [fx, fy, food_block, food_block])

    # Update directions
    indexDirections = len(directions) - 1
    while indexDirections != 0:
        directions[indexDirections] = directions[indexDirections - 1]
        indexDirections -= 1
    

    for s in range(1, len(snake)):
        if collision(snake[0][0], snake[0][1], snake[s][0], snake[s][1], snake_block, snake_block, snake_block, snake_block):
            GAMEOVER = True

    # Update Screen
    pygame.display.flip()
