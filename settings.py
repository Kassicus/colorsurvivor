import pygame
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Color Suvivor"

class ColorLibrary():
    def __init__(self) -> None:
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

    def random(self) -> pygame.Color:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return color
    
    def random_gray(self, min_value: int = 0, max_value: int = 255) -> pygame.Color:
        value = random.randint(min_value, max_value)
        color = pygame.Color(value, value, value)
        return color
    
    def random_custom(self, channels: str) -> pygame.Color:
        red = 0
        green = 0
        blue = 0

        if 'r' in channels:
            red = random.randint(0, 255)
        if 'g' in channels:
            green = random.randint(0, 255)
        if 'b' in channels:
            blue = random.randint(0, 255)

        color = pygame.Color(red, green, blue)

        return color

color = ColorLibrary()
events = None
global_offset = pygame.math.Vector2()
delta_time = 0
fps_limit = 120