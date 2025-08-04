import pygame

pygame.init()
window = pygame.display.set_mode((600,500))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    
    window.fill("red")
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()