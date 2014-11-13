#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Timothy
#
# Created:     06/11/2014
# Copyright:   (c) Timothy 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import pygame, sys, os, random
    import pygame.freetype
    clock = pygame.time.Clock()
    pygame.init()
    FPS = 60
    DEVPINK = (255,0,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    YELLOW = (0,255,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    mainSurface = pygame.display.set_mode((1366,768))
    beeArray = []
    frame1 = pygame.image.load('drunkbee1.png')
    frame2 = pygame.image.load('drunkbee2.png')
    frame3 = pygame.image.load('drunkbee3.png')
    frame4 = pygame.image.load('drunkbee4.png')
    yOffset = 80
    xOffset = 80
    testFont = pygame.freetype.SysFont('Comic Sans MS',72,False,False)
    while True:
        mainSurface.fill(BLACK)
        testFont.render_to(mainSurface,(300,300),'Click on stuff',WHITE,None)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                beeArray.append(Bee(pygame.mouse.get_pos()[0] - xOffset,pygame.mouse.get_pos()[1] - yOffset))
        for bee in beeArray:
            if bee.frame < 15:
                mainSurface.blit(frame1,(bee.xPos,bee.yPos))
            elif bee.frame < 30:
                mainSurface.blit(frame2,(bee.xPos,bee.yPos))
            elif bee.frame < 45:
                mainSurface.blit(frame3,(bee.xPos,bee.yPos))
            else:
                mainSurface.blit(frame4,(bee.xPos,bee.yPos))
            bee.updateAppearance()
        pygame.display.update()
        clock.tick(60)

class Bee():
    xPos = 0
    yPos = 0
    frame = 0
    def __init__(self,xPos,yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.frame = 1
    def updateAppearance(self):
        if self.frame == 60:
            self.frame = 1
        else:
            self.frame = self.frame + 1
if __name__ == '__main__':
    from pygame.locals import *
    main()
