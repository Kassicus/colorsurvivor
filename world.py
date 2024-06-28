import pygame
import camera
import player
import particle
import settings
import enemy
import random

class World():
    def __init__(self, background_path: str) -> None:
        settings.world_reference = self

        self.display_surface = pygame.display.get_surface()
        self.world_background = pygame.image.load(background_path).convert_alpha()

        self.world_camera = camera.PlayerCenterCamera(self.world_background)
        self.player = player.Player()
        self.particle_group = pygame.sprite.Group()
        self.enemy_container = pygame.sprite.Group()

        self.world_camera.add(self.player)
        self.player.particle_system = particle.PlayerParticleSystem()

        self.create_enemies(5)

    def create_enemies(self, count: int) -> None:
        for c in range(count):
            c = enemy.FollowEnemy(random.randint(0, settings.SCREEN_WIDTH), random.randint(0, settings.SCREEN_HEIGHT), 20, 100)
            c.particle_system = particle.EnemyParticleSystem(c.pos.x, c.pos.y)
            self.world_camera.add(c)
            self.enemy_container.add(c)

    def draw(self) -> None:
        self.world_camera.camera_draw(self.player)

    def update(self) -> None:
        self.world_camera.update()
        self.particle_group.update()
        self.enemy_container.update()

        for e in self.enemy_container:
            if e.tag == "follower":
                e.follow_player()