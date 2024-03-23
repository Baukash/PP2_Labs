import pygame

pygame.init()
screen = pygame.display.set_mode((800,200))
exit = False

pygame.mixer.music.load('orda1.mp3')
pygame.mixer.music.play()

mList = ['orda1.mp3', 'orda2.mp3', 'orda3.mp3']

clocka = pygame.time.Clock()

queue = 0

while not exit:
    clocka.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key == pygame.K_RETURN:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_LEFT:
                if queue==0:
                    queue = 2
                    pygame.mixer.music.load(mList[queue])
                    pygame.mixer.music.play()
                else:
                    queue-=1
                    pygame.mixer.music.load(mList[queue])
                    pygame.mixer.music.play()
            if event.key == pygame.K_RIGHT:
                if queue==2:
                    queue=0
                    pygame.mixer.music.load(mList[queue])
                    pygame.mixer.music.play()
                else:
                    queue+=1
                    pygame.mixer.music.load(mList[queue])
                    pygame.mixer.music.play()
                
            
            
    pygame.display.flip()