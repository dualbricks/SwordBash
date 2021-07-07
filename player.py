import pygame.sprite
import os


class Player():
    def __init__(self):

        self.idle = [pygame.image.load(os.path.join("assets", "animations", "idle", "tile000.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile001.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile002.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile003.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile004.png")),
                     pygame.image.load(os.path.join("assets", "animations", "idle", "tile005.png"))]

        self.idleIndex = 0

        self.idling = self.idle[self.idleIndex]

        self.run = [pygame.image.load(os.path.join("assets", "animations", "running", "tile000.png")),
                    pygame.image.load(os.path.join("assets", "animations", "running", "tile001.png")),
                    pygame.image.load(os.path.join("assets", "animations", "running", "tile002.png")),
                    pygame.image.load(os.path.join("assets", "animations", "running", "tile003.png")),
                    pygame.image.load(os.path.join("assets", "animations", "running", "tile004.png")),
                    pygame.image.load(os.path.join("assets", "animations", "running", "tile005.png")),
                    pygame.image.load(os.path.join("assets", "animations", "running", "tile006.png")),
                    pygame.image.load(os.path.join("assets", "animations", "running", "tile007.png"))]

        self.runIndex = 0

        self.running = self.run[self.idleIndex]

        self.jump = [pygame.image.load(os.path.join("assets", "animations", "jump", "tile000.png")),
                     pygame.image.load(os.path.join("assets", "animations", "jump", "tile001.png")),
                     pygame.image.load(os.path.join("assets", "animations", "fall", "tile000.png")),
                     pygame.image.load(os.path.join("assets", "animations", "fall", "tile001.png")),]

        self.jumpIndex = 0

        self.jumping = self.jump[self.jumpIndex]

    def update_idle(self):

        self.idleIndex += 1

        if self.idleIndex >= len(self.idle):
            self.idleIndex = 0

        self.idling = self.idle[self.idleIndex]

    def update_running(self):

        self.runIndex += 1

        if self.runIndex >= len(self.run):
            self.runIndex = 0

        self.running = self.run[self.runIndex]

    def update_jumping(self):

        self.jumpIndex += 1

        if self.jumpIndex >= len(self.jump):
            self.jumpIndex = 0

        self.jumping = self.jump[self.jumpIndex]