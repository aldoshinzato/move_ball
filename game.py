import pygame


pygame.init()
velocidad= [1 , 1]

screen = pygame.display.set_mode((800,600))

# He cargado mi sprite en memoria
spr_ball = pygame.image.load("assets/soccer.png")
spr_ball= pygame.transform.scale(spr_ball,(64,64))
rect_ball= spr_ball.get_rect()

screen.fill((0,0,0))



# Game loop


endgame = False
while not endgame:
    #
    #Gestionar los eventos del usuario
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            endgame = True
            break

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect_ball= rect_ball.move([5,0])
            elif event.key== pygame.K_LEFT:
                rect_ball= rect_ball.move([-5,0])
            elif event.key == pygame.K_UP:
                rect_ball= rect_ball.move([0,-5])
            elif event.key== pygame.K_DOWN:
                rect_ball= rect_ball.move([0,5])
    #Actualizar los estados del juego





    #rect_ball = rect_ball.move(velocidad)
    # if rect_ball.y > 536:
    #     velocidad[1]= velocidad[1]*-1
    # if rect_ball.y <= 0:
    #     velocidad[1]= velocidad[1]*-1
    # if rect_ball.x > 736:
    #     velocidad[0]=velocidad[0]*-1
    # if rect_ball.x <=0:
    #     velocidad[0]= velocidad[0]*-1


 
    #renderizar la interfaz grafica


    screen.fill((0,0,0))
    screen.blit(spr_ball,rect_ball)
    pygame.display.update()
    pygame.display.flip()