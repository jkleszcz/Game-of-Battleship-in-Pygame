# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 20:10:31 2017

@author: Usuryjskij
"""

import pygame
from pygame.locals import*
GREEN   = (  0, 204,   0)
cant_place_ship = [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10]
class Ship(object):
    
    def __init__(self,shipsize,board):
        self.shipsize = shipsize
        self.placed = False
        self.position = []
        self.board = board
        self.dead = False
        self.hits = shipsize

############################# Place your ships ################################
        
    def placeBoat(self,screen,user_ships):
        ship_flag = True
        while ship_flag:
            for event in pygame.event.get():
                vertic = pygame.key.get_pressed()
                if(event.type==MOUSEBUTTONDOWN and not vertic[K_SPACE]):
                    temppos = event.pos
                    if(temppos[0]>553 and temppos[0]<803 and temppos[1]>self.board and temppos[1]<self.board+250):
                        recx = int((temppos[0]-553)/25)
                        recy = int((temppos[1]-self.board)/25)
                        if(self.checkPlace(recx,recy,vertic) == True):
                            for i in range(self.shipsize):
                                if(recx+self.shipsize-1 > 9):
                                    pygame.draw.rect(screen,GREEN,(555+(10-self.shipsize+i)*25,self.board+2+recy*25,22,22))
                                    user_ships[10-self.shipsize+i][recy] = True
                                    self.position +=[(10-self.shipsize+i,recy)]
                                    self.setCollision(10-self.shipsize+i,recy)
                                else:    
                                    pygame.draw.rect(screen,GREEN,(555+(recx+i)*25,self.board+2+recy*25,22,22))
                                    user_ships[recx+i][recy] = True
                                    self.position +=[(recx+i,recy)]
                                    self.setCollision(recx+i,recy)
                            self.placed = True
                            pygame.display.update()
                            ship_flag = False
                            break
                        else:
                            print("Kolizja, zrob jeszcze raz")
                    
                elif(event.type==MOUSEBUTTONDOWN and vertic[K_SPACE]):
                    temppos = event.pos
                    if(temppos[0]>553 and temppos[0]<803 and temppos[1]>self.board and temppos[1]<self.board+250):
                        recx = int((temppos[0]-553)/25)
                        recy = int((temppos[1]-self.board)/25)
                        if(self.checkPlace(recx,recy,vertic) == True):
                            for i in range(self.shipsize):
                                if(recy >= 6):
                                    pygame.draw.rect(screen,GREEN,(555+(recx)*25,self.board+2+(10-self.shipsize+i)*25,22,22))
                                    user_ships[recx][10-self.shipsize+i] = True
                                    self.position += [(recx,10-self.shipsize+i)]
                                    self.setCollision(recx,10-self.shipsize+i)
                                else:    
                                    pygame.draw.rect(screen,GREEN,(555+(recx)*25,self.board+2+(recy+i)*25,22,22))
                                    user_ships[recx][recy+i] = True
                                    self.position += [(recx,recy+i)]
                                    self.setCollision(recx,recy+i)
                            self.placed = True
                            pygame.display.update()
                            ship_flag = False
                            break


################################# Set collision ###############################

    def setCollision(self,recx,recy):
        if(recx == 0 and recy == 0):
            cant_place_ship[recx][recy] = True
            cant_place_ship[recx+1][recy] = True
            cant_place_ship[recx][recy+1] = True
            cant_place_ship[recx+1][recy+1] = True
        elif(recx == 9 and recy == 9):
            cant_place_ship[recx][recy] = True
            cant_place_ship[recx-1][recy] = True
            cant_place_ship[recx][recy-1] = True
            cant_place_ship[recx-1][recy-1] = True
        elif(not recx == 0 and not recx == 9 and recy == 0):
            for i in range(2):
                for j in range(3):
                    cant_place_ship[recx-1+j][recy+i] = True
        elif(not recx == 0 and not recx == 9 and recy == 9):
            for i in range(2):
                for j in range (3):
                    cant_place_ship[recx-1+j][recy-i] = True
        elif(not recy == 0 and not recy == 9 and recx == 0):
            for i in range(3):
                for j in range(2):
                    cant_place_ship[recx+j][recy-1+i] = True
        elif(not recy == 0 and not recy == 9 and recx == 9):
            for i in range(3):
                for j in range(2):
                    cant_place_ship[recx-j][recy-1+i] = True
        elif(recx == 0 and recy == 9):
            cant_place_ship[recx][recy] = True
            cant_place_ship[recx+1][recy] = True
            cant_place_ship[recx][recy-1] = True
            cant_place_ship[recx+1][recy-1] = True
        elif(recx == 9 and recy == 0):
            cant_place_ship[recx][recy] = True
            cant_place_ship[recx-1][recy] = True
            cant_place_ship[recx][recy+1] = True
            cant_place_ship[recx-1][recy-1] = True
        else:
            for i in range(3):
                for j in range(3):
                    cant_place_ship[recx-1+i][recy-1+j] = True

##############################################################################
        
 ############################## Check place ##################################

    def checkPlace(self,recx,recy,vertic):
        flag = True
        if(vertic[K_SPACE] == False):
            for i in range(self.shipsize):
                if(recx+self.shipsize-1 > 9):
                    if(cant_place_ship[10-self.shipsize+i][recy] == True):
                        flag = False
                else:    
                    if(cant_place_ship[recx+i][recy] == True):
                        flag = False
                        
        elif(vertic[K_SPACE] == True):
            for i in range(self.shipsize):
                if(recy >= 6):
                    if(cant_place_ship[recx][10-self.shipsize+i] == True):
                        flag = False
                else:    
                    if(cant_place_ship[recx][recy+i] == True):
                        flag = False
        return flag
        
    def hit(self):
        self.hits -= 1
        if(self.hits == 0):
            self.dead = True


         

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
