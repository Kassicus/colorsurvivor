import pygame

from settings import *

class DebugInterface():
    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Courier", 16)

        self.fps_text = None
        
        self.display_surface = pygame.display.get_surface()
        self.active = False

    def get_fps_text(self, clock: pygame.time.Clock) -> pygame.Surface:
        string = "FPS: " + str(int(clock.get_fps()))
        text = self.font.render(string, True, color.white)
        return text
    
    def toggle_active(self) -> None:
        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self) -> None:
        self.display_surface.blit(self.fps_text, (SCREEN_WIDTH - self.fps_text.get_width() - 10, 10))

    def update(self, clock: pygame.time.Clock) -> None:
        self.fps_text = self.get_fps_text(clock)