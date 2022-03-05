import pygame,sys

pygame.init()
pygame.display.set_caption('Pong Game by github.com/8uziak')

Widgh, Height = 400, 300

screen = pygame.display.set_mode((Widgh,Height))
clock = pygame.time.Clock()

fps = 60 

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 200)

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

plate_wh, plate_ht = 10, 40 #paddle's width and height


class LeftPlate:

    #beginning positions for x and y
    x_og = 1 
    y_og = 1 

    def __init__(self):

        self.x_pos = self.x_og 
        self.y_pos = self.y_og

        self.body = (1,2,plate_wh,plate_ht)
        self.move = False
    
    def draw(self):
        pygame.draw.rect(screen,white,self.body)

    def move_plate(self):
        if self.move == True:
            self.x_pos -= self.VEL 
        else:
            None

    def reset(self):
        self.x_pos = self.x_og 
        self.y_pos = self.y_og
        

# right plate is operated by a human with arrow keys
class RightPlate:

    #beginning positions for x and y
    x_og = 1 
    y_og = 1 

    def __init__(self):

        self.x_pos = self.x_og 
        self.y_pos = self.y_og

        self.body = (1,2,plate_wh,plate_ht)
        self.move = False
    
    def draw(self):
        pygame.draw.rect(screen,white,self.body)

    def move_plate(self):
        if self.move == True:
            self.x_pos -= self.VEL 
        else:
            None

    def reset(self):
        self.x_pos = self.x_og 
        self.y_pos = self.y_og
        


class Main:
    def __init__(self):
        
        self.game_on = True



        while self.game_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == screen_update:
                    self.update()        
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        None
        
                    if event.key == pygame.K_DOWN:
                        None
            
            pygame.display.update()
            clock.tick(fps)

    def update(self):
        None

    def quit(self):
        self.game_on = False
        pygame.quit()
        sys.exit()
        


if __name__ == "__main__":
    Main()
