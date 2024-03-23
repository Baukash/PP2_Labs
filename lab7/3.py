import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))
exit = False

xline=800
yline=800

x,y=30,30

clock = pygame.time.Clock()

while not exit:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP] and y>=40:
        y -= 20
    if pressed[pygame.K_DOWN] and y<=760:
        y += 20
    if pressed[pygame.K_LEFT] and x>=40:
        x -= 20
    if pressed[pygame.K_RIGHT] and x<=760:
        x += 20
    
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (100,100,100), (x,y), 25)
            
    pygame.display.flip()