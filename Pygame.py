import pygame

pygame.init()

window_size = (800, 800)
window = pygame.display.set_mode(window_size)

pygame.display.set_caption("My Game")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((255, 255, 255))
    pygame.display.flip()


