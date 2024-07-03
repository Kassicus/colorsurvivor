import pygame
import settings
import projectile

class MeleeBase():
    def __init__(self,
                 range: int,
                 direction: str,
                 damage: int,
                 cooldown: int
                 ) -> None:
        
        self.parent = settings.world_reference.player

        self.range = range
        self.direction = direction
        
        self.damage = damage
        self.damage_box = self.create_damage_box(self.direction)
        
        self.cooldown = cooldown
        self.max_cooldown = cooldown

    def update(self) -> None:
        self.cooldown -= 1

        if self.cooldown <= 0:
            self.use()
            self.cooldown = self.max_cooldown

    def use(self) -> None:
        self.damage_box = self.create_damage_box(self.direction)
        for e in settings.world_reference.enemy_container:
            if e.rect.colliderect(self.damage_box):
                e.health -= self.damage

    def create_damage_box(self, direction: str) -> pygame.Rect:
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
    def __init__(self,
                 range: int,
                 damage: int,
                 cooldown: int,
                 p_size: int,
                 p_speed: int,
                 p_color: pygame.Color
                 ) -> None:
        
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
        self.cooldown -= 1

        if self.cooldown <= 0:
            self.use()
            self.cooldown = self.max_cooldown

    def use(self) -> None:
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
    def __init__(self) -> None:
        super().__init__(200, "e", 5, 300)

class RangeMissle(RangeBase):
    def __init__(self) -> None:
        super().__init__(400, 5, 250, 5, 300, settings.color.green)

class RangeMultishot(RangeBase):
    def __init__(self) -> None:
        super().__init__(400, 5, 50, 5, 300, settings.color.green)
        self.multishot_count = 3