import pygame
import settings
import drops
import random

class BaseEnemy(pygame.sprite.Sprite):
    """
    Base class for enemies in the game.
    """

    def __init__(self, x: int, y: int, size: int) -> None:
        """
        Initialize the BaseEnemy object.

        Args:
            x (int): The x-coordinate of the enemy's position.
            y (int): The y-coordinate of the enemy's position.
            size (int): The size of the enemy.

        Returns:
            None
        """
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.speed = 100
        self.health = 5

        self.particle_system = None
        self.drop_table = []
        self.drop_chance = 1

        self.image = pygame.Surface([size, size])
        self.image.fill(settings.color.red)
        self.image.set_colorkey(settings.color.red)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        """
        Update the enemy's position and check for death.

        Returns:
            None
        """
        self.pos += self.vel * settings.delta_time
        self.rect.center = self.pos

        if self.particle_system is not None:
            self.particle_system.update(self.pos.x, self.pos.y)

        if self.health <= 0:
            self.die()

    def die(self) -> None:
        """
        Handle the enemy's death, including dropping items.

        Returns:
            None
        """
        drop_draw = random.randint(1, 1)

        if drop_draw == self.drop_chance:
            drop = random.choice(self.drop_table)
            instance = drop(self.pos.x, self.pos.y)
            settings.world_reference.ground_items.add(instance)
            settings.world_reference.world_camera.add(instance)

        self.kill()


class FollowEnemy(BaseEnemy):
    """
    Enemy class that follows the player.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize the FollowEnemy object.

        Args:
            x (int): The x-coordinate of the enemy's position.
            y (int): The y-coordinate of the enemy's position.

        Returns:
            None
        """
        super().__init__(x, y, 20)

        self.tag = "follower"

        self.speed = 70
        self.health = 5

        self.drop_table.append(drops.HealthDrop)
        self.drop_table.append(drops.CoinDrop)

    def follow_player(self) -> None:
        """
        Make the enemy follow the player.

        Returns:
            None
        """
        self.vel.x, self.vel.y = settings.get_vectors(self, settings.world_reference.player)


class FlyerEnemy(BaseEnemy):
    """
    Enemy class that flies and follows the player.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize the FlyerEnemy object.

        Args:
            x (int): The x-coordinate of the enemy's position.
            y (int): The y-coordinate of the enemy's position.

        Returns:
            None
        """
        super().__init__(x, y, 20)

        self.tag = "flyer follower"

        self.speed = 100
        self.health = 3

        self.drop_table.append(drops.HealthDrop)
        self.drop_table.append(drops.CoinDrop)

    def follow_player(self) -> None:
        """
        Make the enemy follow the player.

        Returns:
            None
        """
        self.vel.x, self.vel.y = settings.get_vectors(self, settings.world_reference.player)