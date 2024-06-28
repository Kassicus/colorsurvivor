import pygame
import random
import settings

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
        self.rect.center = self.pos

    def update(self) -> None:
        self.pos += self.vel * settings.delta_time
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
        self.rect.center = self.pos

        self.particle_container = pygame.sprite.Group()
        self.master_particle_container = settings.world_reference.world_camera
        self.particle_color = settings.color.black
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
            y_range = (int(y - particle_offset), int(y + particle_offset))
            spawn_pos = pygame.math.Vector2(random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1]))
            p = Particle(spawn_pos.x, spawn_pos.y, particle_size, particle_size, self.particle_color, min_life, max_life)

            p.vel.x = random.uniform(min_x_vel, max_x_vel)
            p.vel.y = random.uniform(min_y_vel, max_y_vel)

            self.master_particle_container.add(p)
            self.particle_container.add(p)
            settings.world_reference.particle_group.add(p)

class PlayerParticleSystem(ParticleSystem):
    def __init__(self) -> None:
        super().__init__()

        self.spawn_pos = pygame.math.Vector2(int(settings.SCREEN_WIDTH / 2), int(settings.SCREEN_HEIGHT / 2))
        self.particle_color = settings.color.random_gray(min_value=120)
        self.create_particles(self.spawn_pos.x, self.spawn_pos.y, self.max_particles, 3, 5, 15, 20, 45, -40, 40, -40, 40)

    def update(self,
               x: int,
               y: int
               ) -> None:
        
        new_pos = pygame.math.Vector2(int(x), int(y))
        self.particle_color = settings.color.random_gray(min_value=120)
        new_count = self.max_particles - len(self.particle_container)
        self.create_particles(new_pos.x, new_pos.y, new_count, 3, 5, 15, 20, 45, -40, 40, -40, 40)

class EnemyParticleSystem(ParticleSystem):
    def __init__(self,
                 init_x: int,
                 init_y: int
                 ) -> None:
        super().__init__()

        self.max_particles = 50

        self.spawn_pos = pygame.math.Vector2(init_x, init_y)
        self.particle_color = settings.color.random_custom("r", min_value = 120)
        self.create_particles(self.spawn_pos.x, self.spawn_pos.y, self.max_particles, 3, 5, 8, 20, 45, -40, 40, -40, 40)

    def update(self,
               x: int,
               y: int
               ) -> None:
        
        new_pos = pygame.math.Vector2(int(x), int(y))
        self.particle_color = settings.color.random_custom("r", min_value = 120)
        new_count = self.max_particles - len(self.particle_container)
        self.create_particles(new_pos.x, new_pos.y, new_count, 3, 5, 8, 20, 45, -40, 40, -40, 40)