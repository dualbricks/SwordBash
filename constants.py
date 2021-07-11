import os
import pygame

vec = pygame.math.Vector2
FPS = 60
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
ground_value = 400
ACC = 0.3
FRIC = -0.10
COUNT = 10
CLOCK = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg.png")), (WIDTH, HEIGHT))
ground = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "tile000.png")), (100, 100))


def bg_music():
    pygame.mixer.music.load(os.path.join("assets", "music", "8bit Stage3 Loop.wav"))
    pygame.mixer.music.play(-1, 0.0)


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos = vec(0, 0) ):
        super().__init__()
        self.pos = pos
        self.image = ground
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def render(self):
        WIN.blit(self.image, self.rect)


def staging():
    WIN.blit(background, (0, 0))

    for x in range(0, 900, 100):
        Platform(vec(x, ground_value)).render()


platform_group = pygame.sprite.Group().add(Platform())


