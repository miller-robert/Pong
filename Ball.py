import pygame,math,random
from utils.Utils import load_image


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("ball.png")
        self.screen = pygame.display.get_surface()
        self.rect.x = (self.screen.get_width()/2)
        self.rect.y = (self.screen.get_height()/2)
        self.area = self.screen.get_rect()
        self.speed = 4
        self.vector = (random.random(),self.speed)
        self.hit = False

    def restart(self):
        self.rect.x = (self.screen.get_width()/2)
        self.rect.y = (self.screen.get_height()/2)
        self.area = self.screen.get_rect()
        self.speed = 4
        self.vector = (random.random(),self.speed)
        self.hit = False

    def update(self, left,right):
        new_position = self.calculate_new_position(self.rect,self.vector)
        self.rect = new_position
        angle,speed = self.vector

        #Check to see if the new position is outside of the area (Screen)
        if not self.area.contains(new_position):
            top_left = not self.area.collidepoint(new_position.topleft)
            top_right = not self.area.collidepoint(new_position.topright)
            bottom_left = not self.area.collidepoint(new_position.bottomleft)
            bottom_right = not self.area.collidepoint(new_position.bottomright)

            #if top of ball is above the area or bottom of ball is below the area
            if top_left and top_right or (bottom_left and bottom_right):
                angle = -angle

            #If the ball is past the left side
            if top_left and bottom_left:
                #angle = math.pi - angle
                self.restart()
                return "score_right"

            #if ball is past the right side
            if top_right and bottom_right:
                #angle = math.pi - angle
                self.restart()
                return "score_left"
        else:
            #ball is still in the bounds of the screen
            
            #check for collision with either paddles
            if  self.rect.colliderect(left.rect) == 1 and not self.hit:
                angle = math.pi - angle
                self.hit = not self.hit
            elif  self.rect.colliderect(right.rect) == 1 and not self.hit:
                angle= math.pi - angle
                self.hit = not self.hit
            elif self.hit:
                self.hit = not self.hit
            
        self.vector = (angle,speed)
            

    


    def calculate_new_position(self,rect,vector):
        #Speed is essentially the length of the vector in pixels
        angle,speed = vector
        dx,dy = (speed*math.cos(angle),speed*math.sin(angle))
        return rect.move(dx,dy)