# Enemy
# Class for enemies

from . import base_entity

class Enemy(base_entity.Entity):

    def __init__(self):
        super().__init__()
    
    def attack(self):
        pass