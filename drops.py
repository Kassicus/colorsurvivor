import pygame
import settings
import images

class BaseDrop(pygame.sprite.Sprite):
    def __init__(self,
                 x: int,
                 y: int,
                 ) -> None:
        
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)

        self.image = pygame.Surface([5, 5])
        self.image.fill((0, 255, 0))
        self.image.set_colorkey((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        if self.rect.colliderect(settings.world_reference.player.rect):
            self.pickup()

    def pickup(self) -> None:
        settings.world_reference.ground_items.remove(self)
        settings.world_reference.player.inventory.add(self)
        settings.world_reference.world_camera.remove(self)

class HealthDrop(BaseDrop):
    def __init__(self,
                 x: int,
                 y: int,
                 ) -> None:
        
        super().__init__(x, y)
        
        self.image = images.images["health"]

        self.health = 5

    def pickup(self) -> None:
        super().pickup()
        settings.world_reference.player.health += self.health

class CoinDrop(BaseDrop):
    def __init__(self,
                 x: int,
                 y: int
                 ) -> None:
        
        super().__init__(x, y)
        
        self.image = images.images["coin"]

        self.value = 1

    def pickup(self) -> None:
        super().pickup()