import pygame


from gameplay import main_game
from utils.pygame_loads import Global
from music import SongsPath
from initial_scene import handle_start, render_beginning


pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(
    (
        Global.SCREEN_HEIGHT,
        Global.SCREEN_WIDTH,
    )
)

running: bool = True
game_started: bool = False

songs_path: SongsPath = SongsPath()
SongsPath.start_music(songs_path)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Close game

    # Start background music
    SongsPath.check_current_music(songs_path)

    # Updates button state and draw the initial menu
    if not game_started:
        game_started = handle_start(event)
        render_beginning(SCREEN, event)
    else:
        main_game(SCREEN, event)

    pygame.display.flip()
    # clock.tick(30) -> the stupidity of a silly dev, I built a WHOLE system to avoid flickering
    # thinking it was a complex bug when IN FACT it was one simple line of code that  shouldn't be there

pygame.quit()
