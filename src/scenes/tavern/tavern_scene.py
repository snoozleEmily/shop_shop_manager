import pygame
from typing import Optional, Callable

from .dice import Dice
from scenes.states import GameScenes
from utils.container import render_container
from utils.pygame_loads import load_image
from backgrounds import TAVEN_BACKGROUND
from utils.declared_buttons import (
    ROLL_DICE,
    DICE_CUP,
    EXIT_SCENE,
)

die: Dice = Dice()
die_face = None


def render_tavern(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
) -> None:
    display_surface.blit(load_image(TAVEN_BACKGROUND), (0, 0))

    # Display the container when ROLL_DICE is clicked
    container_width, container_height = 688, 360  # Define your container dimensions
    render_container(display_surface, 55, 20, container_width, container_height)

    ROLL_DICE.draw_screen(display_surface)
    if ROLL_DICE.update_scene(mouse_event, trigger_update):
        global die_face
        dice_path = die.roll()
        die_face = load_image(dice_path)

    # Hide DICE_CUP button and only reveal it when ROLL_DICE is clicked
    DICE_CUP.draw_screen(display_surface)
    if DICE_CUP.update_scene(mouse_event, trigger_update):
        pass

    # Keep drawing the dice face after it has been rolled
    if die_face:
        display_surface.blit(die_face, (100, 50))

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_tavern = True, False
