import pygame
from typing import Optional, Callable

from turns.day_turner import Days
from .counting_sheep.render_sheep import render_sheep
from scenes.scene_manager import GameScenes
from utils.pygame_loads import load_image
from utils.declared_buttons import SLEEP, WAKE_UP, EXIT_SCENE
from backgrounds import HOME_DAYLIGHT_IMG, HOME_NIGHT_IMG


turn: Days = Days()

def render_home(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None
):
    if GameScenes.in_sheep_mg:
        # Render counting sheep game
        render_sheep(display_surface, mouse_event, trigger_update)
        return
    
    display_surface.blit(load_image(HOME_DAYLIGHT_IMG), (0, 0))

    # Change background image to night
    SLEEP.draw_screen(display_surface)
    if SLEEP.update_scene(mouse_event, trigger_update):
        # Go to counting sheep minigame
        GameScenes.in_sheep_mg, GameScenes.in_home = True, False
    
    # Change background image to day
    WAKE_UP.draw_screen(display_surface)
    if WAKE_UP.update_scene(mouse_event, trigger_update):
        # After end of minigame, end the day
        # GameScenes.in_town, GameScenes.in_home = True, False  # Go to town
        turn.handle_days(display_surface)  # End day

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_home = True, False


# The counting sheep minigame  will give the player energy


# The minigame should start after the sleep button was clicked
# And only after it is finished the day will end
# The minigame should return the amount of energy acquired during it
