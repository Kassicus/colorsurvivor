import pygame
import random
import math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Color Survivor"

class ColorLibrary():
    """
    A class representing a color library.

    Attributes:
    - black: A pygame.Color object representing the color black.
    - white: A pygame.Color object representing the color white.
    - red: A pygame.Color object representing the color red.
    - green: A pygame.Color object representing the color green.
    - blue: A pygame.Color object representing the color blue.
    """

    def __init__(self) -> None:
        """
        Initialize the ColorLibrary class.
        """
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

    def random(self) -> pygame.Color:
        """
        Generate a random color.

        Returns:
        - A pygame.Color object representing a random color.
        """
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return color
    
    def random_gray(self, min_value: int = 0, max_value: int = 255) -> pygame.Color:
        """
        Generate a random grayscale color.

        Parameters:
        - min_value: The minimum value for each channel (default: 0).
        - max_value: The maximum value for each channel (default: 255).

        Returns:
        - A pygame.Color object representing a random grayscale color.
        """
        value = random.randint(min_value, max_value)
        color = pygame.Color(value, value, value)
        return color
    
    def random_custom(self, channels: str, min_value: int = 0, max_value: int = 255) -> pygame.Color:
        """
        Generate a random custom color.

        Parameters:
        - channels: A string representing the channels to randomize ('r', 'g', 'b').
        - min_value: The minimum value for each channel (default: 0).
        - max_value: The maximum value for each channel (default: 255).

        Returns:
        - A pygame.Color object representing a random custom color.
        """
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
    """
    Calculate the vectors between two sprites.

    Parameters:
    - origin: The origin sprite.
    - target: The target sprite.

    Returns:
    - A list containing the x and y components of the vectors.
    """
    distance = [target.pos.x - origin.pos.x, target.pos.y - origin.pos.y]
    normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
    direction = [distance[0] / normal, distance[1] / normal]
    vectors = [direction[0] * origin.speed, direction[1] * origin.speed]

    return vectors

def get_pos_vectors(origin_pos: pygame.math.Vector2, target_pos: pygame.math.Vector2, speed: float) -> list:
    """
    Calculate the vectors between two positions.

    Parameters:
    - origin_pos: The origin position.
    - target_pos: The target position.
    - speed: The speed of the origin.

    Returns:
    - A list containing the x and y components of the vectors.
    """
    distance = [target_pos.x - origin_pos.x, target_pos.y - origin_pos.y]
    normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
    direction = [distance[0] / normal, distance[1] / normal]
    vectors = [direction[0] * speed, direction[1] * speed]

    return vectors

def get_distance(origin_pos, target_pos) -> float:
    """
    Calculate the distance between two positions.

    Parameters:
    - origin_pos: The origin position.
    - target_pos: The target position.

    Returns:
    - The distance between the two positions.
    """
    distance = [target_pos.x - origin_pos.x, target_pos.y - origin_pos.y]
    normal = math.sqrt(distance[0] ** 2 + distance [1] ** 2)

    return normal

color = ColorLibrary()

events = None
world_reference = None

global_offset = pygame.math.Vector2()
delta_time = 0
fps_limit = 120