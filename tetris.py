import pygame, sys, figureDrawer as fd, figureMove as fm
pygame.init()

#Definir colores 

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
TETRIS_BACKGROUND = (33,74,86)

# Tamaño de la ventana
ancho = 800
largo = 600
size = (ancho,largo)

# Coordenadas de la figura
coord_x = 400
coord_y = 0
figureType = ""

# Velocidad de movimiento
speed_y = 10
speed_x = 0


screen = pygame.display.set_mode(size)

# Se crea reloj para controlar los FPS del juego
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # ------------- Logica ------------------

    if(fm.stopFigure(coord_y,600,figureType)):
        speed_y = 0
    
    coord_y += speed_y

    #--------------Mover fichas------------
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speed_x = -10
        if event.key == pygame.K_RIGHT:
            speed_x = 10
        if event.key == pygame.K_DOWN:
            speed_y = 10
                 
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            speed_x = 0
        if event.key == pygame.K_RIGHT:
            speed_x = 0 
        if event.key == pygame.K_DOWN:
            speed_y = 0   

    coord_x += speed_x 
    coord_y += speed_y
    
    # ------------- Logica ------------------

    # Se define el color de fondo de la pantalla
    screen.fill(TETRIS_BACKGROUND)

    
    
    #------------ Zona de Dibujo--------------
    
    fd.drawL(screen,coord_x,coord_y)
    figureType = "L"
    #------------ Zona de Dibujo--------------

    # Metodo para actualizar pantalla
    pygame.display.flip()
    
    # Metodo para controlar los FPS del juego
    clock.tick(1)


