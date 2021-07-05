import pygame
from pygame import display
from pygame import time
from pygame import math
from pygame.locals import *


pygame.init()

vec = math.Vector2

HEIGHT = 450
WIDTH = 400
ACC= 0.5
FRIC = -0.12
FPS= 60

FramePerSec = time.Clock()

displaysurface = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Game")

