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
    game.bg_music()
    run = True
    while run:

        game.staging()
        for event in pygame.event.get():
            player.move()
            game.WIN.blit(player.image, player.rect)
            game.CLOCK.tick(game.FPS)
            if event.type == pygame.QUIT:
                run = False
            pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
