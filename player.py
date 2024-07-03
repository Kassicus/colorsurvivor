import pygame
import settings
import drops

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(int(settings.SCREEN_WIDTH / 2), int(settings.SCREEN_HEIGHT / 2))
        self.vel = pygame.math.Vector2()
        self.speed = 250
        self.size = 40

        self.health = 5

        self.particle_system = None

        self.weapons = []
        self.inventory = pygame.sprite.Group()
        self.coins = 0

        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(settings.color.white)
        self.image.set_colorkey(settings.color.white)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        self.pos += self.vel * settings.delta_time
        self.rect.center = self.pos

        self.move()
        self.get_coins()
        
        if self.particle_system is not None:
            self.particle_system.update(self.pos.x, self.pos.y)

        for weapon in self.weapons:
            weapon.update()

    def move(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vel.x = -self.speed
        elif keys[pygame.K_d]:
            self.vel.x = self.speed
        else:
            self.vel.x = 0

        if keys[pygame.K_w]:
            self.vel.y = -self.speed
        elif keys[pygame.K_s]:
            self.vel.y = self.speed
        else:
            self.vel.y = 0

    def get_coins(self) -> int:
        for item in self.inventory:
            if isinstance(item, drops.CoinDrop):
                self.coins += item.value
                item.kill()