import pygame
import settings
import debug
import world

pygame.init()

class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
        pygame.display.set_caption(settings.SCREEN_TITLE)

        self.running = True
        self.clock = pygame.time.Clock()
        settings.events = pygame.event.get()

        self.debug_interface = debug.DebugInterface()
        self.world = world.World("assets/backgrounds/test_map.png")

    def start(self) -> None:
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self) -> None:
        settings.events = pygame.event.get()

        for event in settings.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                if event.key == pygame.K_TAB:
                    self.debug_interface.toggle_active()

    def draw(self) -> None:
        self.screen.fill(settings.color.black)

        self.world.draw()

        if self.debug_interface.active:
            self.debug_interface.draw()

    def update(self) -> None:
        self.world.update()

        self.debug_interface.update(self.clock)            
        pygame.display.update()
        settings.delta_time = self.clock.tick(settings.fps_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()