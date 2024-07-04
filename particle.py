import pygame
import random
import settings

class Particle(pygame.sprite.Sprite):
    """
    Represents a particle in the game.

    Attributes:
    - pos: A Vector2 representing the position of the particle.
    - vel: A Vector2 representing the velocity of the particle.
    - lifetime: An integer representing the remaining lifetime of the particle.
    - color: A pygame.Color object representing the color of the particle.
    - image: A pygame.Surface object representing the image of the particle.
    - rect: A pygame.Rect object representing the bounding rectangle of the particle.
    """

    def __init__(self,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 color: pygame.Color,
                 min_life: int,
                 max_life: int) -> None:
        """
        Initializes a new instance of the Particle class.

        Parameters:
        - x: An integer representing the x-coordinate of the particle's position.
        - y: An integer representing the y-coordinate of the particle's position.
        - width: An integer representing the width of the particle's image.
        - height: An integer representing the height of the particle's image.
        - color: A pygame.Color object representing the color of the particle.
        - min_life: An integer representing the minimum lifetime of the particle.
        - max_life: An integer representing the maximum lifetime of the particle.
        """

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
        """
        Updates the particle's position and lifetime.
        """

        self.pos += self.vel * settings.delta_time
        self.rect.center = self.pos

        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()

class ParticleSystem(pygame.sprite.Sprite):
    """
    Represents a particle system in the game.

    Attributes:
    - pos: A Vector2 representing the position of the particle system.
    - image: A pygame.Surface object representing the image of the particle system.
    - rect: A pygame.Rect object representing the bounding rectangle of the particle system.
    - particle_container: A pygame.sprite.Group object containing all the particles in the system.
    - master_particle_container: A reference to the main particle container in the game.
    - particle_color: A pygame.Color object representing the color of the particles in the system.
    - max_particles: An integer representing the maximum number of particles in the system.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the ParticleSystem class.
        """

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
        """
        Creates particles and adds them to the particle system.

        Parameters:
        - x: An integer representing the x-coordinate of the spawn position.
        - y: An integer representing the y-coordinate of the spawn position.
        - count: An integer representing the number of particles to create.
        - min_particle_size: An integer representing the minimum size of the particles.
        - max_particle_size: An integer representing the maximum size of the particles.
        - particle_offset: An integer representing the maximum offset from the spawn position.
        - min_life: An integer representing the minimum lifetime of the particles.
        - max_life: An integer representing the maximum lifetime of the particles.
        - min_x_vel: A float representing the minimum x-axis velocity of the particles.
        - max_x_vel: A float representing the maximum x-axis velocity of the particles.
        - min_y_vel: A float representing the minimum y-axis velocity of the particles.
        - max_y_vel: A float representing the maximum y-axis velocity of the particles.
        """

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
    """
    Represents a particle system for the player in the game.

    Inherits from the ParticleSystem class.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the PlayerParticleSystem class.
        """

        super().__init__()

        self.spawn_pos = pygame.math.Vector2(int(settings.SCREEN_WIDTH / 2), int(settings.SCREEN_HEIGHT / 2))
        self.particle_color = settings.color.random_gray(min_value=120)
        self.create_particles(self.spawn_pos.x, self.spawn_pos.y, self.max_particles, 3, 5, 15, 20, 45, -40, 40, -40, 40)

    def update(self,
               x: int,
               y: int
               ) -> None:
        """
        Updates the player particle system.

        Parameters:
        - x: An integer representing the x-coordinate of the player's position.
        - y: An integer representing the y-coordinate of the player's position.
        """

        new_pos = pygame.math.Vector2(int(x), int(y))
        self.particle_color = settings.color.random_gray(min_value=120)
        new_count = self.max_particles - len(self.particle_container)
        self.create_particles(new_pos.x, new_pos.y, new_count, 3, 5, 15, 20, 45, -40, 40, -40, 40)

class EnemyParticleSystem(ParticleSystem):
    """
    Represents a particle system for an enemy in the game.

    Inherits from the ParticleSystem class.
    """

    def __init__(self,
                 init_x: int,
                 init_y: int
                 ) -> None:
        """
        Initializes a new instance of the EnemyParticleSystem class.

        Parameters:
        - init_x: An integer representing the initial x-coordinate of the enemy's position.
        - init_y: An integer representing the initial y-coordinate of the enemy's position.
        """

        super().__init__()

        self.max_particles = 50

        self.spawn_pos = pygame.math.Vector2(init_x, init_y)
        self.particle_color = settings.color.random_custom("r", min_value = 120)
        self.create_particles(self.spawn_pos.x, self.spawn_pos.y, self.max_particles, 3, 5, 8, 20, 45, -40, 40, -40, 40)

    def update(self,
               x: int,
               y: int
               ) -> None:
        """
        Updates the enemy particle system.

        Parameters:
        - x: An integer representing the x-coordinate of the enemy's position.
        - y: An integer representing the y-coordinate of the enemy's position.
        """

        new_pos = pygame.math.Vector2(int(x), int(y))
        self.particle_color = settings.color.random_custom("r", min_value = 120)
        new_count = self.max_particles - len(self.particle_container)
        self.create_particles(new_pos.x, new_pos.y, new_count, 3, 5, 8, 20, 45, -40, 40, -40, 40)