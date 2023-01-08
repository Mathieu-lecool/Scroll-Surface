import pygame

class Scroll:

    def __init__(self, surface):
        self.surface = surface
        self.surf_size = surface.get_size()
        self.height = 250
        self.size = (self.surf_size[0], self.height)
        self.screen = pygame.Surface(self.size)
        self.y = 0

    def get_screen(self): return self.screen

    def mousewheel(self, event):
        if event.y == -1 and self.size[1] > self.surf_size[1]+abs(self.y): self.y -= 1
        elif self.y < 0: self.y += 1

    def update(self): self.surface.blit(self.screen, (0,self.y))
