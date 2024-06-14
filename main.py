import pygame
from ui_controls import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True

background_image = pygame.image.load(r"Python-studies\games\shop_shop_manager\images\background_image.png")
button = Button(250, 250, "Play Game")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update button state
    button.update()

    # Draw everything
    screen.blit(background_image, (0, 0))
    button.draw(screen)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()