import pygame
from typing import Optional, Callable


from .dice import Dice
from scenes.scene_manager import GameScenes
from .render_minigame import render_minigame
from utils.container import render_container
from utils.pygame_loads import Screen, load_image
from backgrounds import TAVERN_IMG
from utils.declared_buttons import (
    ROLL_DICE,
    EXIT_SCENE,
)


def render_tavern(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
) -> None:
    display_surface.blit(load_image(TAVERN_IMG), (0, 0))

    # Display the container when ROLL_DICE is clicked
    container_width, container_height = 688, 360
    render_container(
        display_surface,
        47,
        20,
        container_width,
        container_height,
        "black-ish",
    )

    ROLL_DICE.draw_screen(display_surface)
    if ROLL_DICE.update_scene(mouse_event, trigger_update):
        Dice.minigame_active = True

    if Dice.minigame_active:
        render_minigame(display_surface, mouse_event, trigger_update)

    # Keep the dice face on screen after it has been rolled
    if Dice.dice_path:
        display_surface.blit(Dice.dice_path, (350, 200))  # Dice positioning

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_tavern = True, False
