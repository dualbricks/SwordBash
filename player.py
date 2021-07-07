import pygame
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

        self.runRight = [pygame.image.load(os.path.join("assets", "animations", "running", "tile000.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile001.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile002.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile003.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile004.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile005.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile006.png")),
                         pygame.image.load(os.path.join("assets", "animations", "running", "tile007.png"))]

        self.runRightIndex = 0

        self.runLeft = []

        for frames in self.runRight:
            self.runLeft.append(pygame.transform.flip(frames, True, False))

        self.runLeftIndex = 0

        self.jump = [pygame.image.load(os.path.join("assets", "animations", "jump", "tile000.png")),
                     pygame.image.load(os.path.join("assets", "animations", "jump", "tile001.png")),
                     pygame.image.load(os.path.join("assets", "animations", "fall", "tile000.png")),
                     pygame.image.load(os.path.join("assets", "animations", "fall", "tile001.png")),]

        self.jumpIndex = 0

    def update_idle(self):

        self.idleIndex += 1

        if self.idleIndex >= len(self.idle) * 5:
            self.idleIndex = 0

    def update_running_right(self):

        self.runRightIndex += 1

        if self.runRightIndex >= len(self.runRight) * 6:

            self.runRightIndex = 0

    def update_jumping(self):

        self.jumpIndex += 1

        if self.jumpIndex >= len(self.jump) * 5:
            self.jumpIndex = 0

    def update_running_left(self):

        self.runLeftIndex += 1

        if self.runLeftIndex >= len(self.runLeft) * 6:

            self.runLeftIndex = 0
