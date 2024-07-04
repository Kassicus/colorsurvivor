import pygame
import settings

class Projectile(pygame.sprite.Sprite):
    def __init__(self,
                 x: int,
                 y: int,
                 target_x: int,
                 target_y: int,
                 size: int,
                 speed: float,
                 damage: int,
                 color: pygame.Color
                 ) -> None:
        """
        Initialize a Projectile object.

        Args:
            x (int): The x-coordinate of the projectile's starting position.
            y (int): The y-coordinate of the projectile's starting position.
            target_x (int): The x-coordinate of the projectile's target position.
            target_y (int): The y-coordinate of the projectile's target position.
            size (int): The size of the projectile.
            speed (float): The speed at which the projectile moves.
            damage (int): The amount of damage the projectile inflicts.
            color (pygame.Color): The color of the projectile.

        Returns:
            None
        """
        
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.target_pos = pygame.math.Vector2(target_x, target_y)

        self.speed = speed
        self.damage = damage
        self.color = color

        self.image = pygame.Surface([size, size])
        self.image.fill(self.color)
        #self.image.set_colorkey(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.vel.x, self.vel.y = settings.get_pos_vectors(self.pos, self.target_pos, self.speed)

    def update(self) -> None:
        """
        Update the position of the projectile.

        Returns:
            None
        """
        self.pos += self.vel * settings.delta_time
        self.rect.center = self.pos