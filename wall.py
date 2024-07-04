import pygame
import settings

class Wall(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """
        Initialize a Wall object.

        Args:
            x (int): The x-coordinate of the top-left corner of the wall.
            y (int): The y-coordinate of the top-left corner of the wall.
            width (int): The width of the wall in number of tiles.
            height (int): The height of the wall in number of tiles.
        """
        pygame.sprite.Sprite.__init__(self)

        self.size = 50

        self.pos = pygame.math.Vector2(x * self.size, y * self.size)

        self.image = pygame.Surface([width * self.size, height * self.size])
        self.image.fill(settings.color.white)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
