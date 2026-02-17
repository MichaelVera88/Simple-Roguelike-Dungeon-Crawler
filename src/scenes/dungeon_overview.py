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
        self.dungeon_room = pygame.image.load(dungeon_room).convert_alpha()
        self.dungeon_room_hover = pygame.image.load(dungeon_room_hover).convert_alpha()

        # Initialize Dungeon Generation
        self.dg = dungeon_generation.DungeonGeneration()
        self.current_room = self.dg.dungeon_start
        starting_rooms = self.dg.get_adjacent_rooms(self.current_room)
        self.dg.create_rooms(self.current_room, starting_rooms)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for row in self.dg.dungeon_layout:
                    for room in row:
                        if room is not None:
                            dungeon_room_hitbox = self.dungeon_room.get_rect(topleft=room.room_pos)
                            if dungeon_room_hitbox.collidepoint(pygame.mouse.get_pos()) and not room.entered:
                                    room.entered = True
                                    adjacent_rooms = self.dg.get_adjacent_rooms(room)
                                    self.dg.create_rooms(room, adjacent_rooms)
                                    self.current_room = room
                                    self.next_scene = "dungeon_room"

    def handle_updates(self):
        pass 

    def handle_draw(self, window):
        # Clear Window
        window.fill((0,0,0))

        # Display Discovered Rooms
        for row in self.dg.dungeon_layout:
            for room in row:
                if room is not None:
                    dungeon_room_hitbox = self.dungeon_room.get_rect(topleft=room.room_pos)
                    if dungeon_room_hitbox.collidepoint(pygame.mouse.get_pos()):
                        if not room.entered:
                            window.blit(self.dungeon_room_hover, dungeon_room_hitbox)
                        else:
                            window.blit(self.dungeon_room, room.room_pos)
                    else:
                        window.blit(self.dungeon_room, room.room_pos)
        
        # Current Dungeon Room Player is Inside
        x_coord, y_coord = self.current_room.room_pos
        x_coord += 12
        y_coord += 12
        window.blit(self.player_marker, (x_coord, y_coord))