import pygame
import character
import os
import constants

pygame.init()

# game_prefix
game = constants
# character


def main():
    player = character.Player()
    # game.bg_music()
    run = True
    while run:
        game.staging()
        game.CLOCK.tick(game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    if player.type == "character":
                        player = character.TransformChar(player.pos)
                    else:
                        player = character.Player(player.pos)
                elif event.key == pygame.K_SPACE:
                    player.update_jump()
            if event.type == pygame.QUIT:
                run = False
        player.move()
        game.WIN.blit(player.image, player.rect)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
