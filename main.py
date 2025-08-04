import pygame

pygame.init()
window = pygame.display.set_mode((600,500))
running = True

window_icon = pygame.image.load("Static/Images/window_icon_sword.png").convert_alpha()

pygame.display.set_icon(window_icon)
pygame.display.set_caption("Roguelike Dungeon Crawler")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill("red")
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()