import pygame
import debug
import world

from settings import *

pygame.init()

class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption(SCREEN_TITLE)

        self.running = True
        self.clock = pygame.time.Clock()
        events = pygame.event.get()

        self.debug_interface = debug.DebugInterface()
        self.world = world.World("assets/backgrounds/test.png")

    def start(self) -> None:
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self) -> None:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                if event.key == pygame.K_TAB:
                    self.debug_interface.toggle_active()

    def draw(self) -> None:
        self.screen.fill(color.black)

        self.world.draw()

        if self.debug_interface.active:
            self.debug_interface.draw()

    def update(self) -> None:
        self.world.update()

        self.debug_interface.update(self.clock)            
        pygame.display.update()
        delta_time = self.clock.tick(fps_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()