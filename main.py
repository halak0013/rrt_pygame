#Bismillahirrahmanirrahim
import pygame as pg
import sabitler as sbt
from time import sleep
from rrt_temel import RrtProces
#import rrt_temel as rp


pg.init()
scr=pg.display.set_mode((600,500))
pg.display.set_caption("rrt ile yol bulma")
x,y=scr.get_size()
scr.fill(sbt.Colors.black)

startC=[]
goalC=[]
beginCheck=0
done=True
while beginCheck<2:
    for event in pg.event.get():
        if event.type==pg.MOUSEBUTTONDOWN:
            if beginCheck == 0:
                startC=event.pos
                pg.draw.circle(scr,sbt.Colors.lime,startC,sbt.circleRad)
            else:
                goalC=event.pos
                pg.draw.circle(scr,sbt.Colors.red,goalC,sbt.circleRad)
            pg.display.flip()
            beginCheck+=1
rrt = RrtProces(scr,x,y,startC,goalC)



while done:
    #? arka planı boyuyor
    rrt.drawStartAndGoal(startC,goalC)
    done=rrt.finish()
    sleep(0.05)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            done=False
    #?ekranı güncellemek için
    pg.display.flip()
done=True
while done:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            done=False