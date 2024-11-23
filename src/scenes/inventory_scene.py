import pygame
from typing import Optional, Callable

from .scene_manager import GameScenes
from utils.pygame_loads import Global, load_image
from scenes.market_board import render_table, total_pages
from utils.declared_buttons import EXIT_SCENE, NEXT_BUTTON
from backgrounds import PAPER_IMG


def render_inventory(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
) -> None:
    display_surface.blit(load_image(PAPER_IMG), (0, 0))
    render_table(display_surface)

    NEXT_BUTTON.draw_screen(display_surface)
    if NEXT_BUTTON.update_scene(mouse_event, trigger_update):
        if Global.current_page < total_pages - 1:
            Global.current_page += 1
        else:
            Global.current_page = 0

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_inventory = True, False
