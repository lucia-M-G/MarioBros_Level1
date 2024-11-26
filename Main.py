import pygame
pygame.__version__
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Bros - Nivel 1")

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
        self.gravity = 1
        self.jump_speed = -15
        self.speed = 2.5
        # Contador de saltos
        self.jump_count = 0

    def update(self, blocks):
        is_below_block = False

        # Mover la captura de teclas aquí
        keys = pygame.key.get_pressed()

        # Movimiento a la derecha e izquierda
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Verificar si hay un bloque debajo de Mario
        for block in blocks:
            # Verifica la colisión abajo
            if self.rect.colliderect(block.rect.move(0, self.rect.height)):
                is_below_block = True
        
        # Salto
        if keys[pygame.K_UP] and not self.is_jumping:
            # Verificar si NO está debajo de un bloque
            if not is_below_block:
                jump_sound.play()
                self.is_jumping = True
                self.vel_y = self.jump_speed
                self.jump_count += 1

        # Gravedad
        if self.is_jumping:
            # Aplica gravedad
            self.vel_y += self.gravity 
        
        # Actualizar la posición vertical de Mario
        self.rect.y += self.vel_y

        # Detectar colisión con bloques
        # Reinicia la variable para cada actualización
        is_below_block = False
        
        # Detectar colisión con bloques
        for block in blocks:
            if self.rect.colliderect(block.rect):
                # Solo si Mario está cayendo
                if self.vel_y >= 0: 
                    # Colisión con el bloque, Mario se queda encima
                    self.rect.bottom = block.rect.top
                    self.is_jumping = False
                    self.vel_y = 0
                    # Indica que Mario está en un bloque
                    is_below_block = True
                    self.jump_count = 0
                    # Salimos del bucle si hay colisión
                    break

        # Si no hay colisión con bloques, aplicar gravedad
        if not is_below_block and self.rect.bottom < HEIGHT:
            self.vel_y += self.gravity

        # Limitar posición vertical
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.is_jumping = False
            self.vel_y = 0
            self.jump_count = 0
        
        # Limitar posición horizontal
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0 

# Clase enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Movimiento hacia la izquierda
        self.rect.x -= 1
        if self.rect.right < 0:
            self.rect.left = WIDTH

# Clase bloque
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = block_img
        self.rect = self.image.get_rect()
        self.rect.x = x - 60
        self.rect.y = y

        # Ajustar el ancho del rectángulo de colisión
        self.rect.width -= 10

# Instanciar objetos
mario = Mario()
enemy = Enemy(600, HEIGHT - 82)
block = Block(300, HEIGHT - 150)

# Grupos de sprites
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
all_sprites.add(mario, enemy, block)
blocks.add(block)
    
# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar fondo
    screen.blit(background_img, (0, 0))

    # Actualizar sprites
    mario.update(blocks)
    enemy.update()

    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)