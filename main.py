import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

RUNNING = True

iconsnake = pygame.image.load("images/snake_icon1.png")
pygame.display.set_caption("Snake")
pygame.display.set_icon(iconsnake)
pygame.mixer.music.load("soundtrack/Prof Oak.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

widht = 11
pygame.draw.line(screen, purple, (640, 480), (0, 480), widht)
pygame.draw.line(screen, purple, (0, 480), (0, 0), widht)
pygame.draw.line(screen, purple, (640, 480), (640, 0), widht)
pygame.draw.line(screen, purple, (640, 0), (0, 0), widht)



while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    pygame.draw.rect(screen, red, [200, 150, 10, 10])
    pygame.display.flip()

def gameLoop(): # creating a function
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_heigth / 2
    
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) /10.0)
    foody = round(random.randrange(0, dis_width - snake_block) /10.0)

    if x1 >= dis_width or x1 < 0 or y1 >= dis_heigth or y1 < 0:
        game_close = True    
    