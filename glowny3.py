# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 23:15:51 2017

@author: Usuryjskij
"""

import pygame, ships
from pygame.locals import*

background_file = 'tlo2.jpg'
windesktop = 'bismarck.jpg'
WINDOWWIDTH = 1356
WINDOWHEIGHT = 700
BLACK   = (  0,   0,   0)
WHITE = (255,255,255)
GREEN   = (  0, 204,   0)
RED = (255,0,0)
class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32) #rozmiar okna
        self.ticket = pygame.display.set_caption("") #Etykieta
        self.background = pygame.image.load(background_file).convert()
        self.basic_font = pygame.font.Font('freesansbold.ttf', 80)
        self.small_font = pygame.font.Font('freesansbold.ttf', 25)
        self.user_ships = [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10]
        self.user_ships2 = [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10]
        pygame.mixer.music.load('theme.mp3')
        pygame.mixer.music.play(-1, 0.0)
    def desktop(self):
        self.screen.blit(self.background, (0,0))
        pygame.display.update()
        
        
############################### Menu glowne gry ##############################        
    def menuGame(self):
        new_game_button = self.basic_font.render("NEW GAME",True,BLACK)
        new_game_rect = new_game_button.get_rect() 
        new_game_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        self.screen.blit(new_game_button,new_game_rect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif(event.type==MOUSEBUTTONDOWN):
                    #if(event.pos >= (537,329) and event.pos <= (823,366)):
                    if new_game_rect.collidepoint(event.pos):
                        return
############################# Player 1 place ships ############################ 
   
    def place_ships(self):
        self.desktop()
        self.draw_board()
        self.air_ship = ships.Ship(4,370)
        self.battle1 = ships.Ship(3,370)
        self.battle2 = ships.Ship(3,370)
        self.submarine1 = ships.Ship(2,370)
        self.submarine2 = ships.Ship(2,370)
        self.submarine3 = ships.Ship(2,370)
        self.war1 = ships.Ship(1,370)
        self.war2 = ships.Ship(1,370)
        self.war3 = ships.Ship(1,370)
        self.war4 = ships.Ship(1,370)
        
        pygame.display.update()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif(event.type==MOUSEBUTTONDOWN):
                    if (air_rect.collidepoint(event.pos) and self.air_ship.placed == False):
                        self.air_ship.placeBoat(self.screen,self.user_ships)
                    elif(battle1_rect.collidepoint(event.pos) and self.battle1.placed == False):
                        self.battle1.placeBoat(self.screen,self.user_ships)
                    elif(battle2_rect.collidepoint(event.pos) and self.battle2.placed == False):
                        self.battle2.placeBoat(self.screen,self.user_ships)
                    elif(sub1_rect.collidepoint(event.pos) and self.submarine1.placed == False):
                        self.submarine1.placeBoat(self.screen,self.user_ships)                               
                    elif(sub2_rect.collidepoint(event.pos) and self.submarine2.placed == False):
                        self.submarine2.placeBoat(self.screen,self.user_ships)                               
                    elif(sub3_rect.collidepoint(event.pos) and self.submarine3.placed == False):
                        self.submarine3.placeBoat(self.screen,self.user_ships)                   
                    elif(war1_rect.collidepoint(event.pos) and self.war1.placed == False):
                        self.war1.placeBoat(self.screen,self.user_ships)
                    elif(war2_rect.collidepoint(event.pos) and self.war2.placed == False):
                        self.war2.placeBoat(self.screen,self.user_ships)
                    elif(war3_rect.collidepoint(event.pos) and self.war3.placed == False):
                        self.war3.placeBoat(self.screen,self.user_ships)
                    elif(war4_rect.collidepoint(event.pos) and self.war4.placed == False):
                        self.war4.placeBoat(self.screen,self.user_ships)
                    elif(ready_rect.collidepoint(event.pos) and self.air_ship.placed == True 
                         and self.battle1.placed == True and self.battle2.placed == True 
                         and self.submarine1.placed == True and self.submarine2.placed == True 
                         and self.submarine3.placed == True and self.war1.placed == True 
                         and self.war2.placed == True and self.war3.placed == True and self.war4.placed == True):
                        return
            if(self.air_ship.placed == True):
                pygame.draw.rect(self.screen,GREEN,(900,50,300,85),5) 
                pygame.display.update()
            if(self.battle1.placed == True):
                pygame.draw.rect(self.screen,GREEN,(900,145,300,85),5) 
                pygame.display.update()                
            if(self.battle2.placed == True):
                pygame.draw.rect(self.screen,GREEN,(900,240,300,85),5) 
                pygame.display.update()                   
            if(self.submarine1.placed == True):
                pygame.draw.rect(self.screen,GREEN,(900,335,145,60),5) 
                pygame.display.update()                        
            if(self.submarine2.placed == True):
                pygame.draw.rect(self.screen,GREEN,(1055,335,145,60),5) 
                pygame.display.update()
            if(self.submarine3.placed == True):
                pygame.draw.rect(self.screen,GREEN,(900,405,145,60),5) 
                pygame.display.update()  
            if(self.war1.placed == True):
                pygame.draw.rect(self.screen,GREEN,(1055,405,145,60),5) 
                pygame.display.update()
            if(self.war2.placed == True):
                pygame.draw.rect(self.screen,GREEN,(900,475,145,60),5) 
                pygame.display.update() 
            if(self.war3.placed == True):
                pygame.draw.rect(self.screen,GREEN,(1055,475,145,60),5) 
                pygame.display.update()  
            if(self.war4.placed == True):
                pygame.draw.rect(self.screen,GREEN,(978,545,145,60),5) 
                pygame.display.update()  


############################# Player 2 place ships ############################ 
   
    def place_ships2(self):
        self.desktop()
        self.draw_board2()
        self.air_ship2 = ships.Ship(4,50)
        self.battle12 = ships.Ship(3,50)
        self.battle22 = ships.Ship(3,50)
        self.submarine12 = ships.Ship(2,50)
        self.submarine22 = ships.Ship(2,50)
        self.submarine32 = ships.Ship(2,50)
        self.war12 = ships.Ship(1,50)
        self.war22 = ships.Ship(1,50)
        self.war32 = ships.Ship(1,50)
        self.war42 = ships.Ship(1,50)
        
        pygame.display.update()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif(event.type==MOUSEBUTTONDOWN):
                    if (air_rect2.collidepoint(event.pos) and self.air_ship2.placed == False):
                        self.air_ship2.placeBoat(self.screen,self.user_ships2)
                    elif(battle1_rect2.collidepoint(event.pos) and self.battle12.placed == False):
                        self.battle12.placeBoat(self.screen,self.user_ships2)
                    elif(battle2_rect2.collidepoint(event.pos) and self.battle22.placed == False):
                        self.battle22.placeBoat(self.screen,self.user_ships2)
                    elif(sub1_rect2.collidepoint(event.pos) and self.submarine12.placed == False):
                        self.submarine12.placeBoat(self.screen,self.user_ships2)                               
                    elif(sub2_rect2.collidepoint(event.pos) and self.submarine22.placed == False):
                        self.submarine22.placeBoat(self.screen,self.user_ships2)                               
                    elif(sub3_rect2.collidepoint(event.pos) and self.submarine32.placed == False):
                        self.submarine32.placeBoat(self.screen,self.user_ships2)                   
                    elif(war1_rect2.collidepoint(event.pos) and self.war12.placed == False):
                        self.war12.placeBoat(self.screen,self.user_ships2)
                    elif(war2_rect2.collidepoint(event.pos) and self.war22.placed == False):
                        self.war22.placeBoat(self.screen,self.user_ships2)
                    elif(war3_rect2.collidepoint(event.pos) and self.war32.placed == False):
                        self.war32.placeBoat(self.screen,self.user_ships2)
                    elif(war4_rect2.collidepoint(event.pos) and self.war42.placed == False):
                        self.war42.placeBoat(self.screen,self.user_ships2)
                    elif(ready_rect2.collidepoint(event.pos) and self.air_ship2.placed == True 
                         and self.battle12.placed == True and self.battle22.placed == True 
                         and self.submarine12.placed == True and self.submarine22.placed == True 
                         and self.submarine32.placed == True and self.war12.placed == True 
                         and self.war22.placed == True and self.war32.placed == True and self.war42.placed == True):
                        return
            if(self.air_ship2.placed == True):
                pygame.draw.rect(self.screen,GREEN,(100,50,300,85),5) 
                pygame.display.update()
            if(self.battle12.placed == True):
                pygame.draw.rect(self.screen,GREEN,(100,145,300,85),5) 
                pygame.display.update()                
            if(self.battle22.placed == True):
                pygame.draw.rect(self.screen,GREEN,(100,240,300,85),5) 
                pygame.display.update()                   
            if(self.submarine12.placed == True):
                pygame.draw.rect(self.screen,GREEN,(100,335,145,60),5) 
                pygame.display.update()                        
            if(self.submarine22.placed == True):
                pygame.draw.rect(self.screen,GREEN,(255,335,145,60),5) 
                pygame.display.update()
            if(self.submarine32.placed == True):
                pygame.draw.rect(self.screen,GREEN,(100,405,145,60),5) 
                pygame.display.update()  
            if(self.war12.placed == True):
                pygame.draw.rect(self.screen,GREEN,(255,405,145,60),5) 
                pygame.display.update()
            if(self.war22.placed == True):
                pygame.draw.rect(self.screen,GREEN,(100,475,145,60),5) 
                pygame.display.update() 
            if(self.war32.placed == True):
                pygame.draw.rect(self.screen,GREEN,(255,475,145,60),5) 
                pygame.display.update()  
            if(self.war42.placed == True):
                pygame.draw.rect(self.screen,GREEN,(178,545,145,60),5) 
                pygame.display.update() 
                                
############################### Rysowanie siatek #############################

    def draw_board(self):
        global air_rect,battle1_rect,battle2_rect, sub1_rect,sub2_rect,sub3_rect,war1_rect,war2_rect,war3_rect,war4_rect,ready_rect

        pygame.draw.rect(self.screen,WHITE,(543,360,270,270))

        sub_2 = self.small_font.render("Player 2 fleet status:",True,BLACK)

        rect_sub_2 = sub_2.get_rect()

        rect_sub_2.center = (WINDOWWIDTH / 2, 340)

        self.screen.blit(sub_2,rect_sub_2)
                    
        for i in range (10):
            for j in range (10):
                pygame.draw.rect(self.screen,BLACK,(553+i*25,370+j*25,25,25),2)
        
        air_button = pygame.image.load('air.jpg').convert()
        air_rect = air_button.get_rect()
        air_rect.topleft = (900,50)
        self.screen.blit(air_button,air_rect)
        
        battle1_button = pygame.image.load('battleship.png').convert()
        battle1_rect = battle1_button.get_rect()
        battle1_rect.topleft = (900,145)
        self.screen.blit(battle1_button,battle1_rect)
        
        battle2_button = pygame.image.load('battleship.png').convert()
        battle2_rect = battle2_button.get_rect()
        battle2_rect.topleft = (900,240)
        self.screen.blit(battle2_button,battle2_rect)
        
        sub1_button = pygame.image.load('submarine.png').convert()
        sub1_rect = sub1_button.get_rect()
        sub1_rect.topleft = (900,335)
        self.screen.blit(sub1_button,sub1_rect)

        sub2_button = pygame.image.load('submarine.png').convert()
        sub2_rect = sub2_button.get_rect()
        sub2_rect.topleft = (1055,335)
        self.screen.blit(sub2_button,sub2_rect)
        
        sub3_button = pygame.image.load('submarine.png').convert()
        sub3_rect = sub3_button.get_rect()
        sub3_rect.topleft = (900,405)
        self.screen.blit(sub3_button,sub3_rect)

        war1_button = pygame.image.load('warship.png').convert()
        war1_rect = war1_button.get_rect()
        war1_rect.topleft = (1055,405)
        self.screen.blit(war1_button,war1_rect)
    
        war2_button = pygame.image.load('warship.png').convert()
        war2_rect = war2_button.get_rect()
        war2_rect.topleft = (900,475)
        self.screen.blit(war2_button,war2_rect)
        
        war3_button = pygame.image.load('warship.png').convert()
        war3_rect = war3_button.get_rect()
        war3_rect.topleft = (1055,475)
        self.screen.blit(war3_button,war3_rect)
        
        war4_button = pygame.image.load('warship.png').convert()
        war4_rect = war4_button.get_rect()
        war4_rect.center = (1050,575)
        self.screen.blit(war4_button,war4_rect)
        
        ready_button = pygame.image.load('ready.jpg').convert()
        ready_rect = ready_button.get_rect()
        ready_rect.center = (1050,650)
        self.screen.blit(ready_button,ready_rect)
        
        pygame.display.update()
        
############################### Rysowanie siatek 2 #############################

    def draw_board2(self):
        global air_rect2,battle1_rect2,battle2_rect2, sub1_rect2,sub2_rect2,sub3_rect2,war1_rect2,war2_rect2,war3_rect2,war4_rect2,ready_rect2
        pygame.draw.rect(self.screen,WHITE,(543,40,270,270))
        sub_1 = self.small_font.render("Player 1 fleet status",True,BLACK)
        rect_sub_1 = sub_1.get_rect()

        rect_sub_1.center = (WINDOWWIDTH / 2, 20)

        self.screen.blit(sub_1,rect_sub_1)

            
        for i in range (10):
            for j in range (10):
                pygame.draw.rect(self.screen,BLACK,(553+i*25,50+j*25,25,25),2)
                    

        
        air_button2 = pygame.image.load('air.jpg').convert()
        air_rect2 = air_button2.get_rect()
        air_rect2.topleft = (100,50)
        self.screen.blit(air_button2,air_rect2)
        
        battle1_button2 = pygame.image.load('battleship.png').convert()
        battle1_rect2 = battle1_button2.get_rect()
        battle1_rect2.topleft = (100,145)
        self.screen.blit(battle1_button2,battle1_rect2)
        
        battle2_button2 = pygame.image.load('battleship.png').convert()
        battle2_rect2 = battle2_button2.get_rect()
        battle2_rect2.topleft = (100,240)
        self.screen.blit(battle2_button2,battle2_rect2)
        
        sub1_button2 = pygame.image.load('submarine.png').convert()
        sub1_rect2 = sub1_button2.get_rect()
        sub1_rect2.topleft = (100,335)
        self.screen.blit(sub1_button2,sub1_rect2)

        sub2_button2 = pygame.image.load('submarine.png').convert()
        sub2_rect2 = sub2_button2.get_rect()
        sub2_rect2.topleft = (255,335)
        self.screen.blit(sub2_button2,sub2_rect2)
        
        sub3_button2 = pygame.image.load('submarine.png').convert()
        sub3_rect2 = sub3_button2.get_rect()
        sub3_rect2.topleft = (100,405)
        self.screen.blit(sub3_button2,sub3_rect2)

        war1_button2 = pygame.image.load('warship.png').convert()
        war1_rect2 = war1_button2.get_rect()
        war1_rect2.topleft = (255,405)
        self.screen.blit(war1_button2,war1_rect2)
    
        war2_button2 = pygame.image.load('warship.png').convert()
        war2_rect2 = war2_button2.get_rect()
        war2_rect2.topleft = (100,475)
        self.screen.blit(war2_button2,war2_rect2)
        
        war3_button2 = pygame.image.load('warship.png').convert()
        war3_rect2 = war3_button2.get_rect()
        war3_rect2.topleft = (255,475)
        self.screen.blit(war3_button2,war3_rect2)
        
        war4_button2 = pygame.image.load('warship.png').convert()
        war4_rect2 = war4_button2.get_rect()
        war4_rect2.center = (250,575)
        self.screen.blit(war4_button2,war4_rect2)
        
        ready_button2 = pygame.image.load('ready.jpg').convert()
        ready_rect2 = ready_button2.get_rect()
        ready_rect2.center = (250,650)
        self.screen.blit(ready_button2,ready_rect2)
        
        pygame.display.update()
        
################################ Game begin #############################

    def startgame(self):
        self.p1traf = 0
        self.p2traf = 0
        self.desktop()
        self.draw_board()
        self.draw_board2()
        pygame.display.update()

        while 1:
            self.player_1_turn()
            self.shipdead()
            self.player_2_turn()
            self.shipdead()

            if(self.p1traf == 20):
                self.displayWinner(1)
                while 1:
                    for event in pygame.event.get():
                        waiting = pygame.key.get_pressed()
                        if(waiting[K_SPACE]==True):
                            return
            elif(self.p2traf == 20):
                self.displayWinner(2)
                while 1:
                    for event in pygame.event.get():
                        waiting = pygame.key.get_pressed()
                        if(waiting[K_SPACE]==True):
                            return                
                
                
                
                    
############################# Player 1 turn ##################################

    def player_1_turn(self):
        fla = True
        while fla:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif(event.type==MOUSEBUTTONDOWN):
                    temppos = event.pos
                    if(temppos[0]>553 and temppos[0]<803 and temppos[1]>370 and temppos[1]<620):
                        recx = int((temppos[0]-553)/25)
                        recy = int((temppos[1]-370)/25)
                        if(self.user_ships[recx][recy] == True):
                            self.p1traf +=1
                            pygame.mixer.music.load('Explosion1.wav')
                            pygame.mixer.music.play(1,0.0)
                            pygame.draw.rect(self.screen,RED,(555+recx*25,370+2+recy*25,22,22))
                            pygame.display.update()
                            self.player1_hit(recx,recy)
                        elif(self.user_ships[recx][recy] == False):
                            pygame.mixer.music.load('Splash.wav')
                            pygame.mixer.music.play(1,0.0)
                            pygame.draw.rect(self.screen,BLACK,(555+recx*25,370+2+recy*25,22,22))
                            pygame.display.update()
                        fla = False
                        break

############################# Player 2 turn ##################################

    def player_2_turn(self):
        fla = True
        while fla:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif(event.type==MOUSEBUTTONDOWN):
                    temppos = event.pos
                    if(temppos[0]>553 and temppos[0]<803 and temppos[1]>50 and temppos[1]<300):
                        recx = int((temppos[0]-553)/25)
                        recy = int((temppos[1]-50)/25)
                        if(self.user_ships2[recx][recy] == True):
                            self.p2traf +=1
                            pygame.mixer.music.load('Explosion1.wav')
                            pygame.mixer.music.play(1,0.0)
                            pygame.draw.rect(self.screen,RED,(555+recx*25,50+2+recy*25,22,22))
                            pygame.display.update()
                            self.player2_hit(recx,recy)
                        elif(self.user_ships2[recx][recy] == False):
                            pygame.mixer.music.load('Splash.wav')
                            pygame.mixer.music.play(1,0.0)
                            pygame.draw.rect(self.screen,BLACK,(555+recx*25,50+2+recy*25,22,22))
                            pygame.display.update()
                        fla = False
                        break
                            
############################### Check hit 1 ###################################                            
    def player1_hit(self,recx,recy):
        shot = (recx,recy)
        for i in range(self.air_ship.shipsize):
            if(shot == self.air_ship.position[i]):
                self.air_ship.hit()
                return
        for i in range(self.battle1.shipsize):
            if(shot == self.battle1.position[i]):
                self.battle1.hit()
                return
        for i in range(self.battle2.shipsize):
            if(shot == self.battle2.position[i]):
                self.battle2.hit()
                return
        for i in range(self.submarine1.shipsize):
            if(shot == self.submarine1.position[i]):
                self.submarine1.hit()
                return
        for i in range(self.submarine2.shipsize):
            if(shot == self.submarine2.position[i]):
                self.submarine2.hit()
                return
        for i in range(self.submarine3.shipsize):
            if(shot == self.submarine3.position[i]):
                self.submarine3.hit()
                return
        for i in range(self.war1.shipsize):
            if(shot == self.war1.position[i]):
                self.war1.hit()
                return
        for i in range(self.war2.shipsize):
            if(shot == self.war2.position[i]):
                self.war2.hit()
                return 
        for i in range(self.war3.shipsize):
            if(shot == self.war3.position[i]):
                self.war3.hit()
                return
        for i in range(self.war4.shipsize):
            if(shot == self.war4.position[i]):
                self.war4.hit()
                return
                
############################### Check hit 2 ###################################                            
    def player2_hit(self,recx,recy):
        shot = (recx,recy)
        for i in range(self.air_ship2.shipsize):
            if(shot == self.air_ship2.position[i]):
                self.air_ship2.hit()
                return
        for i in range(self.battle12.shipsize):
            if(shot == self.battle12.position[i]):
                self.battle12.hit()
                return
        for i in range(self.battle22.shipsize):
            if(shot == self.battle22.position[i]):
                self.battle22.hit()
                return
        for i in range(self.submarine12.shipsize):
            if(shot == self.submarine12.position[i]):
                self.submarine12.hit()
                return
        for i in range(self.submarine22.shipsize):
            if(shot == self.submarine22.position[i]):
                self.submarine22.hit()
                return
        for i in range(self.submarine32.shipsize):
            if(shot == self.submarine32.position[i]):
                self.submarine32.hit()
                return
        for i in range(self.war12.shipsize):
            if(shot == self.war12.position[i]):
                self.war12.hit()
                return
        for i in range(self.war22.shipsize):
            if(shot == self.war22.position[i]):
                self.war22.hit()
                return 
        for i in range(self.war32.shipsize):
            if(shot == self.war32.position[i]):
                self.war32.hit()
                return
        for i in range(self.war42.shipsize):
            if(shot == self.war42.position[i]):
                self.war42.hit()
                return
                
############################## Winner??? #####################################                
    #def check_winner(self):
        #if(self.air_ship.dead == True and self.battle1.dead == True 
         #  and self.battle2.dead == True and self.submarine1.dead == True 
          # and self.submarine2.dead == True and self.submarine3.dead == True
           #and self.war1.dead == True and self.war2.dead == True 
           #and self.war3.dead == True and self.war4.dead == True):
            #return 1
        
        #elif(self.air_ship2.dead == True and self.battle12.dead == True 
         #  and self.battle22.dead == True and self.submarine12.dead == True 
          # and self.submarine22.dead == True and self.submarine32.dead == True
           #and self.war12.dead == True
           #and self.war22.dead == True and self.war32.dead == True and self.war42.dead == True):
            #return 2
       # for i in range(10):
        #    for j in range(10):
                
        #else:
         #   return 0
            
################################ Display winner ##############################            
            
    def displayWinner(self,winner):
        self.desktop()
        
        pygame.display.update()
        if (winner == 1):
            sub = self.basic_font.render("Player 1 WIN!",True,BLACK)
        elif(winner == 2):
            sub = self.basic_font.render("Player 2 WIN!",True,BLACK)                
        sub_rect = sub.get_rect() 
        sub_rect.center = (WINDOWWIDTH / 2, 100)
        sub2 = self.small_font.render("Press SPACEBAR to continue", True, BLACK)
        sub2rect = sub2.get_rect()
        sub_rect.center = (WINDOWWIDTH / 2, 600)
        self.screen.blit(sub,sub_rect)
        self.screen.blit(sub2,sub2rect)
        pygame.display.update()
        
###############################Ship dead ######################################
    def shipdead(self):
        if(self.air_ship.dead == True):
            pygame.draw.rect(self.screen,RED,(900,50,300,85),10) 
            pygame.display.update()
        if(self.battle1.dead == True):
            pygame.draw.rect(self.screen,RED,(900,145,300,85),10) 
            pygame.display.update()                
        if(self.battle2.dead == True):
            pygame.draw.rect(self.screen,RED,(900,240,300,85),10) 
            pygame.display.update()                   
        if(self.submarine1.dead == True):
            pygame.draw.rect(self.screen,RED,(900,335,145,60),10) 
            pygame.display.update()                        
        if(self.submarine2.dead == True):
            pygame.draw.rect(self.screen,RED,(1055,335,145,60),10) 
            pygame.display.update()
        if(self.submarine3.dead == True):
            pygame.draw.rect(self.screen,RED,(900,405,145,60),10) 
            pygame.display.update()  
        if(self.war1.dead == True):
            pygame.draw.rect(self.screen,RED,(1055,405,145,60),10) 
            pygame.display.update()
        if(self.war2.dead == True):
            pygame.draw.rect(self.screen,RED,(900,475,145,60),10) 
            pygame.display.update() 
        if(self.war3.dead == True):
            pygame.draw.rect(self.screen,RED,(1055,475,145,60),10) 
            pygame.display.update()  
        if(self.war4.dead == True):
            pygame.draw.rect(self.screen,RED,(978,545,145,60),10) 
            pygame.display.update()
        if(self.air_ship2.dead == True):
            pygame.draw.rect(self.screen,RED,(100,50,300,85),10) 
            pygame.display.update()
        if(self.battle12.dead == True):
            pygame.draw.rect(self.screen,RED,(100,145,300,85),10) 
            pygame.display.update()                
        if(self.battle22.dead == True):
            pygame.draw.rect(self.screen,RED,(100,240,300,85),10) 
            pygame.display.update()                   
        if(self.submarine12.dead == True):
            pygame.draw.rect(self.screen,RED,(100,335,145,60),10) 
            pygame.display.update()                        
        if(self.submarine22.dead == True):
            pygame.draw.rect(self.screen,RED,(255,335,145,60),10) 
            pygame.display.update()
        if(self.submarine32.dead == True):
            pygame.draw.rect(self.screen,RED,(100,405,145,60),10) 
            pygame.display.update()  
        if(self.war12.dead == True):
            pygame.draw.rect(self.screen,RED,(255,405,145,60),10) 
            pygame.display.update()
        if(self.war22.dead == True):
            pygame.draw.rect(self.screen,RED,(100,475,145,60),10) 
            pygame.display.update() 
        if(self.war32.dead == True):
            pygame.draw.rect(self.screen,RED,(255,475,145,60),10) 
            pygame.display.update()  
        if(self.war42.dead == True):
            pygame.draw.rect(self.screen,RED,(178,545,145,60),10) 
            pygame.display.update()
############################### GAME ##########################################
     
    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.desktop()
            self.menuGame()
            self.user_ships = [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10]
            self.user_ships2 = [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10]
            ships.cant_place_ship = [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10]
            self.place_ships2()
            ships.cant_place_ship = [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10]
            self.place_ships()
            pygame.mixer.music.stop()
            self.startgame()
            
##############################################################################
                        
if __name__ == '__main__':
    statki = Game()
    statki.runGame()

                
                
