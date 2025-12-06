import pygame
from pathlib import Path
from scenes import main_menu

# Initialize & Set Game Window
pygame.init()
window = pygame.display.set_mode((600,500))
window_icon = pygame.image.load(Path(__file__).parent.parent / "Static" / "Images" / "window_icon_sword.png").convert_alpha()

pygame.display.set_icon(window_icon)
pygame.display.set_caption("Roguelike Dungeon Crawler")

# Game Scenes
scenes = {
    "main_menu": main_menu
}

current_scene = main_menu.MainMenu()

# Run Game Window Loop
running = True
while running:

    ets = pygame.event.get()

    for event in ets:
        if event == pygame.QUIT:
            running = False

    # Create Current Scene
    current_scene.events(ets)
    current_scene.update()
    current_scene.draw(window)

    # Switch to Next Scene
    if current_scene.next_scene:
        current_scene = scenes[current_scene.next_scene]()

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()