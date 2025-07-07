import pygame
from src.constants import SIZE


class TileMap:
    def __init__(self, _map=list):
        self.map = _map
        self.size = SIZE
        self.tile_items = []
        self.set_tile_items()

    def set_tile_items(self):
        self.tile_items = [
            {
                "color": "black",
                "rect": [0, 0, self.size, self.size],
            },
            {
                "color": "white",
                "rect": [0, 0, self.size, self.size],
            },
        ]

    def on_render(self, surface):
        for row in range(len(self.map)):
            for collumn in range(len(self.map[row])):
                index_item = self.map[row][collumn]
                item = self.tile_items[index_item]
                rect = pygame.rect.Rect(item.get("rect"))
                rect.x, rect.y = [collumn * self.size, row * self.size]
                pygame.draw.rect(
                    surface=surface,
                    color=item.get("color"),
                    rect=rect,
                )
