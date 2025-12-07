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
        dungeon_room_hover = self.static_folder / "Images" / "UI" / "Dungeon" / "dungeon_room_hover.png"

        # Static Files to Pygame
        self.player_marker = pygame.image.load(player_marker).convert_alpha()
        self.start_dungeon_room = pygame.image.load(dungeon_room).convert_alpha()
        self.dungeon_room = pygame.image.load(dungeon_room).convert_alpha()
        self.dungeon_room_hover = pygame.image.load(dungeon_room_hover).convert_alpha()

        # Initialize Dungeon Generation
        self.dg = dungeon_generation.DungeonGeneration()
        self.current_room = self.dg.dungeon_start

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, room in enumerate(self.current_room.children):
                    dungeon_room_hitbox = self.dungeon_room.get_rect(topleft=room.room_pos)
                    if dungeon_room_hitbox.collidepoint(pygame.mouse.get_pos()):
                        match index:
                            case 0:
                                print("Left Room Selected")
                            case 1:
                                print("Forward Room Selected")
                            case 2:
                                print("Right Room Selected")
                        self.next_scene = "dungeon_room"

    def handle_updates(self):
        pass 

    def handle_draw(self, window):
        # Clear Window
        window.fill((0,0,0))

        # Starting Dungeon Room
        window.blit(self.start_dungeon_room, self.dg.dungeon_start.room_pos)

        # Display connecting rooms from current room
        for room in self.current_room.children:
            dungeon_room_hitbox = self.dungeon_room.get_rect(topleft=room.room_pos)
            if dungeon_room_hitbox.collidepoint(pygame.mouse.get_pos()):
                window.blit(self.dungeon_room_hover, dungeon_room_hitbox)
            else:
                window.blit(self.dungeon_room, room.room_pos)

        window.blit(self.player_marker, (288,438))