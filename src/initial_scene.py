import pygame
from typing import Optional, Callable

from scenes.scene_manager import GameScenes
from utils.pygame_loads import load_image
from utils.declared_buttons import START_GAME_BUTTON
from backgrounds import INITIAL_IMG


def handle_start(mouse_event: pygame.event.Event) -> bool:
    if mouse_event.type == pygame.MOUSEBUTTONDOWN and mouse_event.button == 1:
        if START_GAME_BUTTON.rect.collidepoint(mouse_event.pos):
            GameScenes.in_beginning, GameScenes.in_town = False, True
            return True  # Starts the game
    return False


def render_beginning(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
) -> None:

    START_GAME_BUTTON.update_scene(mouse_event, trigger_update)

    # Draw everything on the screen
    display_surface.blit(load_image(INITIAL_IMG), (0, 0))
    START_GAME_BUTTON.draw_screen(display_surface)
