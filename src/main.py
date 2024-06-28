import pygame
import initial_menu
from gameplay import *
from music import *

# pygame setup
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True
start_music(mp3_files)
game_started = False

while running:
    # Handle events
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False # Exit the loop if the user closes the window        
   
    # Checks and update the current music
    check_current_music(mp3_files)
    
     # Updates button state and draw the initial menu
    if not game_started:
        game_started = initial_menu.handle_game_start(event)
        initial_menu.update_initial_screen(screen, event)
    else:
        # Starts the game
        main_game(screen, event)

    # Updates the display
    pygame.display.flip()

    # Limits FPS to 60
    clock.tick(60)  

pygame.quit()