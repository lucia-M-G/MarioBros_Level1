import pygame
pygame.__version__
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

# Función para dibujar
def dibujar():
    screen.fill(BLANCO)

    # Dibujar plataformas
    for plataforma in plataformas:
        pygame.draw.rect(screen, NEGRO, plataforma)

    # Dibujar Mario
    pygame.draw.rect(screen, ROJO, mario)

    # Dibujar Bandera
    pygame.draw.rect(screen, AZUL, bandera)

    pygame.display.flip()
    
# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles de Mario
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario.x -= velocidad_mario
    if keys[pygame.K_RIGHT]:
        mario.x += velocidad_mario
    if keys[pygame.K_SPACE] and en_suelo:
        vel_y = -10
        en_suelo = False

    # Aplicar gravedad
    vel_y += gravedad
    mario.y += vel_y

    # Colisiones con el suelo y plataformas
    en_suelo = False
    for plataforma in plataformas:
        if mario.colliderect(plataforma) and vel_y > 0:
            mario.y = plataforma.y - mario.height
            vel_y = 0
            en_suelo = True

    # Colisiones con la bandera
    if mario.colliderect(bandera):
        print("¡Nivel completado!")
        pygame.quit()
        sys.exit()

    # Límite de la pantalla
    if mario.x < 0:
        mario.x = 0
    if mario.x > ANCHO - mario.width:
        mario.x = ANCHO - mario.width
    
    dibujar()
    clock.tick(FPS)