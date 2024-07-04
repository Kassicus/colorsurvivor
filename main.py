import pygame
import settings
import debug
import world

pygame.init()

class Game():
    """
    The main game class that controls the game loop and manages game objects.
    """

    def __init__(self) -> None:
        """
        Initializes the Game object.

        Creates the game window, sets up the debug interface, and loads the game world.
        """
        self.screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
        pygame.display.set_caption(settings.SCREEN_TITLE)

        self.running = True
        self.clock = pygame.time.Clock()
        settings.events = pygame.event.get()

        self.debug_interface = debug.DebugInterface()
        self.world = world.World("assets/backgrounds/test_map.png")

    def start(self) -> None:
        """
        Starts the game loop.

        Continuously updates, draws, and handles events until the game is exited.
        """
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self) -> None:
        """
        Handles game events.

        Checks for quit events and key presses to control game behavior.
        """
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
        """
        Draws game objects on the screen.

        Clears the screen, draws the game world, and optionally draws the debug interface.
        """
        self.screen.fill(settings.color.black)

        self.world.draw()

        if self.debug_interface.active:
            self.debug_interface.draw()

    def update(self) -> None:
        """
        Updates game objects.

        Updates the game world and the debug interface, and updates the display.
        """
        self.world.update()

        self.debug_interface.update(self.clock)            
        pygame.display.update()
        settings.delta_time = self.clock.tick(settings.fps_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()