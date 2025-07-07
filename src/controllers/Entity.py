import pygame
from math import floor, fabs
from src.constants import SIZE, SCREEN


class Entity:
    def __init__(self, name=str, color=str, entity_type=str):
        self.size = [SIZE, SIZE]
        self.name = name
        self.color = color
        self.entity_type = entity_type
        self.speed = 5
        self.vel = pygame.Vector2(0, 0)
        self.pos = pygame.Vector2(0, 0)
        self.ref = pygame.rect.Rect(self.pos.x, self.pos.y, self.size[0], self.size[1])
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, self.size[0], self.size[1])

    def on_move(self, mouse_pos=tuple[int, int]):
        self.ref.x, self.ref.y = (
            floor((mouse_pos[0] - SCREEN[0] / 2) / self.size[0]) * self.size[0],
            floor((mouse_pos[1] - SCREEN[1] / 2) / self.size[1]) * self.size[1],
        )
    
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.on_wake()

    def on_wake(self):
        if self.rect.x != self.ref.x or self.rect.y != self.ref.y:
            x = self.ref.x - self.rect.x
            y = self.ref.y - self.rect.y
            x /= fabs(x) if x != 0 else 1
            y /= fabs(y) if y != 0 else 1
            self.vel.x, self.vel.y = x * self.speed, y * self.speed
            self.pos.x += self.vel.x
            self.pos.y += self.vel.y
