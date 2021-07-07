import pygame
import player
import os

pygame.init()

# game_prefix
FPS = 60
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SwordBash")
background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "bg.png")), (WIDTH, HEIGHT))
ground_value = 400

ground = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background", "tile000.png")), (100, 100))


def bg_music():
    pygame.mixer.music.load(os.path.join("assets", "music", "8bit Stage3 Loop.wav"))
    pygame.mixer.music.play(-1, 0.0)


def ground_floor():
    for x in range(0, 900, 100):
        WIN.blit(ground, (x, ground_value))


def main():
    clock = pygame.time.Clock()
    bg_music()
    run = True
    while run:
        for event in pygame.event.get():
            WIN.blit(background, (0, 0))
            ground_floor()
            pygame.display.update()
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


if __name__ == "__main__":
    main()
