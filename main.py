import pygame
import random
import time

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

<<<<<<< HEAD
widht = 2
pygame.draw.line(screen, purple, (630, 470), (10, 470), widht)
pygame.draw.line(screen, purple, (10, 470), (10, 10), widht)
pygame.draw.line(screen, purple, (630, 470), (630, 10), widht)
pygame.draw.line(screen, purple, (630, 10), (10, 10), widht)
=======
widht = 11
pygame.draw.line(screen, purple, (640, 480), (0, 480), widht)
pygame.draw.line(screen, purple, (0, 480), (0, 0), widht)
pygame.draw.line(screen, purple, (640, 480), (640, 0), widht)
pygame.draw.line(screen, purple, (640, 0), (0, 0), widht)


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
>>>>>>> a425d48168da672783db49f8731e61d3afcc8e9c

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

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0)
    foody = round(random.randrange(0, screen_width - snake_block) / 10.0)

    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
<<<<<<< HEAD
        game_close = True    


=======
        game_close = True
>>>>>>> a425d48168da672783db49f8731e61d3afcc8e9c
