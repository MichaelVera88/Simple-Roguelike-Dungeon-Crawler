# Dungeon Combat Room
# Scene for when a player enters a combat room.

import pygame
import random
from scenes import base
from logic import enemy

class DungeonCombatRoom(base.BaseScene):

    def __init__(self, player):
        super().__init__()

        # Load Static Files
        enemy_skeleton = self.static_folder / "Images" / "UI" / "Enemies" / "skeleton.png"
        
        # Static Files to Pygame
        self.enemy = pygame.image.load(enemy_skeleton).convert_alpha()
        self.enemy_hitbox = self.enemy.get_rect(topleft=(200,300))

        # Load Player
        self.player = player
        self.turns = 1

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
            if self.turns > 0:
                damage = random.randint(1, 5)
                self.skeleton.health -= damage
                self.click_skeleton = False
                self.turns -= 1
                print(self.turns)
                if self.skeleton.health <= 0:
                    self.next_scene = "dungeon_overview"
            elif self.turns == 0:
                damage = random.randint(1, 3)
                self.player.health -= damage
                self.turns = 2
        
        if self.player.health <= 0:
            self.next_scene = "main_menu"

    def handle_draw(self, window):
        # Clear Window
        window.fill((0,0,0))
        font = pygame.font.Font(None, 18)

        if self.skeleton.health > 0:
            window.blit(self.enemy, self.enemy_hitbox)
            skeleton_health = font.render(f"{self.skeleton.health}", True, (0, 0, 0))
            window.blit(skeleton_health, self.enemy_hitbox)

        player_health = font.render(f"{self.player.health}", True, (255, 255, 255))
        window.blit(player_health, (0,0))