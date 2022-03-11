import pygame,sys

pygame.init()
pygame.display.set_caption('Pong Game')

widgh, height = 400, 300

screen = pygame.display.set_mode((widgh,height))
clock = pygame.time.Clock()

fps = 60 

radius = 6

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 200)

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

plate_wh, plate_ht = 10, 40 #paddle's width and height



class PongPlateArrows():
    def __init__(self):

        self.widgh = widgh - 20
        self.height = height / 2 - 70

        self.plate_wh = plate_wh
        self.plate_ht = plate_ht
      
    
    def draw_plate(self):
        self.plate = pygame.Rect(self.widgh, self.height, self.plate_wh,self.plate_ht)
        pygame.draw.rect(screen,white,self.plate)
    



class PongPlateWSAD():
    def __init__(self):

        self.widgh = 20
        self.height = height / 2 - 70

        self.plate_wh = plate_wh
        self.plate_ht = plate_ht
    
    def draw_plate(self):
        self.plate = pygame.Rect(self.widgh, self.height, self.plate_wh,self.plate_ht)
        pygame.draw.rect(screen,white,self.plate)

    def reset(self):
        self.widgh = 20
        self.height = height / 2 - 70

class Ball():
    def __init__(self):

        self.widgh = widgh / 2
        self.height = height / 2

        self.radius = radius

    def draw_ball(self):
        pygame.draw.circle(screen,white,(self.widgh,self.height),self.radius)
        

class Main():


    def __init__(self):
        
        self.pongplate2 = PongPlateArrows()
        self.pongplate1 = PongPlateWSAD()
        self.ball = Ball()

        game_on = True
        while game_on:
            self.whileloop()
    
    def whileloop(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end_game()
            if event.type == screen_update:
                self.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.pongplate2.height != 0:
                        self.pongplate2.height -= 5
    
                if event.key == pygame.K_DOWN:
                    if self.pongplate2.height != height - plate_ht: 
                        self.pongplate2.height += 5

                if event.key == pygame.K_w:
                    if self.pongplate1.height != 0:
                        self.pongplate1.height -= 5
    
                if event.key == pygame.K_s:
                    if self.pongplate1.height != height - plate_ht: 
                        self.pongplate1.height += 5
    
    
            self.place_elements()
            pygame.display.update()
            clock.tick(fps) # FPS = 60

    
    def update(self):
        None

    def place_elements(self):
        self.background()
        self.pongplate2.draw_plate()
        self.pongplate1.draw_plate()
        self.ball.draw_ball()
    
    def check_collision(self):
        None
    
    def background(self):
        screen.fill(black)

    def score(self):
        None
    
    def end_game(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Main()