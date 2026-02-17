# Win Screen
# Shows when player health defeats boss room

import pygame
from scenes import base

class Winner(base.BaseScene):

    def __init__(self):
        super().__init__()

        # Load Static Files
        win_text = self.static_folder / "Images" / "winner.png"

        # Static Files to Pygame
        self.win_text = pygame.image.load(win_text).convert_alpha()

    def handle_events(self, events):
        pass

    def handle_updates(self):
        pass

    def handle_draw(self, window):
        window.fill((0,0,0))
        window.blit(self.win_text, (200,100))