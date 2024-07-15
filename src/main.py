import pygame
from pyximport import install ; install() # Cython

from initial_menu import *
from gameplay import *
from scenes.states import *
from music import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Globals.SCREEN_HEIGHT, Globals.SCREEN_WIDTH))
clock = pygame.time.Clock()
running = True
game_started = False

start_music(mp3_files)

while running:
    # Handle events
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False # Close game        
   
    check_current_music(mp3_files)
    
    # Updates button state and draw the initial menu
    if not game_started:
        game_started = handle_game_start(event)
        render_initial_screen(screen, event)
    else:
        main_game(screen, event)

    # Updates the display
    pygame.display.flip()

    # Limits FPS to 60
    clock.tick(60)  

pygame.quit()

