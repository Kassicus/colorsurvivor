import pygame

images = {}

def load_images():
    images["coin"] = pygame.image.load("assets/drops/coin.png").convert_alpha()
    images["health"] = pygame.image.load("assets/drops/health.png").convert_alpha()