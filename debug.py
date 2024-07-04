import pygame

from settings import *

class DebugInterface():
    """
    A class that represents the debug interface for the game.

    Attributes:
    - font: A pygame.font.Font object representing the font used for rendering text.
    - fps_text: A pygame.Surface object representing the rendered FPS text.
    - display_surface: A pygame.Surface object representing the game display surface.
    - active: A boolean indicating whether the debug interface is active or not.

    Methods:
    - get_fps_text(clock: pygame.time.Clock) -> pygame.Surface: Returns the rendered FPS text.
    - toggle_active() -> None: Toggles the active state of the debug interface.
    - draw() -> None: Draws the debug interface on the display surface.
    - update(clock: pygame.time.Clock) -> None: Updates the debug interface.

    """

    def __init__(self) -> None:
        """
        Initializes the DebugInterface object.

        """
        self.font = pygame.font.SysFont("Courier", 16)
        self.fps_text = None
        self.display_surface = pygame.display.get_surface()
        self.active = False

    def get_fps_text(self, clock: pygame.time.Clock) -> pygame.Surface:
        """
        Returns the rendered FPS text.

        Parameters:
        - clock: A pygame.time.Clock object representing the game clock.

        Returns:
        - text: A pygame.Surface object representing the rendered FPS text.

        """
        string = "FPS: " + str(int(clock.get_fps()))
        text = self.font.render(string, True, color.white)
        return text
    
    def toggle_active(self) -> None:
        """
        Toggles the active state of the debug interface.

        """
        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self) -> None:
        """
        Draws the debug interface on the display surface.

        """
        self.display_surface.blit(self.fps_text, (SCREEN_WIDTH - self.fps_text.get_width() - 10, 10))

    def update(self, clock: pygame.time.Clock) -> None:
        """
        Updates the debug interface.

        Parameters:
        - clock: A pygame.time.Clock object representing the game clock.

        """
        self.fps_text = self.get_fps_text(clock)