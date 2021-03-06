
import pygame, sys, random
from pygame.math import Vector2


# set up pygame
pygame.mixer.pre_init(44100,16,512)
pygame.mixer.init()
pygame.init()
pygame.display.set_caption('Snake Nokia 3310 by github.com/8uziak')
       
block_size = 20   # length of each side of a square (20 horizontally and 10 vertically)

#list
lis = []
for l in range(60):
    lis.append(l)
    

#importing grafics 
apple = pygame.image.load('Images/apple.png')
apple = pygame.transform.scale(apple, (20,20))

head_right = pygame.image.load('Images/head_right.png')
head_right = pygame.transform.scale(head_right, (20,20))

head_left = pygame.image.load('Images/head_left.png')
head_left = pygame.transform.scale(head_left, (20,20))

head_up = pygame.image.load('Images/head_up.png')
head_up = pygame.transform.scale(head_up, (20,20))

head_down = pygame.image.load('Images/head_down.png')
head_down = pygame.transform.scale(head_down, (20,20))

eat_right = pygame.image.load('Images/eat_right.png')
eat_right = pygame.transform.scale(eat_right, (20,20))

eat_left = pygame.image.load('Images/eat_right.png')
eat_right = pygame.transform.scale(eat_right, (20,20))

eat_up = pygame.image.load('Images/eat_up.png')
eat_up = pygame.transform.scale(eat_up, (20,20))

eat_down = pygame.image.load('Images/eat_down.png')
eat_down = pygame.transform.scale(eat_down, (20,20))

body_right = pygame.image.load('Images/body_right.png')
body_right  = pygame.transform.scale(body_right, (20,20))

body_left = pygame.image.load('Images/body_left.png')
body_left  = pygame.transform.scale(body_left, (20,20))

body_up = pygame.image.load('Images/body_up.png')
body_up = pygame.transform.scale(body_up, (20,20))

body_down = pygame.image.load('Images/body_down.png')
body_down  = pygame.transform.scale(body_down, (20,20))

area = pygame.image.load('Images/area.png')
area = pygame.transform.scale(area, (20,20))

area_up = pygame.image.load('Images/area_up.png')
area_up = pygame.transform.scale(area_up, (20,20))

area_right = pygame.image.load('Images/area_right.png')
area_right = pygame.transform.scale(area_right, (20,20))

area_left = pygame.image.load('Images/area_left.png')
area_left = pygame.transform.scale(area_left, (20,20))

area_down = pygame.image.load('Images/area_down.png')
area_down = pygame.transform.scale(area_down, (20,20))
###

# font for the score value
score_font = pygame.font.Font('Font/nokia3310.ttf', 100)

# window size
screen = pygame.display.set_mode((block_size * 60,block_size * 40))
clock = pygame.time.Clock()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

class Snake:
    def __init__(self):
        self.body = [Vector2(30,24),Vector2(29,24),Vector2(28,24)]
        self.direction = Vector2(1,0)
        self.new_block = False
        self.head = head_right

        self.eat_sound = pygame.mixer.Sound('Sounds/sound_1.wav')

    def place_snake(self):
        self.update_head_grafics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * block_size)
            y_pos = int(block.y * block_size)
            block_rect = pygame.Rect(x_pos,y_pos,block_size,block_size)
            
            if index == 0: 
                screen.blit(self.head,block_rect)
            
            else:
                previous_block = self.body[index] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x and next_block.y - previous_block.y == 1:
                    screen.blit(body_down,block_rect)

                elif previous_block.x == next_block.x and next_block.y - previous_block.y == -1:
                    screen.blit(body_up,block_rect)
                
                elif previous_block.y == next_block.y and next_block.x - previous_block.x == 1:
                    screen.blit(body_right,block_rect)
                
                elif previous_block.y == next_block.y and next_block.x - previous_block.x == -1:
                    screen.blit(body_left,block_rect)

    def update_head_grafics(self):
        head_rotation = self.body[1] - self.body[0]
        if head_rotation == Vector2(1,0):
            self.head = head_left

        elif head_rotation == Vector2(-1,0):
            self.head = head_right

        elif head_rotation == Vector2(0,1):
            self.head = head_up

        elif head_rotation == Vector2(0,-1):
            self.head = head_down


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

    def play_eat_sound(self):
        self.eat_sound.play()

    def reset(self):
        self.body = [Vector2(30,24),Vector2(29,24),Vector2(28,24)]
        self.direction = Vector2(1,0)

class Fruit: 
    def __init__(self):
        self.randomize()

    def place_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * block_size),int(self.pos.y * block_size),block_size, block_size)
        screen.blit(apple,fruit_rect)

    def randomize(self):
        self.x = random.randint(2,58-1)
        self.y = random.randint(11,38-1)
        self.pos = Vector2(self.x,self.y)


class Main:
    def __init__(self):

        self.snake = Snake()
        self.fruit = Fruit()

        self.game_on = True
        while self.game_on:
            self.whileloop()

        
    
    def whileloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end_game()
            if event.type == screen_update:
                self.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.snake.direction.y != 1:
                        self.snake.direction = Vector2(0,-1)

                if event.key == pygame.K_RIGHT:
                    if self.snake.direction.x != -1:
                        self.snake.direction = Vector2(1, 0)
    
                if event.key == pygame.K_LEFT:
                    if self.snake.direction.x != 1:
                        self.snake.direction = Vector2(-1, 0)
    
                if event.key == pygame.K_DOWN:
                    if self.snake.direction.y != -1:
                        self.snake.direction = Vector2(0, 1)

        self.place_elements()
        pygame.display.update()
        clock.tick(60)

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_game_over()
    
    def place_elements(self):
        self.place_grass()
        self.snake.place_snake()
        self.fruit.place_fruit()
        self.score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_eat_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    # background for the game
    def place_grass(self):

        for row in range(40):
            for col in range(60):
                if row == 10 and col in lis[2:58]:
                        
                    area_down_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                    screen.blit(area_down,area_down_rect)

                elif row == 38 and col in lis[2:58]:
                    area_up_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                    screen.blit(area_up,area_up_rect)
                
            
                elif row in lis[11:38] and col == 1:
                        area_right_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                        screen.blit(area_right,area_right_rect)


                elif row in lis[11:38] and col == 58:
                        area_left_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                        screen.blit(area_left,area_left_rect)
                
                elif row == 7 and col in lis[2:58]:
                        
                    area_down_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                    screen.blit(area_down,area_down_rect)


                elif row == 8 and col in lis[2:58]:
                    area_up_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                    screen.blit(area_up,area_up_rect)
                        
                else:
                    area_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                    screen.blit(area,area_rect)


    def check_game_over(self):
        if not 2 <= self.snake.body[0].x < 58 or not 11 <= self.snake.body[0].y < 38:
            self.snake.reset()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.snake.reset()
    
    def score(self):
        score = str((len(self.snake.body) - 3) * 10)
        if len(score) <= 1: 
            x_score = '0000'
        elif len(score) == 2: 
            x_score = '00' + score
        elif len(score) == 3:
            x_score = '0' + score
        elif len(score) >= 4:
            x_score = score
        
        score_render = score_font.render(x_score, True,(0,0,0))
        score_rect = score_render.get_rect(center = (200, 100))
        screen.blit(score_render,score_rect)            

    def snake_eat_animation(self):
        if self.fruit.pos - self.snake.body[0] == Vector2(1,0):
            None

    def end_game(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    Main()