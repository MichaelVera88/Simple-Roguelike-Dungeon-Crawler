# Death Screen
# Shows when player health is 0

import pygame
from scenes import base

class Death(base.BaseScene):

    def __init__(self):
        super().__init__()

        # Load Static Files
        death_text = self.static_folder / "Images" / "you_died.png"

        # Static Files to Pygame
        self.death_text = pygame.image.load(death_text).convert_alpha()

    def handle_events(self, events):
        pass

    def handle_updates(self):
        pass

    def handle_draw(self, window):
        window.fill((0,0,0))
        window.blit(self.death_text, (200,100))