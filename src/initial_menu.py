import pygame
from typing import Optional, Callable

from utils.pygame_loads import load_image
from utils.buttons import START_GAME_BUTTON
from scenes.states import GameScenes
from backgrounds import INITIAL_BACKGROUND

# Initialize button
pygame.font.init()


def handle_game_start(mouse_event: pygame.event.Event) -> bool:
    if mouse_event.type == pygame.MOUSEBUTTONDOWN and mouse_event.button == 1:
        if START_GAME_BUTTON.rect.collidepoint(mouse_event.pos):
            GameScenes.in_beginning, GameScenes.in_town = False, True
            return True  # Starts the game
    return False


def render_initial_screen(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    update_scene: Optional[Callable] = None,
) -> None:

    START_GAME_BUTTON.update_state(mouse_event, update_scene)

    # Draw everything on the screen
    display_surface.blit(load_image(INITIAL_BACKGROUND), (0, 0))
    START_GAME_BUTTON.draw_screen(display_surface)
