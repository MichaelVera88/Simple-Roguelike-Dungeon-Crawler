import pygame

# Initialize & Set Game Window
pygame.init()
window = pygame.display.set_mode((600,500))

window_icon = pygame.image.load("Static/Images/window_icon_sword.png").convert_alpha()

pygame.display.set_icon(window_icon)
pygame.display.set_caption("Roguelike Dungeon Crawler")

# Run Game Window Loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill("red")
    window.blit(window_icon, (0,0))
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()