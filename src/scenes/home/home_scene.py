import pygame
from typing import Optional, Callable

from .counting_sheep import CountingSheep
from scenes.scene_manager import GameScenes
from utils.pygame_loads import load_image
from utils.declared_buttons import SLEEP, EXIT_SCENE
from backgrounds import HOME_DAYLIGHT_IMG, HOME_NIGHT_IMG


def render_home(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
):
    if CountingSheep.grow_dark:
        # Night background is NOT being rendered
        display_surface.blit(load_image(HOME_NIGHT_IMG), (0, 0))
    else:
        display_surface.blit(load_image(HOME_DAYLIGHT_IMG), (0, 0))

    # Change background to night
    SLEEP.draw_screen(display_surface)
    if SLEEP.update_scene(mouse_event, trigger_update):
        CountingSheep.grow_dark == True

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_home = True, False


# Give n quantity of energy based on the housing level
# Player had to collect each turn (day) to get the energy
