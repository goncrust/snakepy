import pygame
import random
import time
import menu
from images.image_loader import *

# Init pygame
pygame.init()

# Create screen
# default = 640x480
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Create menu
menu = menu.Menu(screen)
in_menu = True
click = False

# RUNNING AND GAMEOVER VARIABLE
RUNNING = True
GAMEOVER = False

# Images
gameover = pygame.transform.scale(gameover, (screen_width, screen_height))

# Configure window
pygame.display.set_caption("Snake | Points 0")
pygame.display.set_icon(snake_icon)

# Border variables
screen_distance = 5
border_width = 5

# Setup music
pygame.mixer.music.load("soundtrack/prof_oak.mp3")
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
x = random.randrange(screen_distance + border_width + 20,
                     (screen_width - screen_distance - border_width - snake_block)/2, 10)
y = random.randrange(screen_distance + border_width + 20,
                     (screen_height - screen_distance - border_width - snake_block)/2, 10)

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


def generate_food():
    global fx
    global fy
    fx = random.randrange(screen_distance + border_width,
                          screen_width - screen_distance - border_width - food_block, 10)
    fy = random.randrange(screen_distance + border_width,
                          screen_height - screen_distance - border_width - food_block, 10)

    for s in snake:
        if (collision(s[0], s[1], fx, fy, food_block, food_block, snake_block, snake_block)):
            generate_food()


generate_food()

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if in_menu:
                    click = True

    # --------------- GameLoop -------------------

    # Clear Screen
    screen.fill((0, 0, 0))

    # Menu
    if in_menu:
        mos_x, mos_y = pygame.mouse.get_pos()
        menu.select_button(mos_x, mos_y)
        if click:
            option = menu.menu_option()
            if option == 1:
                in_menu = False
            elif option == 2:
                in_menu = False
            elif option == 3:
                RUNNING = False
            click = False
        menu.menu_screen()
        pygame.display.flip()
        continue

    # Borders
    pygame.draw.rect(screen, purple, [
                     screen_distance, screen_distance, screen_width - screen_distance*2, border_width])
    pygame.draw.rect(screen, purple, [
                     screen_distance, screen_distance, border_width, screen_height - screen_distance*2])
    pygame.draw.rect(screen, purple, [
                     screen_distance, screen_height - screen_distance - border_width, screen_width - screen_distance*2, border_width])
    pygame.draw.rect(screen, purple, [
                     screen_width - screen_distance - border_width, screen_distance, border_width, screen_height - screen_distance*2])

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
    if (snake[0][0] > screen_width - screen_distance - border_width - snake_block) or (snake[0][0] < screen_distance + border_width) or (snake[0][1] > screen_height - screen_distance - border_width - snake_block) or (snake[0][1] < screen_distance + border_width):
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
        generate_food()

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
    index_directions = len(directions) - 1
    while index_directions != 0:
        directions[index_directions] = directions[index_directions - 1]
        index_directions -= 1

    for s in range(1, len(snake)):
        if collision(snake[0][0], snake[0][1], snake[s][0], snake[s][1], snake_block, snake_block, snake_block, snake_block):
            GAMEOVER = True

    # Update Screen
    pygame.display.flip()
