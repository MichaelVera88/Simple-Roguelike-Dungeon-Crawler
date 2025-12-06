# Dungeon Overview Scene
# Scene shows birds-eye-view of the dungeon and available rooms to explore.

import pygame
from scenes import base

class DungeonOverview(base.BaseScene):
    def __init__(self):
        super().__init__()

        # Load Static Files
        player_marker = self.static_folder / "Images" / "UI" / "Dungeon" / "player_marker.png"
        dungeon_room = self.static_folder / "Images" / "UI" / "Dungeon" / "dungeon_room.png"

        # Static Files to Pygame
        self.player_marker = pygame.image.load(player_marker).convert_alpha()
        self.start_dungeon_room = pygame.image.load(dungeon_room).convert_alpha()

    def handle_events(self, events):
        pass

    def handle_updates(self):
        pass

    def handle_draw(self, window):
        # Clear Window
        window.fill((0,0,0))

        window.blit(self.start_dungeon_room, (275,425))
        window.blit(self.player_marker, (288,438))