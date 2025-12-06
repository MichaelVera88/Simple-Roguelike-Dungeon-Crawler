# Main Menu Scene
# First thing player sees when game is launched.

import pygame
from scenes import base

class MainMenu(base.BaseScene):

    def __init__(self):
        super().__init__()

        # Load Static Files
        game_title = self.static_folder / "Images" / "game_title.png"
        play_button = self.static_folder / "Images" / "UI" / "play_button.png"
        play_button_hover = self.static_folder / "Images" / "UI" / "play_button_hover.png"

        # Static Files to Pygame
        self.game_title = pygame.image.load(game_title).convert_alpha()
        self.play_button = pygame.image.load(play_button).convert_alpha()
        self.play_button_hover = pygame.image.load(play_button_hover).convert_alpha()
        self.play_button_hitbox = self.play_button.get_rect(topleft=(200,300))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button_hitbox.collidepoint(pygame.mouse.get_pos()):
                    self.next_scene = "dungeon_overview"
    
    def handle_updates(self):
        pass

    def handle_draw(self, window):
        # Clear Window
        window.fill((0,0,0))

        # Draw Game Title
        window.blit(self.game_title, (100,50))

        # Draw Play Button
        if self.play_button_hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.play_button_hover, self.play_button_hitbox)
        else:
            window.blit(self.play_button, self.play_button_hitbox)
    