import pygame, sys 

pygame.init()



block_size = 30

screen = pygame.display.set_mode((block_size * 20,block_size * 10))
clock = pygame.time.Clock()



surface = pygame.Surface((100,100))
xpos = 200
ypos = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((66,123,123))

    xpos += 1
    ypos -= 1 
    screen.blit(surface, (xpos,ypos))
    
    pygame.display.update()
    clock.tick(60)