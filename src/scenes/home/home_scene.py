import pygame
from typing import Optional, Callable

from scenes.states import GameScenes
from utils.pygame_loads import load_image
from utils.declared_buttons import EXIT_SCENE
from backgrounds import HOME_BACKGROUND


def render_home(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
):

    display_surface.blit(load_image(HOME_BACKGROUND), (0, 0))

    # Give n quantity of energy based on the housing level
    # Player had to collect each turn (day) to get the energy

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_home = True, False


# Menu for houses purchase
