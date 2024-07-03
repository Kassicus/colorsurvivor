import pygame
import camera
import player
import particle
import settings
import enemy
import random
import weapon
import images

class World():
    def __init__(self, background_path: str) -> None:
        settings.world_reference = self
        images.load_images()

        self.display_surface = pygame.display.get_surface()
        self.world_background = pygame.image.load(background_path).convert_alpha()
        
        self.world_camera = camera.PlayerCenterCamera(self.world_background)
        self.player = player.Player()
        self.particle_group = pygame.sprite.Group()
        self.enemy_container = pygame.sprite.Group()
        self.friendly_projectiles = pygame.sprite.Group()
        self.ground_items = pygame.sprite.Group()

        self.world_camera.add(self.player)
        self.player.particle_system = particle.PlayerParticleSystem()

        self.player.weapons.append(weapon.RangeMultishot())

        self.create_enemies(50)

    def create_enemies(self, count: int) -> None:
        for c in range(count):
            c = enemy.FollowEnemy(random.randint(0, settings.SCREEN_WIDTH), random.randint(0, settings.SCREEN_HEIGHT))
            c.particle_system = particle.EnemyParticleSystem(c.pos.x, c.pos.y)
            self.world_camera.add(c)
            self.enemy_container.add(c)

    def friendly_projectile_collision(self) -> None:
        for e in self.enemy_container:
            for p in self.friendly_projectiles:
                if e.rect.colliderect(p.rect):
                    e.health -= p.damage
                    p.kill()

    def enemy_collision(self) -> None:
        for e in self.enemy_container:
            for e2 in self.enemy_container:
                if e != e2:
                    if e.rect.colliderect(e2.rect):
                        e.pos.x += random.randint(-5, 5)
                        e.pos.y += random.randint(-5, 5)

    def draw(self) -> None:
        self.world_camera.camera_draw(self.player)

    def update(self) -> None:
        self.world_camera.update()
        self.particle_group.update()
        self.enemy_container.update()
        self.friendly_projectiles.update()
        self.ground_items.update()

        self.friendly_projectile_collision()
        self.enemy_collision()

        for e in self.enemy_container:
            if e.tag == "follower":
                e.follow_player()