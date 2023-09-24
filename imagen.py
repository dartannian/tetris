import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dibujar Rectángulos")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Lista para almacenar los rectángulos
rectangles = []

# Variables para controlar el rectángulo rojo
rect_x = 100
rect_y = 0
rect_width = 50
rect_height = 50
rect_speed = 2  # Velocidad de desplazamiento hacia abajo

# Función para dibujar rectángulos
def draw_rectangles():
    for rect in rectangles:
        pygame.draw.rect(screen, RED, rect)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Lógica para mover el rectángulo rojo
    rect_y += rect_speed

    # Comprueba si el rectángulo rojo ha llegado al final de la pantalla
    if rect_y >= screen_height:
        # Guarda el rectángulo en la lista y crea uno nuevo arriba
        rectangles.append(pygame.Rect(rect_x, rect_y - rect_height, rect_width, rect_height))
        rect_y = 0  # Reinicia la posición del nuevo rectángulo

    # Limpia la pantalla
    screen.fill(WHITE)

    # Dibuja los rectángulos
    draw_rectangles()
    print(screen.get_height())

    # Actualiza la pantalla
    pygame.display.flip()

# Finaliza Pygame
pygame.quit()
sys.exit()