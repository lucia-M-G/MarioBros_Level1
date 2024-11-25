import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 400
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mario Bros - Nivel 1")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Velocidad del juego
FPS = 60
clock = pygame.time.Clock()

# Mario (jugador)
mario = pygame.Rect(50, ALTO - 70, 40, 50)
velocidad_mario = 5
gravedad = 0.5
vel_y = 0
en_suelo = True

# Plataforma
plataformas = [pygame.Rect(0, ALTO - 20, ANCHO, 20),
               pygame.Rect(200, ALTO - 100, 100, 20),
               pygame.Rect(400, ALTO - 200, 100, 20),
               pygame.Rect(600, ALTO - 150, 150, 20)]

# Bandera final
bandera = pygame.Rect(700, ALTO - 70, 20, 70)