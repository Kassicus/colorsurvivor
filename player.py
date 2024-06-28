import pygame

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
        self.vel = pygame.math.Vector2()
        self.speed = 250
        self.size = 40

        self.particle_system = None

        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(color.white)
        self.image.set_colorkey(color.white)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos()

    def update(self) -> None:
        self.pos += self.vel * delta_time
        self.rect.center = self.pos

        self.move()
        
        if self.particle_system is not None:
            self.particle_system.update(self.pos.x, self.pos.y)

    def move(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vel.x -= self.speed
        elif keys[pygame.K_d]:
            self.vel.x += self.speed
        else:
            self.vel.x = 0

        if keys[pygame.K_w]:
            self.vel.y -= self.speed
        elif keys[pygame.K_s]:
            self.vel.y += self.speed
        else:
            self.vel.y = 0