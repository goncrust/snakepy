import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

RUNNING = True

def move(self):
    self.rect.top -= self.speed

iconsnake = pygame.image.load("images/snake_icon1.png")
pygame.display.set_caption("Snake")
pygame.display.set_icon(iconsnake)
pygame.mixer.music.load("soundtrack/Prof Oak.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    pygame.draw.rect(screen, red, [200, 150, 10, 10])
    pygame.display.flip()
