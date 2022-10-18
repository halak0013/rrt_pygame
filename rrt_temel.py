#Bismillahirrahmanirrahim
import random
import pygame as pg
import sabitler as sbt


class RrtProces:
    def __init__(self, screen,scrWidth,scrHeight,startP,goalP):
        self.screnn = screen
        self.scrHeight=scrHeight
        self.scrWidth=scrWidth
        self.startP=startP
        self.goalP=goalP
        sbt.Arrays.cordsTree.append((startP))
        sbt.Arrays.parents.append(0)

    def randPoint(self):
        return (random.randint(0, self.scrWidth), random.randint(0, self.scrHeight))

    def drawLine(self,cord1, cord2,color):
        pg.draw.line(self.screnn,color,cord1,cord2,sbt.ticknes)
    
    def distance(self,cord1,cord2):
        return ((cord1[0]-cord2[0])**2+(cord1[1]-cord2[1])**2)**0.5


    def drawCircle(self,cord,color,rad=sbt.circleRad):
        pg.draw.circle(self.screnn,color,cord,rad)
    
    def drawStartAndGoal(self,startC,goalC):
        self.drawCircle(startC,sbt.Colors.lime)
        self.drawCircle(goalC,sbt.Colors.red)

    def findCord(self,nearest,randP):
        dis=self.distance(nearest,randP)
        cord=[]
        cord.append((sbt.lineDis*(randP[0]-nearest[0]))/dis+nearest[0])
        cord.append((sbt.lineDis*(randP[1]-nearest[1]))/dis+nearest[1])
        sbt.Arrays.cordsTree.append((cord))
        return cord

    def addNode(self):
        randP=self.randPoint()
        cordsTree2=sbt.Arrays.cordsTree
        nearest=cordsTree2[0]
        tempD1=self.distance(randP,cordsTree2[0])
        tempD2=0
        index=0

        for p in range(len(cordsTree2)):
            tempD2=self.distance(randP,cordsTree2[p])
            if tempD1>tempD2:
                nearest=cordsTree2[p]
                tempD1=tempD2
                index=p
        
        sbt.Arrays.parents.append(index)
        cord =self.findCord(nearest,randP)
        #print(nearest,cord)
        self.drawLine(nearest,cord,sbt.Colors.aqua)
        self.drawCircle(cord,sbt.Colors.white,3)
        return nearest
        
    def finish(self):
        cord=self.addNode()
        if self.distance(cord,self.goalP) < sbt.finishDis:
            print("başarılı")
            self.shortestPath()
            return False
        return True
    def shortestPath(self):
        index=sbt.Arrays.parents[-1]
        tempC=sbt.Arrays.cordsTree[-1]
        cordsTree=sbt.Arrays.cordsTree
        while index != 0:
            self.drawLine(tempC,cordsTree[index],sbt.Colors.blue)
            tempC=cordsTree[index]
            index=sbt.Arrays.parents[index]
