import pygame
import settings

class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self,
                 x: int,
                 y: int,
                 size: int
                 ) -> None:
        
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.speed = 100
        self.health = 5

        self.particle_system = None

        self.image = pygame.Surface([size, size])
        self.image.fill(settings.color.red)
        self.image.set_colorkey(settings.color.red)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        self.pos += self.vel * settings.delta_time
        self.rect.center = self.pos

        if self.particle_system is not None:
            self.particle_system.update(self.pos.x, self.pos.y)

        if self.health <= 0:
            self.kill()

class FollowEnemy(BaseEnemy):
    def __init__(self,
                 x: int,
                 y: int,
                 size: int,
                 speed: float
                 ) -> None:
        
        super().__init__(x, y, size)
    
        self.tag = "follower"

        self.speed = speed
        self.health = 5

    def follow_player(self) -> None:
        self.vel.x = settings.get_vectors(self, settings.world_reference.player)[0]
        self.vel.y = settings.get_vectors(self, settings.world_reference.player)[1]