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


# character
main_player = player.Player()
main_player.x = 0
main_player.y = ground_value - 32
speed = 5


def bg_music():
    pygame.mixer.music.load(os.path.join("assets", "music", "8bit Stage3 Loop.wav"))
    pygame.mixer.music.play(-1, 0.0)


def ground_floor():
    for x in range(0, 900, 100):
        WIN.blit(ground, (x, ground_value))


def actions(key_pressed):
    if key_pressed[pygame.K_RIGHT]:
        main_player.update_running_right()
        WIN.blit(main_player.runRight[main_player.runRightIndex // 6], (main_player.x + speed, main_player.y))
        main_player.x += speed
    elif key_pressed[pygame.K_SPACE]:
        main_player.update_jumping()
        WIN.blit(main_player.jump[main_player.jumpIndex // 6], (main_player.x, main_player.y - speed*2))
    elif key_pressed[pygame.K_LEFT]:
        main_player.update_running_left()
        WIN.blit(main_player.runLeft[main_player.runLeftIndex // 6], (main_player.x - speed, main_player.y))
        main_player.x -= speed
    else:
        main_player.update_idle()
        WIN.blit(main_player.idle[main_player.idleIndex // 6], (main_player.x, main_player.y))


def main():
    clock = pygame.time.Clock()
    bg_music()
    run = True
    while run:
        clock.tick(FPS)
        WIN.blit(background, (0, 0))
        ground_floor()
        for event in pygame.event.get():
            key_pressed = pygame.key.get_pressed()
            actions(key_pressed)
            pygame.display.update()
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


if __name__ == "__main__":
    main()
