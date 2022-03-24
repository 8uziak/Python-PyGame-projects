import pygame, sys 

pygame.init()
pygame.display.set_caption('Aim It Game')

width, height = 400, 400


screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

fps = 60 

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 200)

black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screen_update: # just XD i need a break fr 
            None
        if event.type == pygame.KEYDOWN: #press mouse button
            None
        

    pygame.display.update()
    clock.tick(fps) # FPS = 60
               