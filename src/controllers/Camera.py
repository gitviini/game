import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.Vector2(0,0)

        self.display_surface.blit()