import pygame
from typing import Optional, Callable

from scenes.states import GameScenes
from utils.pygame_loads import load_image
from utils.declared_buttons import EXIT_SCENE
from scenes.market_board import render_table
from backgrounds import PAPER_BACKGROUND


def render_inventory(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
) -> None:

    display_surface.blit(load_image(PAPER_BACKGROUND), (0, 0))
    render_table(display_surface)

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_inventory = True, False
