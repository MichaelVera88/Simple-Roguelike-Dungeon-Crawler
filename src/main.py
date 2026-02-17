import pygame
from pathlib import Path
from logic import player
from scenes import main_menu, dungeon_overview, dungeon_loot_room, dungeon_combat_room

# Initialize & Set Game Window
pygame.init()
window = pygame.display.set_mode((600,500))
window_icon = pygame.image.load(Path(__file__).parent.parent / "Static" / "Images" / "window_icon_sword.png").convert_alpha()

pygame.display.set_icon(window_icon)
pygame.display.set_caption("Roguelike Dungeon Crawler")

# Initialize Player
character = player.Player()

# Game Scenes
scenes = {
    "main_menu": main_menu.MainMenu(),
    "dungeon_overview": dungeon_overview.DungeonOverview(),
    "dungeon_loot_room": dungeon_loot_room.DungeonLootRoom(),
    "dungeon_combat_room": dungeon_combat_room.DungeonCombatRoom(character)
}

current_scene = scenes["main_menu"]

# Run Game Window Loop
running = True
while running:

    ets = pygame.event.get()

    for event in ets:
        if event.type == pygame.QUIT:
            running = False

    # Show Current Scene
    current_scene.handle_events(ets)
    current_scene.handle_updates()
    current_scene.handle_draw(window)

    # Switch to Next Scene
    if current_scene.next_scene:
        if current_scene.next_scene == "dungeon_combat_room":
            current_scene = dungeon_combat_room.DungeonCombatRoom(character)
        else:
            current_scene = scenes[current_scene.next_scene]
        current_scene.next_scene = None

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()