import pygame
import settings

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

    def update(self):
        self.cooldown -= 1

        if self.cooldown <= 0:
            self.use()
            self.cooldown = self.max_cooldown

    def use(self):
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
    
class MeleeKnife(MeleeBase):
    def __init__(self) -> None:
        super().__init__(200, "e", 5, 300)