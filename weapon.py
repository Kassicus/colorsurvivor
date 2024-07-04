import pygame
import settings
import projectile

class MeleeBase():
    """
    Base class for melee weapons.
    """

    def __init__(self,
                 range: int,
                 direction: str,
                 damage: int,
                 cooldown: int
                 ) -> None:
        """
        Initialize a MeleeBase object.

        Args:
            range (int): The range of the melee weapon.
            direction (str): The direction of the melee weapon.
            damage (int): The damage inflicted by the melee weapon.
            cooldown (int): The cooldown time of the melee weapon.
        """
        self.parent = settings.world_reference.player

        self.range = range
        self.direction = direction
        
        self.damage = damage
        self.damage_box = self.create_damage_box(self.direction)
        
        self.cooldown = cooldown
        self.max_cooldown = cooldown

    def update(self) -> None:
        """
        Update the cooldown of the melee weapon.
        """
        self.cooldown -= 1

        if self.cooldown <= 0:
            self.use()
            self.cooldown = self.max_cooldown

    def use(self) -> None:
        """
        Use the melee weapon to inflict damage on enemies within range.
        """
        self.damage_box = self.create_damage_box(self.direction)
        for e in settings.world_reference.enemy_container:
            if e.rect.colliderect(self.damage_box):
                e.health -= self.damage

    def create_damage_box(self, direction: str) -> pygame.Rect:
        """
        Create a damage box based on the direction of the melee weapon.

        Args:
            direction (str): The direction of the melee weapon.

        Returns:
            pygame.Rect: The damage box.
        """
        if direction == "n":
            r = pygame.Rect(self.parent.pos.x - 10, self.parent.pos.y - self.range, 20, self.range)
        elif direction == "s":
            r = pygame.Rect(self.parent.pos.x - 10, self.parent.pos.y, 20, self.range)
        elif direction == "e":
            r = pygame.Rect(self.parent.pos.x, self.parent.pos.y - 10, self.range, 20)
        elif direction == "w":
            r = pygame.Rect(self.parent.pos.x - self.range, self.parent.pos.y - 10, self.range, 20)

        return r
    
class RangeBase():
    """
    Base class for ranged weapons.
    """

    def __init__(self,
                 range: int,
                 damage: int,
                 cooldown: int,
                 p_size: int,
                 p_speed: int,
                 p_color: pygame.Color
                 ) -> None:
        """
        Initialize a RangeBase object.

        Args:
            range (int): The range of the ranged weapon.
            damage (int): The damage inflicted by the ranged weapon.
            cooldown (int): The cooldown time of the ranged weapon.
            p_size (int): The size of the projectiles fired by the ranged weapon.
            p_speed (int): The speed of the projectiles fired by the ranged weapon.
            p_color (pygame.Color): The color of the projectiles fired by the ranged weapon.
        """
        self.parent = settings.world_reference.player

        self.range = range
        
        self.damage = damage
        self.size = p_size
        self.speed = p_speed
        self.color = p_color
        
        self.cooldown = cooldown
        self.max_cooldown = cooldown

        self.multishot_count = 1

    def update(self) -> None:
        """
        Update the cooldown of the ranged weapon.
        """
        self.cooldown -= 1

        if self.cooldown <= 0:
            self.use()
            self.cooldown = self.max_cooldown

    def use(self) -> None:
        """
        Use the ranged weapon to fire projectiles at enemies within range.
        """
        shots = 0
        targets = []

        for e in settings.world_reference.enemy_container:
            if settings.get_distance(self.parent.pos, e.pos) < self.range:
                if e not in targets:
                    if shots < self.multishot_count:
                        p = projectile.Projectile(self.parent.pos.x, self.parent.pos.y, e.pos.x, e.pos.y, self.size, self.speed, self.damage, self.color)
                        settings.world_reference.world_camera.add(p)
                        settings.world_reference.friendly_projectiles.add(p)
                        targets.append(e)
                        shots += 1
    
class MeleeKnife(MeleeBase):
    """
    Class representing a melee knife weapon.
    """

    def __init__(self) -> None:
        """
        Initialize a MeleeKnife object.
        """
        super().__init__(200, "e", 5, 300)

class RangeMissle(RangeBase):
    """
    Class representing a ranged missile weapon.
    """

    def __init__(self) -> None:
        """
        Initialize a RangeMissle object.
        """
        super().__init__(400, 5, 250, 5, 300, settings.color.green)

class RangeMultishot(RangeBase):
    """
    Class representing a ranged multishot weapon.
    """

    def __init__(self) -> None:
        """
        Initialize a RangeMultishot object.
        """
        super().__init__(400, 3, 250, 5, 300, settings.color.green)
        self.multishot_count = 3