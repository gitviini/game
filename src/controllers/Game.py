import pygame
from src.controllers.Entity import Entity
from src.controllers.TileMap import TileMap
from src.constants import SCREEN, SIZE

tilemap = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

class Game:
    def __init__(self):
        self.screen = pygame.Surface((1000,1000))
        self.display = pygame.display.set_mode(SCREEN)
        self.offset = pygame.Vector2(0, 0)
        self.entities = []
        self.tilemap = TileMap(tilemap)
        self.keys = []
        self.mouse_pos = pygame.Vector2(SCREEN[0] / 2, SCREEN[1] / 2)
        self._click = False
        self._running = True
        self._fps = 40
        self.key = False
        self.clock = pygame.time.Clock()
        self.camera = pygame.rect.Rect(0,0,SCREEN[0],SCREEN[1])

    def on_event(self, event=pygame.event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.KEYDOWN:
            self.key = True

        elif event.type == pygame.KEYUP:
            self.key = False

        if self.key == True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.mouse_pos = (self.mouse_pos[0], self.mouse_pos[1] - SIZE / 2)
            if keys[pygame.K_s]:
                self.mouse_pos = (self.mouse_pos[0], self.mouse_pos[1] + SIZE / 2)
            if keys[pygame.K_a]:
                self.mouse_pos = (self.mouse_pos[0] - SIZE / 2, self.mouse_pos[1])
            if keys[pygame.K_d]:
                self.mouse_pos = (self.mouse_pos[0] + SIZE / 2, self.mouse_pos[1])

        if event.type == pygame.MOUSEBUTTONDOWN:
            self._click = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self._click = False

        if self._click:
            self.mouse_pos = pygame.mouse.get_pos()
            print(self.mouse_pos)

    def on_loop(self):
        self.player.on_move(self.mouse_pos)
    
    def _on_render_collision(self):
        pass

    def on_render(self):
        self.screen.fill("black")

        self.tilemap.on_render(self.screen)

        for entity in self.entities:
            entity_screen_pos = entity.rect.move(-self.camera.x, -self.camera.y)
            print(f"entity: {entity.rect}")
            print(f"cam: {self.camera}")
            pygame.draw.rect(self.screen, entity.color, entity.rect)

        pygame.display.flip()

    def on_execute(self):
        self.entities.append(Entity("vini", "green", "player"))
        self.player = self.entities[0]

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
            self.camera.center = self.player.rect.center

            self.display.fill("purple")

            self.display.blit(self.screen, (0,0), self.camera)
            
            self.clock.tick(self._fps)
