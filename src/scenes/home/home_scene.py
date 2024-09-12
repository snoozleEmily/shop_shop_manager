import pygame
from typing import Optional, Callable

from .counting_sheep import CountingSheep
from scenes.scene_manager import GameScenes
from utils.container import render_container  # Do I need this?
from utils.pygame_loads import load_image
from utils.declared_buttons import SLEEP, EXIT_SCENE
from backgrounds import HOME_DAYLIGHT_IMG, HOME_NIGHT_IMG

turn: CountingSheep = CountingSheep()


def render_home(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
):

    # if CountingSheep.grow_dark:
    #    pass
    # display_surface.blit(load_image(HOME_NIGHT_IMG), (0, 0))
    # render_container(display_surface, 50, 0, 688, 380, "white-ish")

    # Minigame happens here...

    display_surface.blit(load_image(HOME_DAYLIGHT_IMG), (0, 0))

    # Change background image to night
    SLEEP.draw_screen(display_surface)
    if SLEEP.update_scene(mouse_event, trigger_update):
        # Need to implement the counting sheep minigame
        # to after, end the day

        # CountingSheep.grow_dark = True  # minigame begins

        # After end of minigame, end the day
        GameScenes.in_town, GameScenes.in_home = True, False  # Go to town
        turn.end_minigame(display_surface)  # End day

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_home = True, False


# The counting sheep minigame  will give the player energy
