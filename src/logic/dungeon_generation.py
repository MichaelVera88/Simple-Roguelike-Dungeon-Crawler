# Dungeon Generation
# Node Data Structure that randomly creates rooms throughout dungeon.

import random

class Room():
    """
    Node class for all rooms in the dungeon.

    Attributes:
        entered (Boolean): Flag to determine if current room has already been entered by player.
        room_pos (Tuple): Position of the current room on screen
        layout_coords (Tuple): Coordinates of room within the 2D Dungeon Layout Array
    """

    def __init__(self, room_pos:tuple=(0,0), layout_coords:tuple=(0,0)):
        self.entered = False
        self.room_pos = room_pos
        self.layout_coords = layout_coords


class DungeonGeneration():
    """
    Class uses Room Class nodes to create and generate connected rooms.

    Attributes:
        start_dungeon_room_pos (Tuple): First dungeon room's position.
        dungeon_start (Room Object): First room of dungeon; Constant across all playthroughs.
        dungeon_layout (2D Array): A 5x5 grid layout for the dungeon rooms to spawn in.
    """

    def __init__(self):
        start_dungeon_room_pos = (275,425)
        start_dungeon_room_coords = (0,2)
        self.dungeon_start = Room(
            start_dungeon_room_pos,
            start_dungeon_room_coords)
        self.dungeon_start.entered = True
        self.dungeon_layout = [
                                [None, None, self.dungeon_start, None, None],
                                [None, None, None, None, None],
                                [None, None, None, None, None],
                                [None, None, None, None, None],
                                [None, None, None, None, None]
                                ]

    def get_adjacent_rooms(self, room:"Room") -> list:
        """
        Gets Adjacent Rooms from Dungeon Layout
        
        :param self: Self
        :param room: Current Room Object
        """

        x_room_coord, y_room_coord = room.layout_coords

        left_room = forward_room = right_room = None

        if 4 > x_room_coord > 0 and 4 > y_room_coord > 0:
            left_room = self.dungeon_layout[x_room_coord][y_room_coord + 1]
            forward_room = self.dungeon_layout[x_room_coord + 1][y_room_coord]
            right_room = self.dungeon_layout[x_room_coord][y_room_coord - 1]

        return [left_room, forward_room, right_room]

    def create_rooms(self, room:"Room", rooms:list) -> None:
        """
        Randomly creates new connected rooms depending on given adjacent rooms.
        
        :param self: Self
        :param room: Current Room Object
        :param rooms: List of Adjacent Rooms
        """
        
        x_room_coord, y_room_coord = room.layout_coords
        left_gen = forward_gen = right_gen = False

        # Check Left Room
        if random.randint(1, 2) == 2:
            if rooms[0] == None and 4 > y_room_coord > 0:
                new_left_room = Room(self.generate_left_room_pos(room.room_pos),
                                    self.generate_left_room_coords(room.layout_coords))
                self.dungeon_layout[x_room_coord][y_room_coord + 1] = new_left_room
                left_gen = True
        else:
            if rooms[0] == None and 4 > y_room_coord > 0:
                self.dungeon_layout[x_room_coord][y_room_coord + 1] = Room((-100,0), self.generate_left_room_coords(room.layout_coords))
        
        # Check Forward Room
        if random.randint(1, 2) == 2:
            if rooms[1] == None and 4 > x_room_coord >= 0:
                new_forward_room = Room(self.generate_forward_room_pos(room.room_pos),
                                    self.generate_forward_room_coords(room.layout_coords))
                self.dungeon_layout[x_room_coord + 1][y_room_coord] = new_forward_room
                forward_gen = True
        else:
            if rooms[1] == None and 4 > x_room_coord >= 0:
                self.dungeon_layout[x_room_coord + 1][y_room_coord] = Room((-100,0), self.generate_forward_room_coords(room.layout_coords))

        # Check Right Room
        if random.randint(1, 2) == 2:
            if rooms[2] == None and 4 > y_room_coord > 0:
                new_right_room = Room(self.generate_right_room_pos(room.room_pos),
                                    self.generate_right_room_coords(room.layout_coords))
                self.dungeon_layout[x_room_coord][y_room_coord - 1] = new_right_room
                right_gen = True
        else:
            if rooms[2] == None and 4 > y_room_coord > 0:
                self.dungeon_layout[x_room_coord][y_room_coord - 1] = Room((-100,0), self.generate_right_room_coords(room.layout_coords))
        
        if not any((left_gen, forward_gen, right_gen)):
            if rooms[1] == None and 4 > x_room_coord >= 0:
                new_forward_room = Room(self.generate_forward_room_pos(room.room_pos),
                                        self.generate_forward_room_coords(room.layout_coords))
                self.dungeon_layout[x_room_coord + 1][y_room_coord] = new_forward_room

    def generate_left_room_pos(self, room_pos:tuple) -> tuple:
        """
        Calculates the position of the left room relative to the current room.
        
        :param self: Self
        :param room_pos: Current Room Object Position
        """
        
        return tuple(x + y for x, y in zip(room_pos, (-50,0)))
    
    def generate_left_room_coords(self, room_coords:tuple) -> tuple:
        """
        Calculates the coordinates of the left room in the dungeon layout.
        
        :param self: Self
        :param room_pos: Current Room Coordinates
        """

        x, y = room_coords
        return (x, y + 1)
    
    def generate_forward_room_pos(self, room_pos:tuple) -> tuple:
        """
        Calculates the position of the ahead room relative to the current room.
        
        :param self: Self
        :param room_pos: Current Room Object Position
        """
        
        return tuple(x + y for x, y in zip(room_pos, (0,-50)))
    
    def generate_forward_room_coords(self, room_coords:tuple) -> tuple:
        """
        Calculates the coordinates of the forward room in the dungeon layout.
        
        :param self: Self
        :param room_pos: Current Room Coordinates
        """

        x, y = room_coords
        return (x + 1, y)

    def generate_right_room_pos(self, room_pos:tuple) -> tuple:
        """
        Calculates the position of the right room relative to the current room.
        
        :param self: Self
        :param room_pos: Current Room Object Position
        """
        
        return tuple(x + y for x, y in zip(room_pos, (50,0)))
    
    def generate_right_room_coords(self, room_coords:tuple) -> tuple:
        """
        Calculates the coordinates of the right room in the dungeon layout.
        
        :param self: Self
        :param room_pos: Current Room Coordinates
        """

        x, y = room_coords
        return (x, y - 1)

    