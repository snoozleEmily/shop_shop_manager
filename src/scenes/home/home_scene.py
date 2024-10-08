import pygame
from typing import Optional, Callable

from turns.day_turner import Days
from .counting_sheep import CountingSheep
from .sheep_sprite import sheep_sprites, jumping_sheep
from scenes.scene_manager import GameScenes
from utils.pygame_loads import load_image
from utils.declared_buttons import SLEEP, EXIT_SCENE
from backgrounds import HOME_DAYLIGHT_IMG, HOME_NIGHT_IMG

turn: Days = Days()

current_frame = 0
frame_counter = 0
animation_speed = 5


def render_home(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
    frame: int = 0,
):
    global current_frame, frame_counter

    # Minigame happens here...
    display_surface.blit(load_image(HOME_DAYLIGHT_IMG), (0, 0))

    # Sheep animation loop
    frame_counter += 1
    if frame_counter >= animation_speed:
        # Cycle through frames
        current_frame = (current_frame + 1) % len(sheep_sprites)
        frame_counter = 0

    sheep_position = (300, 200)
    display_surface.blit(sheep_sprites[current_frame], sheep_position)

    # Change background image to night
    SLEEP.draw_screen(display_surface)
    if SLEEP.update_scene(mouse_event, trigger_update):

        # After end of minigame, end the day
        GameScenes.in_town, GameScenes.in_home = True, False  # Go to town
        turn.handle_days(display_surface)  # End day

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_home = True, False


# The counting sheep minigame  will give the player energy


# The minigame should start after the sleep button was clicked
# And only after it is finished the day will end
# The minigame should return the amount of energy acquired during it
