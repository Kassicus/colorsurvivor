import pygame
import random

from settings import *

class Particle(pygame.sprite.Sprite):
    def __init__(self,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 color: pygame.Color,
                 min_life: int,
                 max_life: int) -> None:

        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()

        self.lifetime = random.randint(min_life, max_life)

        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos()

    def update(self) -> None:
        self.pos += self.vel * delta_time
        self.rect.center = self.pos

        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()

class ParticleSystem(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(0, 0)
        self.image = pygame.Surface([0, 0])
        self.rect = self.image.get_rect()
        self.rect.center = self.pos()

        self.master_particle_container = world_reference.world_camera
        self.particle_container = pygame.sprite.Group()
        self.particle_color = color.black
        self.max_particles = 100

    def create_particles(self,
                         x: int,
                         y: int,
                         count: int,
                         min_particle_size: int,
                         max_particle_size: int,
                         particle_offset: int,
                         min_life: int,
                         max_life: int,
                         min_x_vel: float,
                         max_x_vel: float,
                         min_y_vel: float,
                         max_y_vel: float
                         ) -> None:
        
        for p in range(count):
            particle_size = random.randint(min_particle_size, max_particle_size)
            x_range = (int(x - particle_offset), int(x + particle_offset))
            y_range = (int(y - particle_offset), int(y - particle_offset))
            spawn_pos = pygame.math.Vector2(random.randint(x_range), random.randint(y_range))
            p = Particle(spawn_pos.x, spawn_pos.y, particle_size, particle_size, self.particle_color, min_life, max_life)

            p.vel.x = random.uniform(min_x_vel, max_x_vel)
            p.vel.y = random.uniform(min_y_vel, max_y_vel)

            self.master_particle_container.add(p)
            self.particle_container.add(p)

class PlayerParticleSystem(ParticleSystem):
    def __init__(self) -> None:
        super().__init__()

        self.spawn_pos = pygame.math.Vector2(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
        self.particle_color = color.random_gray(min_value=100)
        self.create_particles(self.spawn_pos.x, self.spawn_pos.y, self.max_particles, 3, 5, 15, 20, 45, -40, 40, -40, 40)

    def update(self,
               x: int,
               y: int
               ) -> None:
        
        new_pos = pygame.math.Vector2(int(x), int(y))
        self.particle_color = color.random_gray(min_value=100)
        new_count = self.max_particles - len(self.particle_container)
        self.create_particles(new_pos.x, new_pos.y, new_count, 3, 5, 15, 20, 45, -40, 40, -40, 40)