# Dungeon Generation
# Node Data Structure that randomly creates rooms throughout dungeon.

import random

class Room():
    """
    Node class for all rooms in the dungeon.

    Attributes:
        room_pos (Tuple): Position of the current room on screen
        left_room (Room Object): Pointer to the room on the left side of current room, if available.
        forward_room (Room Object): Pointer to the room on ahead of current room, if available.
        right_room (Room Object): Pointer to the room on the right side of current room, if available.
        children (list[Room Object]): List of all available rooms that is connected to current room.
    """

    def __init__(self, room_pos:tuple=(0,0), left_room:"Room"=None, forward_room:"Room"=None, right_room:"Room"=None):
        self.room_pos = room_pos
        self.left_room = left_room
        self.forward_room = forward_room
        self.right_room = right_room
        self.children = [self.left_room, self.forward_room, self.right_room]

class DungeonGeneration():
    """
    Class uses Room Class nodes to create and generate connected rooms.

    Attributes:
        dungeon_start (Room Object): First room of dungeon; Constant across all playthroughs.
        start_dungeon_room_pos (Tuple): First dungeon room's position.
    """
    def __init__(self):
        start_dungeon_room_pos = (275,425)
        self.dungeon_start = Room(
            start_dungeon_room_pos,
            Room(self.generate_left_room_pos(start_dungeon_room_pos), None, None, None),
            Room(self.generate_forward_room_pos(start_dungeon_room_pos), None, None, None),
            Room(self.generate_right_room_pos(start_dungeon_room_pos), None, None, None))

    def create_rooms(self, room:"Room") -> None:
        """
        Randomly creates new connected rooms to given room.
        
        :param self: Self
        :param room: Current Room Object
        """
        for child in range(len(room.children)):
            room.children[child] = random.choice([None, Room(None, None, None)])

    def generate_left_room_pos(self, room_pos:tuple) -> tuple:
        """
        Calculates the position of the left room relative to the current room.
        
        :param self: Self
        :param room_pos: Current Room Object Position
        """
        return tuple(x + y for x, y in zip(room_pos, (-50,0)))
    
    def generate_forward_room_pos(self, room_pos:tuple) -> tuple:
        """
        Calculates the position of the ahead room relative to the current room.
        
        :param self: Self
        :param room_pos: Current Room Object Position
        """
        return tuple(x + y for x, y in zip(room_pos, (0,-50)))
    
    def generate_right_room_pos(self, room_pos:tuple) -> tuple:
        """
        Calculates the position of the right room relative to the current room.
        
        :param self: Self
        :param room_pos: Current Room Object Position
        """
        return tuple(x + y for x, y in zip(room_pos, (50,0)))
    


    