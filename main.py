import pygame
import character
import os
import constants

pygame.init()

# game_prefix
game = constants
# character
player = character.Player()


def main():
    # game.bg_music()
    run = True
    while run:
        game.staging()
        game.CLOCK.tick(game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        player.move()
        game.WIN.blit(player.image, player.rect)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
