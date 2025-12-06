# Base Scene
# Template class for the rest of the scenes in the game.

from pathlib import Path

class BaseScene:

    def __init__(self):
        current_folder = Path(__file__).resolve().parent
        self.static_folder = current_folder.parent.parent / "Static"

        self.next_scene = None

    def events(self, events):
        """
        Handles Player Inputs.
        
        :param self: Self
        :param events: Pygame Events Listener
        """
        pass

    def update(self):
        """
        Handles Animations & Logic.
        
        :param self: Self
        """
        pass

    def draw(self, window):
        """
        Handles Game GUI & Visuals
        
        :param self: Self
        :param window: Pygame Display
        """
        pass