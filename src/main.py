import pygame
from pyximport import install

install()  # Cython

import music
from scenes.states import Screen
from initial_scene import handle_game_start, render_beginning
from gameplay import main_game

pygame.init()
pygame.mixer.init()
SCREEN = pygame.display.set_mode((Screen.SCREEN_HEIGHT, Screen.SCREEN_WIDTH))
clock = pygame.time.Clock()
running = True
game_started = False

music.start_music(music.mp3_files)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Close game

    # Start background music
    music.check_current_music(music.mp3_files)

    # Updates button state and draw the initial menu
    if not game_started:
        game_started = handle_game_start(event)
        render_beginning(SCREEN, event)
    else:
        main_game(SCREEN, event)

    # Updates the display
    pygame.display.flip()

    # Limits FPS to 60
    clock.tick(60)

pygame.quit()
