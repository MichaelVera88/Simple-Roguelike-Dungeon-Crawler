# Dungeon Combat Room
# Scene for when a player enters a combat room.

import pygame
import random
from scenes import base
from logic import enemy

class DungeonCombatRoom(base.BaseScene):

    def __init__(self):
        super().__init__()

        #self.player = player

        # Load Static Files
        enemy_skeleton = self.static_folder / "Images" / "UI" / "Enemies" / "skeleton.png"
        
        # Static Files to Pygame
        self.enemy = pygame.image.load(enemy_skeleton).convert_alpha()
        self.enemy_hitbox = self.enemy.get_rect(topleft=(200,300))

        # Load Enemy Entities
        self.skeleton = enemy.Enemy()
        self.click_skeleton = False

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.enemy_hitbox.collidepoint(pygame.mouse.get_pos()):
                    self.click_skeleton = True

    def handle_updates(self):
        if self.click_skeleton:
            turns = 2
            if turns >= 0:
                damage = random.randint(1, 3)
                self.skeleton.health -= damage
                print(self.skeleton.health)
                self.click_skeleton = False
                turns -= 1
                if self.skeleton.health <= 0:
                    self.next_scene = "dungeon_overview"

    def handle_draw(self, window):
        # Clear Window
        window.fill((0,0,0))
        font = pygame.font.Font(None, 14)

        if self.skeleton.health > 0:
            window.blit(self.enemy, self.enemy_hitbox)
            skeleton_health = font.render(f"{self.skeleton.health}", True, (0, 0, 0))
            window.blit(skeleton_health, self.enemy_hitbox)