import pygame
pygame.__version__
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Bros - Nivel 1")

# Colores
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)

# Velocidad del juego
FPS = 60
clock = pygame.time.Clock()

# Cargar recursos
try:
    mario_img = pygame.image.load("assets/images/mario.png")
    enemy_img = pygame.image.load("assets/images/enemy.png")
    block_img = pygame.image.load("assets/images/block.png")
    background_img = pygame.image.load("assets/images/background.png")

    jump_sound = pygame.mixer.Sound("assets/sounds/jump.wav")
    theme_music = "assets/sounds/theme.mp3"
except pygame.error as e:
    print(f"Error cargando recursos: {e}")
    sys.exit()

# Escalar imágenes
mario_img = pygame.transform.scale(mario_img, (50, 50))  # Ajusta el tamaño de Mario
enemy_img = pygame.transform.scale(enemy_img, (35, 35))  # Ajusta el tamaño de los enemigos
block_img = pygame.transform.scale(block_img, (50, 50))  # Ajusta el tamaño de los bloques

# Iniciar música de fondo
pygame.mixer.music.load(theme_music)
pygame.mixer.music.play(-1)

# Clase Mario
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = mario_img
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = HEIGHT - 100
        self.vel_y = 0
        self.is_jumping = False

    def update(self):
        # Mover la captura de teclas aquí
        keys = pygame.key.get_pressed()

        # Movimiento a la derecha e izquierda
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Salto
        if keys[pygame.K_SPACE] and not self.is_jumping:
            jump_sound.play()
            self.is_jumping = True
            self.vel_y = -15

        # Gravedad
        self.vel_y += 1
        self.rect.y += self.vel_y

        # Limitar posición vertical
        if self.rect.y >= HEIGHT - 100:
            self.rect.y = HEIGHT - 100
            self.is_jumping = False

# Clase enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 2  # Movimiento hacia la izquierda
        if self.rect.right < 0:
            self.rect.left = WIDTH

# Clase bloque
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = block_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Instanciar objetos
mario = Mario()
enemy = Enemy(600, HEIGHT - 82)
block = Block(300, HEIGHT - 150)

# Grupos de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(mario, enemy, block)
    
# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar fondo
    screen.blit(background_img, (0, 0))

    # Actualizar sprites
    all_sprites.update()
    all_sprites.draw(screen)
    mario.update()
    
    pygame.display.flip()
    clock.tick(FPS)