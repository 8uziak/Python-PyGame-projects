import pygame,sys
from pygame.math import Vector2

class FirstPlate:
    def __init__(self):
        self.body = [Vector2(3,7),Vector2(3,8),Vector2(3,9),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.delate_block_up = False
        self.delate_block_down = False
        

    def place_pong_1(self):
        for block in self.body:
            x_pos = 3 * block_size
            y_pos = int(block.y * block_size)
            body_rect = pygame.Rect(x_pos,y_pos,block_size,block_size)
            screen.fill(white,body_rect)

    def move_pong_1(self):
        if self.delate_block_up == True:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy
            self.direction = Vector2(0,0)
            self.delate_block_up = False

        elif self.delate_block_down == True:
            body_copy = [Vector2(0,self.body[-1][1] + self.direction.y)]
            body_copy.append(self.body[1:])
            self.body = body_copy
            self.direction = Vector2(0,0)
            self.delate_block_down = False

        print(self.body)

class SecondPlate:
    def __init__(self):
        self.body = None


class Ball:
    def __init__(self):
        self.body = None


class Main:
    def __init__(self):
        self.pong1 = FirstPlate()
        self.pong2 = SecondPlate()
        self.ball = Ball()
        
    def update(self):
        self.pong1.move_pong_1()

    def place_elements(self):
        self.place_backgroud()
        self.pong1.place_pong_1()

    def place_backgroud(self):
        for row in range(height):
            for col in range(width):
                if row == 3 and col in range(3,width-3) :
                    white_area_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                    screen.fill(white,white_area_rect)
                
                elif row in range(4,height - 4) and col == 15:
                    white_area_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                    screen.fill(white,white_area_rect)
                
                elif row == (height - 4) and col in range(3,width-3) :
                    white_area_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                    screen.fill(white,white_area_rect) 
                else:
                    black_area_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                    screen.fill(black,black_area_rect)

    def quit():
        pygame.quit()            
        sys.exit()

pygame.init()
pygame.display.set_caption('Pong Game by github.com/8uziak')

block_size = 18
width = 31
height = 21

# colors <3
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

# window size
screen = pygame.display.set_mode((block_size * width,block_size * height))
clock = pygame.time.Clock()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 200)

main = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.quit()

        if event.type == screen_update:
            main.update()        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main.pong1.delate_block_up = True
                main.pong1.direction = Vector2(0,-1)
 
            if event.key == pygame.K_DOWN:
                main.pong1.delate_block_down = True
                main.pong1.direction = Vector2(0, 1)

    main.place_elements()
    pygame.display.update()
    clock.tick(60)