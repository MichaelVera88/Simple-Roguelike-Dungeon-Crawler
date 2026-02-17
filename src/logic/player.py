# Player
# Class for the player character

import random
from . import base_entity

class Player(base_entity.Entity):

    def __init__(self):
        super().__init__()

        self.health_potions = 3
    
    def attack(self):
        pass

    def use_health_potion(self):
        self.health += 5
        self.health_potions -= 1
        if self.health > 10:
            self.health = 10