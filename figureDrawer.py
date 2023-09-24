import pygame, sys, figureDrawer


#Definir colores 

BLACK = (0,0,0)
GRAY = (178,178,178)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
TETRIS_BACKGROUND = (33,74,86)
TETRIS_MARGIN = (250,205,29)

def drawBoard(surface):
    for x in range(0,800,10):
        pygame.draw.line(surface, BLACK, (x,0), (x,600), 2)
        pygame.draw.line(surface, BLACK, (0,x), (800,x), 2)



def drawZ(surface,coord_x,coord_y,orientation):
    if orientation == 0:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        drawBoard(surface)
    elif orientation == 1:
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y + 10, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10, coord_y - 10, 10, 10)) 
        drawBoard(surface)  
    elif orientation == 2:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        drawBoard(surface)     
    elif orientation == 3:
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y + 10, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10, coord_y - 10, 10, 10))  
        drawBoard(surface)  

def drawS(surface,coord_x,coord_y,orientation):
    if orientation == 0:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y + 10,10,10))
        drawBoard(surface)
    elif orientation == 1:
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y - 10, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10, coord_y + 10, 10, 10)) 
        drawBoard(surface)  
    elif orientation == 2:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y + 10,10,10))
        drawBoard(surface)     
    elif orientation == 3:
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y - 10, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10, coord_y + 10, 10, 10)) 
        drawBoard(surface)  

def drawT(surface,coord_x,coord_y, orientation):
    if orientation == 0:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        drawBoard(surface)
    elif orientation == 1:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y - 10,10,10))
        drawBoard(surface)
    elif orientation == 2:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10 ,coord_y,10,10))
        drawBoard(surface)    
    elif orientation == 3:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y - 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10 ,coord_y,10,10))
        drawBoard(surface)   


def drawL(surface,coord_x,coord_y, orientation):
    if orientation == 0:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y + 10,10,10))
        drawBoard(surface)
    elif orientation == 1:
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y - 10, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y + 10, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10, coord_y + 10, 10, 10)) 
        drawBoard(surface)  
    elif orientation == 2:
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y + 10, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x + 20, coord_y, 10, 10)) 
        drawBoard(surface)      
    elif orientation == 3:
        pygame.draw.rect(surface, GREEN, (coord_x - 10, coord_y - 10, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y - 10, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y, 10, 10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y + 10, 10, 10))
        drawBoard(surface)
   

def drawJ(surface,coord_x,coord_y, orientation):
    if orientation == 0:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y + 10,10,10))
        drawBoard(surface)
    elif orientation == 1:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y - 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y - 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x, coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        drawBoard(surface)
    elif orientation == 2:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 20 ,coord_y,10,10))
        drawBoard(surface)  
    elif orientation == 3:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y - 10,10,10))
        drawBoard(surface)    
        

def drawI(surface,coord_x,coord_y, orientation):
    if orientation == 0:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 20,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y + 10,10,10))
        drawBoard(surface)    
    elif orientation == 1:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y - 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y - 20,10,10))
        drawBoard(surface)   
    elif orientation == 2:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 20,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x - 10,coord_y + 10,10,10))
        drawBoard(surface)  
    elif orientation == 3:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y - 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y - 20,10,10))
        drawBoard(surface)         
             

def drawO(surface,coord_x,coord_y, orientation):
    if orientation == 0:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        drawBoard(surface)
    if orientation == 1:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        drawBoard(surface)  
    if orientation == 2:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        drawBoard(surface) 
    if orientation == 3:
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x,coord_y + 10,10,10))
        pygame.draw.rect(surface, GREEN, (coord_x + 10,coord_y + 10,10,10))
        drawBoard(surface)     


def drawRandomFigure(surface,coord_x,coord_y,orientation, case):
    if case == 1:
        drawZ(surface,coord_x, coord_y, orientation)
    if case == 2:
        drawS(surface,coord_x, coord_y, orientation)
    if case == 3:
        drawT(surface,coord_x, coord_y, orientation)
    if case == 4:
        drawL(surface,coord_x, coord_y, orientation)
    if case == 5:
        drawJ(surface,coord_x, coord_y, orientation)
    if case == 6:
        drawI(surface,coord_x, coord_y, orientation)
    if case == 7:
        drawO(surface,coord_x, coord_y, orientation)

def drawMargin(surface,coord_x,coord_y):
    for i in range(250):
        pygame.draw.rect(surface, TETRIS_MARGIN, (coord_x + i,coord_y,10,10))
        pygame.draw.rect(surface, TETRIS_MARGIN, (coord_x + i,coord_y + 400,10,10))
        i += 10
    for i in range(400):
        pygame.draw.rect(surface, TETRIS_MARGIN, (coord_x,coord_y + i,10,10))
        pygame.draw.rect(surface, TETRIS_MARGIN, (coord_x + 250,coord_y + i,10,10))
        i += 10

