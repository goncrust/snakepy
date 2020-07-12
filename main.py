import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

running = True

iconsnake = pygame.image.load("images/snake_icon1.png")
pygame.display.set_caption("Snake")
pygame.display.set_icon(iconsnake)
pygame.mixer.music.load("soundtrack/track 1.mp3")
pygame.mixer.music.play()

blue=(0,0,255)
red=(255,0,0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen,red,[200,150,10,10])
    pygame.display.flip()
