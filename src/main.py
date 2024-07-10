import pygame
import initial_menu
from gameplay import *
from pyximport import install ; install() # Cython
from music import start_music, check_current_music, mp3_files

pygame.init()
pygame.mixer.init()
start_music(mp3_files)
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True
game_started = False

while running:
    # Handle events
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False # Close game        
   
    check_current_music(mp3_files)
    
    # Updates button state and draw the initial menu
    if not game_started:
        game_started = initial_menu.handle_game_start(event)
        initial_menu.render_initial_screen(screen, event)
    else:
        main_game(screen, event)

    # Updates the display
    pygame.display.flip()

    # Limits FPS to 60
    clock.tick(60)  

pygame.quit()

