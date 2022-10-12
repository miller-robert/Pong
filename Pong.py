from turtle import back
from Ball import Ball
from Paddle import Paddle


try:
    import pygame
except Exception as e:
    print(e)



def run():
    pygame.init()
    global left,right

    #Initialise the screen
    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pong Remake")

    #Initialise the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    #Initialise Players
    left = Paddle("left")
    right = Paddle("right")



    #Initialise ball
    ball = Ball()

    #Initialise sprite groups
    paddle_sprites = pygame.sprite.RenderPlain(left,right)
    ball_sprite = pygame.sprite.RenderPlain(ball)

    #Blit everythign to screen
    screen.blit(background,(0,0))
    pygame.display.flip()

    #initialise clock
    clock = pygame.time.Clock()

    #Main game loop
    is_running = True
    while is_running:
        #Render 60fps
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    left.move_up()
                if event.key == pygame.K_s:
                    left.move_down()
                if event.key == pygame.K_UP:
                    right.move_up()
                if event.key == pygame.K_DOWN:
                    right.move_down()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    left.position = (0,0)
                if event.key == pygame.K_s:
                    left.position = (0,0)
                if event.key == pygame.K_UP:
                    right.position = (0,0)
                if event.key == pygame.K_DOWN:
                    right.position = (0,0)


        #update screen
        screen.blit(background,ball.rect,ball.rect)
        screen.blit(background,left.rect,left.rect)
        screen.blit(background,right.rect,right.rect)
        ball_sprite.update(left,right)
        paddle_sprites.update()
        ball_sprite.draw(screen)
        paddle_sprites.draw(screen)
        pygame.display.flip()





if __name__ == "__main__": run()