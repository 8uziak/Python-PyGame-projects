
import pygame, sys, random
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(5,5),Vector2(4,5),Vector2(3,5)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def place_snake(self):
        for index, block in enumerate(self.body):
            x_pos = int(block.x * block_size)
            y_pos = int(block.y * block_size)
            block_rect = pygame.Rect(x_pos,y_pos,block_size,block_size)
            
            if index == 0: 
                screen.blit(head,block_rect)
            
            else:
                screen.blit(body,block_rect)
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False

        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy


    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5,5),Vector2(4,5),Vector2(3,5)]
        self.direction = Vector2(1,0)

class Fruit: 
    def __init__(self):
        self.randomize()

    def place_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * block_size),int(self.pos.y * block_size),block_size, block_size)
        screen.blit(apple,fruit_rect)

    def randomize(self):
        self.x = random.randint(0,20-1)
        self.y = random.randint(0,10-1)
        self.pos = Vector2(self.x,self.y)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_game_over()

    def place_elements(self):
        self.place_grass()
        self.snake.place_snake()
        self.fruit.place_fruit()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def place_grass(self):

        for row in range(10):
            for col in range(20):
                grass_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                screen.blit(grass,grass_rect)

    def check_game_over(self):
        if not 0 <= self.snake.body[0].x < 20 or not 0 <= self.snake.body[0].y < 10:
            self.snake.reset()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.snake.reset()

    def end_game(self):
        pygame.quit()
        sys.exit()

# set up pygame
pygame.init()
pygame.display.set_caption('Snake by github.com/8uziak')

# length of each side of a square (20 horizontally and 10 vertically)
block_size = 20

#importing grafics 
apple = pygame.image.load('Snake-old-Nokia-version/apple.png')
apple = pygame.transform.scale(apple, (20,20))

head = pygame.image.load('Snake-old-Nokia-version/head.png')
head = pygame.transform.scale(head, (20,20))

body = pygame.image.load('Snake-old-Nokia-version/body.png')
body = pygame.transform.scale(body, (20,20))

grass = pygame.image.load('Snake-old-Nokia-version/grass.png')
grass = pygame.transform.scale(grass, (20,20))

screen = pygame.display.set_mode((block_size * 20,block_size * 10))
clock = pygame.time.Clock()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)


main = Main()
game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.end_game()
        if event.type == screen_update:
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.snake.direction.y != 1:
                    main.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                if main.snake.direction.x != -1:
                    main.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main.snake.direction.x != 1:
                    main.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_DOWN:
                if main.snake.direction.y != -1:
                    main.snake.direction = Vector2(0, 1)

    main.place_elements()
    pygame.display.update()
    clock.tick(60)