import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

fps = 60
clock = pygame.time.Clock()

blue  = (0, 0, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((400,600))
screen.fill(white)
pygame.display.set_caption("Game")

sWidth = 400
sHeight = 600
speed = 5
score = 0
coinScore = 0
lastCoinScore = 0

font = pygame.font.SysFont("Verdana", 60)
fontSmall = pygame.font.SysFont("Verdana", 20)
gameOver = font.render("Game Over", True, black)


bg = pygame.image.load('AnimatedStreet.png')

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, sWidth-40),0)
    
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom>600:
            score+=1
            self.rect.top = 0
            self.rect.center = (random.randint(40, sWidth-40), 0)
            

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left>0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        
        if self.rect.right<sWidth:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)
                
                
class Coin(pygame.sprite.Sprite):    # creating class Coin as an Enemy class
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 450)
        
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom>600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, sWidth-40), 0)
            
    def collide(self):                                   #function for collision
        self.top = 0
        self.rect.center = (random.randint(30, 350), 0)
                

        
p1 = Player()
e1 = Enemy()
c1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(e1)
coins = pygame.sprite.Group()
coins.add(c1)
allSprites = pygame.sprite.Group()
allSprites.add(e1)
allSprites.add(p1)
allSprites.add(c1)

incSpeed = pygame.USEREVENT + 1
pygame.time.set_timer(incSpeed, 5000)


while True:
    for event in pygame.event.get():
        if event.type == incSpeed:
            speed+=0.5
    
        if event.type == QUIT:
            pygame.quit()
            sys.exit
            
    screen.fill(white)
    
    if coinScore-lastCoinScore>=20:                  #Increase speed of enemy every 20 coins
        speed+=0.5
        print("ASFASFASF")
        lastCoinScore = coinScore
    
    screen.blit(bg, (0,0))
    scores = fontSmall.render(str(score), True, black)
    coinScores = fontSmall.render(str(coinScore), True, black)
    screen.blit(scores, (10,10))
    screen.blit(coinScores, (sWidth-30,10))
    
    for entity in allSprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
        
        
    
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        
        
        screen.fill(red)
        screen.blit(gameOver, (30,250))
        
        pygame.display.update()
        for entity in allSprites:
            entity.kill() 
        time.sleep(2)
        
        pygame.quit()
        sys.exit()        
         
        
    if pygame.sprite.spritecollideany(p1, coins):        #collision with coins
        coinScore+=random.randint(1,3)                   #random weight of coins
        pygame.mixer.Sound('collect.mp3').play()         #play sound when collecting coin
        c1.collide()
        
        
        
        
            
    pygame.display.flip()
    clock.tick(fps)
