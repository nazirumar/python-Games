#####################################################################
#
#
#
#  SNAKER.py  - A simple SNAKE game written in Python and Pygame
#
#  This is my first Python / Pygame game written as a learning
#  exercise.
#
#
#  Version: 0.1
#  Date:  12 June 2022
#  Author:  Nazbeen
#  Author email:  nazirumar888@gmail.com
#
#
#
#####################################################################



######### IMPORTS ###################################################


import random, math, pygame
from tarfile import BLOCKSIZE
from pygame.locals import *


counter = 0


    

######### MAIN #####################################################





def main():

    showstartscreen = 1

    while 1 :

        WINSIZE =[800,600]
        WHITE =[255,255,255]
        BLACK = [0,0,0]
        RED = [255,0,0]
        GREEN =[0,255,0]
        BLUE = [0,0,255]
        BLOCKSIZE =[20,20]
        UP = 1
        DOWN = 3
        RIGHT =2
        LEFT = 4
        MAXX = 760
        MINX = 20
        MAXY = 560
        MINY =80
        SNAKESTEP = 20
        TRUE = 1
        FALSE = 0

        ##### VARIABLES

        direction = RIGHT # 1=up,2=right,3=down,4=left
        snakexy =[300,400]
        snakelist =[[300,400],[280,400],[260,400]]
        counter =0
        score =0
        appleoncreen = 0
         #applexy = [0,0]
        newdirection = RIGHT
        snakedead = FALSE
        gameregulator = 6
        gamepaused = 0
        growsnake = 0  # added to grow tail by two each time 
        snakegrowunit = 2 # added to grow tail by two each time



        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(WINSIZE)
        pygame.display.set_caption('SNAKER')
        screen.fill(BLACK)



        ### Show initial Start Screen



        if showstartscreen == TRUE:
            showstartscreen = FALSE

            s =  [[180,120],[180,100],[160,100],[140,100],[120,100],[100,100],[100,120],[100,140],[100,160],[120,160],[140,160],[160,160],[180,160],[180,180],[180,200],[180,220],[160,220],[140,220],[120,220],[100,220],[100,200]]
            apple = [100,200]
            pygame.draw.rect(screen,GREEN,Rect(apple,BLOCKSIZE))
            pygame.display.flip()
            clock.tick(8)



        for e in s:
            pygame.draw.rect(screen,BLUE,Rect(e,BLOCKSIZE))
            pygame.display.flip()
            clock.tick(8)

        font =pygame.font.SysFont('arial', 64)
        text_surface =font.render('NAKER', True, BLUE)
        screen.blit(text_surface, (220,180))
        font=pygame.font.SysFont


























if __name__ == '__main__':
    main()