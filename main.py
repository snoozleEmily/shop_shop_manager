import pygame
from game_core import gameplay
from ui_controls import *
from music import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True

paper_background_image = pygame.image.load(r"D:/Projects/Python-studies/shop_shop_manager/images/background_image.png")
button = Button(250, 250, "Play Game")

# Starts playing background music
start_music(mp3_files)

game_started = False

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Exit the loop if the user closes the window
        
        # If the button is clicked, the game starts
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button.rect.collidepoint(event.pos):
                game_started = True

    # Updates button state
    button.update_button_state(event)

    # Checks and update the current music
    check_current_music(mp3_files)  

    # Draw everything on the screen
    screen.blit(paper_background_image, (0, 0))
    button.draw_button(screen)

    # Starts the game
    if game_started:
        gameplay(screen)

    # Updates the display
    pygame.display.flip()

    # Limits FPS to 60
    clock.tick(60)  

pygame.quit()