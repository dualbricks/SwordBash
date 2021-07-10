import pygame
import os
import constants

game = constants
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):

    def __init__(self, pos = vec(0, game.ground_value - 32)):
        super().__init__()

        self.idle = [pygame.image.load(os.path.join("assets", "animations", "idle", "tile000.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile001.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile002.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile003.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile004.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile005.png"))]
        self.idleLeft = []
        for frames in self.idle:
            self.idleLeft.append(pygame.transform.flip(frames, True, False))
        self.image = self.idle[0]
        self.rect = self.image.get_rect()
        self.running = False
        self.jumping = False
        self.pos = vec((pos.x, pos.y))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"
        self.type = "character"
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

        self.jumpLeft = []

        for frames in self.jump:
            self.jumpLeft.append(pygame.transform.flip(frames, True, False))

        self.jumpIndex = 0

    def update_idle(self):

        self.idleIndex += 1
        if self.idleIndex >= len(self.idle) * 5:
            self.idleIndex = 0

    def move(self):
        if self.pos.y >= game.ground_value:
            self.acc = vec(0, 0.5)
        # only move when speed is high
        if abs(self.vel.x) > 0.5:
            self.running = True
        else:
            self.running = False
        # Get key Input
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -game.ACC
            self.direction = "LEFT"
        elif pressed_keys[pygame.K_RIGHT]:
            self.acc.x = game.ACC
            self.direction = "RIGHT"
        else:
            self.acc.x = 0
            self.running = False

        # moving the position
        self.acc.x += self.vel.x * game.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # border up the character
        if self.pos.x > game.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = game.WIDTH
        self.runIndex += 1
        if self.runIndex >= len(self.runRight) * 4:
            self.runIndex = 0

        if not self.running:
            self.update_idle()
        # updating the rect
        if self.running and self.direction == "RIGHT":
            self.image = self.runRight[self.runIndex // 4]
        elif self.running and self.direction == "LEFT":
            self.image = self.runLeft[self.runIndex // 4]
        elif not self.running and self.direction == "RIGHT" and not self.jumping:
            self.image = self.idle[self.idleIndex // 5]
        else:
            self.image = self.idleLeft[self.idleIndex // 5]
        self.rect.topleft = self.pos

    def update_jump(self):
        self.jumping = True
        self.vel.y = -0.32
        self.pos += self.vel
        self.jumpIndex += 1
        if self.jumpIndex >= len(self.jump) * 5:
            self.jumpIndex = 0
        if self.jumping and self.direction == "RIGHT":
            self.image = self.jump[self.jumpIndex // 5]
        elif self.jumping and self.direction == "LEFT":
            self.image = self.jumpLeft[self.jumpIndex // 5]
        self.rect.topleft = self.pos


class TransformChar(pygame.sprite.Sprite):
    def __init__(self, pos=vec(0, 0)):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "animations", "running", "hero-walk-side-6.png"))
        self.rect = self.image.get_rect()
        self.running = False
        self.jumping = False
        self.pos = vec((pos.x, pos.y))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"
        self.type = "transform"

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
        elif pressed_keys[pygame.K_RIGHT]:
            self.acc.x = game.ACC
        else:
            self.acc.x = 0

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
        self.rect.topleft = self.pos



