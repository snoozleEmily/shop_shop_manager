import pygame


from utils.pygame_loads import Screen
from music import SongsPath, start_music, check_current_music
from initial_scene import handle_game_start, render_beginning
from gameplay import main_game

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(
    (
        Screen.SCREEN_HEIGHT,
        Screen.SCREEN_WIDTH,
    )
)

running = True
game_started = False

songs_path = SongsPath()
start_music(songs_path)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Close game

    # Start background music
    check_current_music(songs_path)

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
