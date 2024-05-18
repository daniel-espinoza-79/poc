import pygame
import os

WIDTH = 800
HEIGHT = 600

RED = (250, 0, 0)
BACKGROUND_COLOR = (242, 242, 250)
IMAGE_WIDTH = 64  # Ancho deseado de la imagen
IMAGE_HEIGHT = 64  # Altura deseada de la imagen

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.count = 1
        self.images = [pygame.transform.scale(
            pygame.image.load(os.path.join(os.getcwd(), f'graphics/pepino/VxNJ6vM-{i}.png')).convert_alpha(),
            (IMAGE_WIDTH, IMAGE_HEIGHT)) for i in range(1, 11)]
        
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
    
    def update(self):
        self.image = self.images[self.count - 1]
        self.rect.x += 2
        self.count += 1

        if self.count > len(self.images):
            self.count = 1

        if self.rect.left > WIDTH:
            self.rect.right = 0

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Juego")

screen = pygame.display.set_mode((WIDTH, HEIGHT))

all_sprites = pygame.sprite.Group()
player = Jugador()
all_sprites.add(player)

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
