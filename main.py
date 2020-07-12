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
