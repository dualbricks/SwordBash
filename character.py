import pygame
import os
import constants

game = constants


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        vec = pygame.math.Vector2
        self.idle = [pygame.image.load(os.path.join("assets", "animations", "idle", "tile000.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile001.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile002.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile003.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile004.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile005.png"))]

        self.image = self.idle[0]
        self.rect = self.image.get_rect()
        self.running = False
        self.jumping = False
        self.pos = vec((0, game.ground_value-32))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"

        self.idleIndex = 0

        self.runRight = [pygame.image.load(os.path.join("assets", "animations", "running", "tile000.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile001.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile002.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile003.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile004.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile005.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile006.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile007.png"))]

        self.runIndex = 0

        self.runLeft = []

        for frames in self.runRight:
            self.runLeft.append(pygame.transform.flip(frames, True, False))

        self.jump = [pygame.image.load(os.path.join("assets", "animations", "jump", "tile000.png")),
                     pygame.image.load(os.path.join("assets", "animations", "jump", "tile001.png")),
                     pygame.image.load(os.path.join("assets", "animations", "fall", "tile000.png")),
                     pygame.image.load(os.path.join("assets", "animations", "fall", "tile001.png"))]

        self.jumpIndex = 0

    def idle(self):

        self.idleIndex += 1
        if self.idleIndex >= len(self.idle) * 5:
            self.idleIndex = 0

    def move(self):
        # only move when speed is high
        if abs(self.vel.x) > 0.5:
            self.running = True
        else:
            self.running = False
        # Get key Input
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -game.ACC
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = game.ACC

        # moving the position
        self.acc.x += self.vel.x * game.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # border up the character
        if self.pos.x > game.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = game.WIDTH

        # updating the rect
        self.rect.midbottom = self.pos

        self.runIndex += 1
        if self.runIndex >= len(self.runRight) * 6:
            self.runIndex = 0

    def jump(self):

        self.jumpIndex += 1
        if self.jumpIndex >= len(self.jump) * 5:
            self.jumpIndex = 0
