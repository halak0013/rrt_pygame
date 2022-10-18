#Bismillahirramanirrahim
from time import sleep
import pygame as pg


pg.init()
scr=pg.display.set_mode((600,500))
pg.display.set_caption("rrt ile yol bulma")
done=False
font = pg.font.SysFont('arial', 18)
text = font.render("Welcome to Pygame Example!",True, (0,255,0))
x=0 
y=50
circle=pg.draw.circle(scr,(200,0,0),(x,y),20)
pg.display.flip()
while not done:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            done=True

        if event.type==pg.MOUSEBUTTONDOWN: 
            x,y=event.pos
            print(x,y)
    #? arka planı boyuyor
    scr.fill((0,0,0))
    #? 20-> yarı çap
    #? 250,250->kordinat 
    pg.draw.circle(scr,(200,0,0),(250,250),20)
    color=(0,250,0)
    circle=pg.draw.circle(scr,(200,0,0),(x,y),20)
    
    
    #?40,300 başlangıç  140,300 son   6 kalınalık
    pg.draw.line(scr,color,(40,300),(140,300),6)
    sleep(0.2)

    scr.blit(text, (40,60))
    #?ekranı güncellemek için
    pg.display.flip()
#? pencere boyutu
x,y=scr.get_size()
print(x,y)
pg.display.flip()