import pygame
import settings
import drops

class Player(pygame.sprite.Sprite):
    """
    Represents the player character in the game.

    Attributes:
        pos (pygame.math.Vector2): The position of the player.
        vel (pygame.math.Vector2): The velocity of the player.
        speed (int): The speed at which the player moves.
        size (int): The size of the player.
        health (int): The health of the player.
        particle_system (ParticleSystem): The particle system associated with the player.
        weapons (list): List of weapons the player has.
        inventory (pygame.sprite.Group): The inventory of the player.
        coins (int): The number of coins the player has.
        image (pygame.Surface): The image representing the player.
        rect (pygame.Rect): The rectangle representing the player's position and size.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Player class.
        """
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(int(settings.SCREEN_WIDTH / 2), int(settings.SCREEN_HEIGHT / 2))
        self.vel = pygame.math.Vector2()
        self.speed = 250
        self.size = 40

        self.health = 5
        self.max_health = 15

        self.particle_system = None

        self.weapons = []
        self.inventory = pygame.sprite.Group()
        self.coins = 0

        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(settings.color.white)
        self.image.set_colorkey(settings.color.white)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        """
        Updates the player's position and performs other necessary updates.
        """
        self.pos += self.vel * settings.delta_time
        self.rect.center = self.pos

        self.move()
        self.get_coins()
        
        if self.particle_system is not None:
            self.particle_system.update(self.pos.x, self.pos.y)

        for weapon in self.weapons:
            weapon.update()

        if self.health > self.max_health:
            self.health = self.max_health

    def move(self) -> None:
        """
        Handles the player's movement based on keyboard input.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vel.x = -self.speed
        elif keys[pygame.K_d]:
            self.vel.x = self.speed
        else:
            self.vel.x = 0

        if keys[pygame.K_w]:
            self.vel.y = -self.speed
        elif keys[pygame.K_s]:
            self.vel.y = self.speed
        else:
            self.vel.y = 0

    def get_coins(self) -> int:
        """
        Collects coins from the inventory and updates the player's coin count.
        
        Returns:
            int: The updated coin count.
        """
        for item in self.inventory:
            if isinstance(item, drops.CoinDrop):
                self.coins += item.value
                item.kill()
        
        return self.coins
