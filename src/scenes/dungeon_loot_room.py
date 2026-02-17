# Dungeon Loot Room
# Scene for when a player enters a loot room.

import pygame
from scenes import base

class DungeonLootRoom(base.BaseScene):

    def __init__(self):
        super().__init__()

        # Load Static Files
        back_button = self.static_folder / "Images" / "UI" / "play_button.png"
        
        # Static Files to Pygame
        self.back_button = pygame.image.load(back_button).convert_alpha()
        self.back_button_hitbox = self.back_button.get_rect(topleft=(200,300))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_hitbox.collidepoint(pygame.mouse.get_pos()):
                    self.next_scene = "dungeon_overview"

    def handle_updates(self):
        pass

    def handle_draw(self, window):
        # Clear Window
        window.fill((0,0,0))

        window.blit(self.back_button, self.back_button_hitbox)