import pygame
import camera
import player
import particle
import settings
import enemy
import random
import weapon
import images
import wall

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
        self.collidables = pygame.sprite.Group()
        self.wall_container = pygame.sprite.Group()

        self.walls = [
            [0, 0, 1, 20]
        ]

        self.world_camera.add(self.player)
        self.player.particle_system = particle.PlayerParticleSystem()

        self.player.weapons.append(weapon.RangeMultishot())

        self.create_enemies(10, "flyer follower")
        self.create_walls(self.walls)

    def create_enemies(self, count: int, etype: str) -> None:
        if etype == "follower":
            for c in range(count):
                c = enemy.FollowEnemy(random.randint(0, settings.SCREEN_WIDTH), random.randint(0, settings.SCREEN_HEIGHT))
                c.particle_system = particle.EnemyParticleSystem(c.pos.x, c.pos.y)
                self.world_camera.add(c)
                self.enemy_container.add(c)
        elif etype == "flyer follower":
            for c in range(count):
                c = enemy.FlyerEnemy(random.randint(0, settings.SCREEN_WIDTH), random.randint(0, settings.SCREEN_HEIGHT))
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
        padding = 10

        for e in self.enemy_container:
            for e2 in self.enemy_container:
                if e != e2:
                    if e.rect.colliderect(e2.rect):
                        e.pos.x += random.randint(-padding, padding)
                        e.pos.y += random.randint(-padding, padding)

    def player_wall_collisions(self) -> None:
        collision_tollerance = 15

        for c in self.collidables:
            if self.player.rect.colliderect(c.rect):
                if abs(self.player.rect.left - c.rect.right) < collision_tollerance:
                    self.player.vel.x = 0
                    self.player.pos.x = c.rect.right + self.player.rect.width / 2
                if abs(self.player.rect.right - c.rect.left) < collision_tollerance:
                    self.player.vel.x = 0
                    self.player.pos.x = c.rect.left - self.player.rect.width / 2
                if abs(self.player.rect.top - c.rect.bottom) < collision_tollerance:
                    self.player.vel.y = 0
                    self.player.pos.y = c.rect.bottom + self.player.rect.height / 2
                if abs(self.player.rect.bottom - c.rect.top) < collision_tollerance:
                    self.player.vel.y = 0
                    self.player.pos.y = c.rect.top - self.player.rect.height / 2

    def enemy_wall_collisions(self) -> None:
        collision_tollerance = 15

        for e in self.enemy_container:
            if "flyer" not in e.tag:
                for c in self.collidables:
                    if e.rect.colliderect(c.rect):
                        if abs(e.rect.left - c.rect.right) < collision_tollerance:
                            e.vel.x = 0
                            e.pos.x = c.rect.right + e.rect.width / 2
                        if abs(e.rect.right - c.rect.left) < collision_tollerance:
                            e.vel.x = 0
                            e.pos.x = c.rect.left - e.rect.width / 2
                        if abs(e.rect.top - c.rect.bottom) < collision_tollerance:
                            e.vel.y = 0
                            e.pos.y = c.rect.bottom + e.rect.height / 2
                        if abs(e.rect.bottom - c.rect.top) < collision_tollerance:
                            e.vel.y = 0
                            e.pos.y = c.rect.top - e.rect.height / 2

    def create_walls(self, wall_array: list) -> None:
        for point_array in range(len(wall_array)):
            w = wall.Wall(wall_array[point_array][0], wall_array[point_array][1], wall_array[point_array][2], wall_array[point_array][3])
            self.world_camera.add(w)
            self.collidables.add(w)
            self.wall_container.add(w)

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
        self.player_wall_collisions()
        self.enemy_wall_collisions()

        for e in self.enemy_container:
            if "follower" in e.tag:
                e.follow_player()