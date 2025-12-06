import pygame
from pathlib import Path

# Initialize & Set Game Window
pygame.init()
window = pygame.display.set_mode((600,500))

window_icon = pygame.image.load(Path(__file__).parent.parent / "Static" / "Images" / "window_icon_sword.png").convert_alpha()
game_title = pygame.image.load(Path(__file__).parent.parent / "Static" / "Images" / "game_title.png").convert_alpha()

# Play Button Images (Modulate & make this scalable)
play_button = pygame.image.load(Path(__file__).parent.parent / "Static" / "Images" / "UI" / "play_button.png").convert_alpha()
play_button_hover = pygame.image.load(Path(__file__).parent.parent / "Static" / "Images" / "UI" / "play_button_hover.png").convert_alpha()
play_button_hitbox = play_button.get_rect(topleft=(200,300))

pygame.display.set_icon(window_icon)
pygame.display.set_caption("Roguelike Dungeon Crawler")

# Run Game Window Loop
running = True
while running:

    mouse_pos = pygame.mouse.get_pos()

    # Create objects for different types of screens
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if play_button_hitbox.collidepoint(mouse_pos):
            window.blit(play_button_hover, play_button_hitbox)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Clicked Play")
        else:
            window.blit(play_button, play_button_hitbox)

    window.blit(game_title, (100,50))
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()