# Dungeon Overview Scene
# Scene shows birds-eye-view of the dungeon and available rooms to explore.

import pygame
from scenes import base
from logic import dungeon_generation

class DungeonOverview(base.BaseScene):
    def __init__(self):
        super().__init__()

        # Load Static Files
        player_marker = self.static_folder / "Images" / "UI" / "Dungeon" / "player_marker.png"
        dungeon_room = self.static_folder / "Images" / "UI" / "Dungeon" / "dungeon_room.png"

        # Static Files to Pygame
        self.player_marker = pygame.image.load(player_marker).convert_alpha()
        self.start_dungeon_room = pygame.image.load(dungeon_room).convert_alpha()
        self.dungeon_room = pygame.image.load(dungeon_room).convert_alpha()

        # Initialize Dungeon Generation
        self.dg = dungeon_generation.DungeonGeneration()
        self.current_room = self.dg.dungeon_start

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for child in self.current_room.children:
                    if child is None:
                        print("None")
                    else:
                        print("Room Generated")

    def handle_updates(self):
        pass 

    def handle_draw(self, window):
        # Clear Window
        window.fill((0,0,0))

        window.blit(self.start_dungeon_room, self.dg.dungeon_start.room_pos)
        for room in self.current_room.children:
            window.blit(self.dungeon_room, room.room_pos)
        window.blit(self.player_marker, (288,438))