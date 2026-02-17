# Dungeon Boss Room
# Scene for when a player enters the final room of dungeon

import pygame
import random
from scenes import base
from logic import enemy

class DungeonBossRoom(base.BaseScene):

    def __init__(self, player):
        super().__init__()

        # Load Static Files
        skull_boss = self.static_folder / "Images" / "UI" / "Enemies" / "boss.png"
        health_potion = self.static_folder / "Images" / "UI" / "Items" / "health_potion.png"

        # Static Files to Pygame
        self.skull_boss = pygame.image.load(skull_boss).convert_alpha()
        self.skull_boss_hitbox = self.skull_boss.get_rect(topleft=(200,100))

        self.health_potion_button = pygame.image.load(health_potion).convert_alpha()
        self.health_potion_button_hitbox = self.health_potion_button.get_rect(topleft=(100,400))

        # Load Player
        self.player = player
        self.turns = 1
        self.click_health_potion_button = False

        # Load Enemy Entities
        self.boss = enemy.Enemy()
        self.boss.health = 50
        self.click_boss = False

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.skull_boss_hitbox.collidepoint(pygame.mouse.get_pos()):
                    self.click_boss = True
                if self.health_potion_button_hitbox.collidepoint(pygame.mouse.get_pos()):
                    self.click_health_potion_button = True

    def handle_updates(self):
        if self.click_boss:
            if self.turns > 0:
                damage = random.randint(1, 5)
                self.boss.health -= damage
                self.click_boss = False
                self.turns -= 1
                if self.boss.health <= 0:
                    self.next_scene = "win_screen"
            elif self.turns == 0:
                damage = random.randint(1, 3)
                self.player.health -= damage
                self.turns = 2
        
        if self.click_health_potion_button:
            if self.player.health_potions > 0:
                self.player.use_health_potion()
            self.click_health_potion_button = False

        if self.player.health <= 0:
            self.next_scene = "death_screen"

    def handle_draw(self, window):
        # Clear Window
        window.fill((0,0,0))
        font = pygame.font.Font(None, 18)

        if self.boss.health > 0:
            window.blit(self.skull_boss, self.skull_boss_hitbox)
            boss_health = font.render(f"{self.boss.health}", True, (0, 0, 0))
            window.blit(boss_health, (200,110))

        player_health = font.render(f"{self.player.health}", True, (255, 255, 255))
        window.blit(player_health, (0,0))

        window.blit(self.health_potion_button, self.health_potion_button_hitbox)

        health_potion_count = font.render(f"{self.player.health_potions}", True, (0, 0, 0))
        window.blit(health_potion_count, self.health_potion_button_hitbox)