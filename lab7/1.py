import pygame
from datetime import datetime
import time

def getTime():
    now = datetime.now()
    minute = now.minute
    second = now.second
    return minute, second

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle+15*6)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect



pygame.init()
screen = pygame.display.set_mode((900,800), pygame.RESIZABLE)
exit = False

bg = pygame.transform.scale(pygame.image.load('main-clock.png'), (900, 800))
leftHand = pygame.image.load('left-hand.png')
rightHand = pygame.image.load('right-hand.png')

screen.fill((255,255,255))

x_sec, y_sec = 460, 400
x_min, y_min = 450, 385
screen.blit(leftHand, (0,0))
screen.blit(rightHand, (0,0))

clocka = pygame.time.Clock()

while not exit:
    clocka.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
    screen.blit(bg, (0,0))
    
    screen.blit(rot_center(leftHand, -getTime()[1]*6, x_sec, y_sec)[0], rot_center(leftHand, -getTime()[1] * 6, x_sec, y_sec)[1])
    
    screen.blit(rot_center(rightHand, -getTime()[0]*6, x_min, y_min)[0], rot_center(rightHand, -getTime()[0] * 6, x_min, y_min)[1])
    
    pygame.draw.circle(screen, (53, 54, 55), (450, 400), 30)
    
    pygame.display.flip()
    
    
    
