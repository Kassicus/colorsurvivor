import pygame
import settings
import images

class BaseDrop(pygame.sprite.Sprite):
    """
    Base class for drops in the game.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize a BaseDrop object.

        Args:
            x (int): The x-coordinate of the drop's position.
            y (int): The y-coordinate of the drop's position.
        """
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)

        self.image = pygame.Surface([5, 5])
        self.image.fill((0, 255, 0))
        self.image.set_colorkey((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        """
        Update the drop's state.
        """
        if self.rect.colliderect(settings.world_reference.player.rect):
            self.pickup()

    def pickup(self) -> None:
        """
        Handle the pickup of the drop.
        """
        settings.world_reference.ground_items.remove(self)
        settings.world_reference.player.inventory.add(self)
        settings.world_reference.world_camera.remove(self)

class HealthDrop(BaseDrop):
    """
    Class for health drops in the game.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize a HealthDrop object.

        Args:
            x (int): The x-coordinate of the drop's position.
            y (int): The y-coordinate of the drop's position.
        """
        super().__init__(x, y)
        
        self.image = images.images["health"]

        self.health = 5

    def pickup(self) -> None:
        """
        Handle the pickup of the health drop.
        """
        super().pickup()
        settings.world_reference.player.health += self.health

class CoinDrop(BaseDrop):
    """
    Class for coin drops in the game.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize a CoinDrop object.

        Args:
            x (int): The x-coordinate of the drop's position.
            y (int): The y-coordinate of the drop's position.
        """
        super().__init__(x, y)
        
        self.image = images.images["coin"]

        self.value = 1

    def pickup(self) -> None:
        """
        Handle the pickup of the coin drop.
        """
        super().pickup()