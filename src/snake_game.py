import pygame
from pygame.constants import KEYDOWN
from pygame.locals import(K_UP,K_DOWN,K_LEFT,K_RIGHT,K_UP,QUIT)
from pygame.time import Clock
import random
from pathlib import Path

pygame.init()

rosso = (255,0,0)
verde = (0,100,0)
blu = (0,0,255)

base_dir = Path(__file__).parent.parent
sfondo_path = Path(f"{base_dir}/img/sfondo_erba.jpeg")
testa_path = Path(f"{base_dir}/img/testaSnake.png")

def avviso(scritta,colore,finestra,lunghezza,altezza,stile):
    carScritta = stile.render(scritta,True,colore)
    finestra.blit(carScritta,(lunghezza/2.5,altezza/2.5))    
    
def collisione(p,q):
    (xp, yp, wp, hp) = p
    (xq, yq, _,_) = q 
    if xp <= xq <= xp + wp and yp <= yq <= yp + hp:
        return True

def serpente(corpo, finestra_gioco):
    for x in corpo[:-1]:
        pygame.draw.rect(finestra_gioco,verde,[x[0]+10,x[1]+10,35,30])

def punteggio(punti,stile, finestra):
    valore = stile.render("Punti: " + str(punti), True,blu)
    finestra.blit(valore,(0,0))

def main():
    running = True
    close = False
    
    lunghezza = 900
    altezza = 500

    finestra_gioco = pygame.display.set_mode((lunghezza,altezza))
    nome = pygame.display.set_caption("Snake")
    sfondo = pygame.image.load(sfondo_path)

    stile = pygame.font.SysFont(None,65)
    
    x = 425
    y = 175
    
    vel = 5

    velX = 0 
    velY = 0

    testa = pygame.image.load(testa_path)
    testa_rid = pygame.transform.scale(testa,(55,50))

    snake = []
    dimSnake = 1

    refreshRate = pygame.time.Clock()

    Xmela = round(random.randrange(85,lunghezza-65))
    Ymela = round(random.randrange(75,altezza-55))

    while running:
        
        while close == True:
            avviso("GAME OVER: C-> Chiudi N-> New partita", rosso, finestra_gioco,0,altezza, stile)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    close = False
                if event.type == KEYDOWN:
                    if event.key == pygame.K_c:
                        running = False
                        close = False
                    if event.key == pygame.K_n:
                        main()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    velX = -vel
                    velY = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    velX  = vel
                    velY = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    velX = 0
                    velY = -vel
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    velX = 0
                    velY = vel

        x += velX
        y += velY
            
        testaRect = pygame.Rect(x,y,55,50)
        
        finestra_gioco.blit(sfondo,(0,0))
        
        snake.append((x,y))
        if len(snake) > dimSnake:
            snake.pop(0)
        
        serpente(snake,finestra_gioco)
        punteggio(dimSnake-1,stile,finestra_gioco)
        
        finestra_gioco.blit(testa_rid,testaRect)
 
        pygame.draw.rect(finestra_gioco,rosso,[Xmela,Ymela,20,20])
        
        if x >= lunghezza-55 or x < 0 or y >= altezza-45 or y < 0:
            close = True
        
        if collisione(testaRect,[Xmela,Ymela,20,20]):
            Xmela = round(random.randrange(10,lunghezza-55))
            Ymela = round(random.randrange(10,altezza-45))
            dimSnake += 1

        refreshRate.tick(30)
        
        pygame.display.flip()

    pygame.quit()

main()