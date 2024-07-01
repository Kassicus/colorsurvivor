import pygame
import random
import math

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
    
    def random_custom(self, channels: str, min_value: int = 0, max_value: int = 255) -> pygame.Color:
        red = 0
        green = 0
        blue = 0

        if 'r' in channels:
            red = random.randint(min_value, max_value)
        if 'g' in channels:
            green = random.randint(min_value, max_value)
        if 'b' in channels:
            blue = random.randint(min_value, max_value)

        color = pygame.Color(red, green, blue)

        return color
    
def get_vectors(origin: pygame.sprite.Sprite, target: pygame.sprite.Sprite) -> list:
    distance = [target.pos.x - origin.pos.x, target.pos.y - origin.pos.y]
    normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
    direction = [distance[0] / normal, distance[1] / normal]
    vectors = [direction[0] * origin.speed, direction[1] * origin.speed]

    return vectors

def get_pos_vectors(origin_pos: pygame.math.Vector2, target_pos: pygame.math.Vector2, speed: float) -> list:
    distance = [target_pos.x - origin_pos.x, target_pos.y - origin_pos.y]
    normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
    direction = [distance[0] / normal, distance[1] / normal]
    vectors = [distance[0] * speed, direction[1] * speed]

    return vectors

def get_distance(origin_pos, target_pos) -> float:
    distance = [target_pos.x - origin_pos.x, target_pos.y - origin_pos.y]
    normal = math.sqrt(distance[0] ** 2 + distance [1] ** 2)

    return normal

color = ColorLibrary()

events = None
world_reference = None

global_offset = pygame.math.Vector2()
delta_time = 0
fps_limit = 120