import pygame

images = {}

def load_images():
    """
    Load images for the game.

    This function loads images for different game objects such as coins and health drops.
    The images are stored in the `images` dictionary.

    Returns:
        None
    """
    images["coin"] = pygame.image.load("assets/drops/coin.png").convert_alpha()
    images["health"] = pygame.image.load("assets/drops/health.png").convert_alpha()