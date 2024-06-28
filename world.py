import pygame
import camera
import player
import particle
import settings

class World():
    def __init__(self, background_path: str) -> None:
        settings.world_reference = self

        self.display_surface = pygame.display.get_surface()
        self.world_background = pygame.image.load(background_path).convert_alpha()

        self.world_camera = camera.PlayerCenterCamera(self.world_background)
        self.player = player.Player()
        self.particle_group = pygame.sprite.Group()

        self.world_camera.add(self.player)
        self.player.particle_system = particle.PlayerParticleSystem()

    def draw(self) -> None:
        self.world_camera.camera_draw(self.player)

    def update(self) -> None:
        self.world_camera.update()
        self.particle_group.update()