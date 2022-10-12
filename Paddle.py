import pygame
from utils.Utils import load_image

class Paddle(pygame.sprite.Sprite):

    def __init__(self,side):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("paddle.png")
        screen =pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 5
        self.state = "still"
        self.reposition()

    def reposition(self):
        self.position = (0,0)
        if self.side == "left":
            self.rect.center = (50,self.area.centery)
        else:
            self.rect.center = (self.area.width - 50, self.area.centery)

    def move_up(self):
        self.position = (self.position[0],self.position[1]  - self.speed)

    def move_down(self):
        self.position = (self.position[0] , self.position[1]+ self.speed)

    def update(self):
        new_position = self.rect.move(self.position)
        if self.area.contains(new_position):
            self.rect = new_position
        pygame.event.pump()