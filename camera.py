import pygame
import settings

class PlayerCenterCamera(pygame.sprite.Group):
    """
    A class representing a camera that centers on a target sprite.

    Attributes:
    - display_surface (pygame.Surface): The surface to display the camera view.
    - half_width (float): Half of the width of the display surface.
    - half_height (float): Half of the height of the display surface.
    - ground_surface (pygame.Surface): The surface representing the ground.
    - ground_rect (pygame.Rect): The rectangle representing the ground surface.

    Methods:
    - center_target_camera(target: pygame.sprite.Sprite) -> None:
        Centers the camera on the target sprite.
    - camera_draw(player: pygame.sprite.Sprite) -> None:
        Draws the camera view on the display surface.
    """

    def __init__(self, ground_surface: pygame.Surface) -> None:
        """
        Initializes the PlayerCenterCamera object.

        Args:
        - ground_surface (pygame.Surface): The surface representing the ground.
        """
        pygame.sprite.Group.__init__(self)

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] / 2
        self.half_height = self.display_surface.get_size()[1] / 2

        self.ground_surface = ground_surface
        self.ground_rect = self.ground_surface.get_rect(topleft=(0, 0))

    def center_target_camera(self, target: pygame.sprite.Sprite) -> None:
        """
        Centers the camera on the target sprite.

        Args:
        - target (pygame.sprite.Sprite): The target sprite to center the camera on.
        """
        settings.global_offset.x = target.rect.centerx - self.half_width
        settings.global_offset.y = target.rect.centery - self.half_height

    def camera_draw(self, player: pygame.sprite.Sprite) -> None:
        """
        Draws the camera view on the display surface.

        Args:
        - player (pygame.sprite.Sprite): The player sprite to center the camera on.
        """
        self.center_target_camera(player)

        ground_offset = self.ground_rect.topleft - settings.global_offset
        self.display_surface.blit(self.ground_surface, ground_offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - settings.global_offset
            self.display_surface.blit(sprite.image, offset_pos)