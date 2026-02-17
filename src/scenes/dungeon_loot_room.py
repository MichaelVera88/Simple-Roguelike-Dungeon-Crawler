# Dungeon Loot Room
# Scene for when a player enters a loot room.

import pygame
from scenes import base

class DungeonLootRoom(base.BaseScene):

    def __init__(self, player):
        super().__init__()

        # Load Static Files
        health_potion = self.static_folder / "Images" / "UI" / "Items" / "health_potion.png"
        
        # Static Files to Pygame
        self.health_potion_button = pygame.image.load(health_potion).convert_alpha()
        self.health_potion_button_hitbox = self.health_potion_button.get_rect(topleft=(200,300))

        self.player = player
        self.clicked_health_potion_button = False

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.health_potion_button_hitbox.collidepoint(pygame.mouse.get_pos()):
                    self.clicked_health_potion_button = True

    def handle_updates(self):
        if self.clicked_health_potion_button:
            self.player.health_potions += 1
            self.clicked_health_potion_button = False
            self.next_scene = "dungeon_overview"

    def handle_draw(self, window):
        # Clear Window
        window.fill((0,0,0))

        window.blit(self.health_potion_button, self.health_potion_button_hitbox)