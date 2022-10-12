import pygame
from utils.Utils import load_image

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("ball.png")
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.speed = 7
        self.vector = (0.5,self.speed)
        self.hit = False
