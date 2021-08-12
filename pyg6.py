import pygame
import math

pygame.init()
x=30
y=200
t=0
t2=0
t3=0
x1=800
y1=370
yt = 48
score_n=0
high_score=0
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('gr00t')

game_over= False
go = False
des = True
asc = False
icon = pygame.image.load(r'C:\Users\meris\Desktop\web_development\icon.png')
pygame.display.set_icon(icon)

ball = pygame.image.load(r'C:\Users\meris\Desktop\web_development\ball.png')

DEFAULT_IMAGE_SIZE = (60,60)
ball = pygame.transform.scale(ball, DEFAULT_IMAGE_SIZE)
clock = pygame.time.Clock()

def show_go_screen():
    #screen.fill((0,0,0))
    font = pygame.font.SysFont("calibri" , yt)
    font2 = pygame.font.SysFont("calibri" , 16)
    text = font.render("GAME OVER", True, (255,0,0))
    text2 = font2.render("better luck next time :)", True, (25,25,255))
    screen.blit(text, (300 - text.get_width()//2, 200 - text.get_height()//2))
    screen.blit(text2, (350 - text.get_width()//2, 250 - text.get_height()//2))
    clock.tick(60)
    pygame.display.flip()
    
#def score():
    
 #   pygame.display.flip()
    

    
while not game_over:

    ball = pygame.transform.rotate(ball, 90)
    
    #pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    
    x1-=8
    if(x1<-400): x1=800
    
    
    
    if des:
        if(y<=400-60):
            y+=0.5*80*t**2
            
            t+=1/60
            
            if y>=340:
                if(x1<x): score_n += 1
                #score()
                #print(t)
                des = False
                #asc = True
                t=0;
                
    if asc:
        if(y>=200):
            y-=30*t2-0.5*80*t2**2
            
            t2+=1/60
        if(y<200):
            #print(t2)

            asc = False
            des = True
            t2 = 0;
    
    if(abs(y-y1)<60 and abs(x-x1)<60 or y>500):
        #screen.fill((255,255,255))
        go= True
        des = False
        asc = False
        
    if go:
        show_go_screen()
        #game_over=True
        pygame.QUIT()
        
       
       
         
   
#if event.type == pygame.KEYDOWN:
    

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>0: asc=True
    if pressed[pygame.K_DOWN] and y<400-60: y+=3
    if pressed[pygame.K_LEFT] and x>0: x-=3
    if pressed[pygame.K_RIGHT] and x<400-60: x+=3
    
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(x1,y1,30,30))
   # pygame.draw.rect(screen, (0,0,0), ball,(x,y))
    screen.blit(ball,(x,y))
    
    font = pygame.font.SysFont("calibri" , 32)
    text = font.render('score: '+ str(score_n), True, (0,0,0))
    screen.blit(text, (90 - text.get_width()//2, 30 - text.get_height()//2))
    highscore = font.render('high score: '+ str(score_n), True, (0,0,0))
    screen.blit(highscore, (90 - text.get_width()//2, 60 - text.get_height()//2))
    
    
    pygame.display.flip()
    
    clock.tick(60)   