import pygame
import os
import random
from typing import Optional, Callable

from ui_controls.clickables import Clickable
from scenes.states import GameScenes
from pygame_loads import load_image
from backgrounds import SHOP_BACKGROUND

EXIT_SCENE = Clickable(740, 330, text=None, type_tag="exit_scene")


def render_shop(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    update_scene: Optional[Callable] = None,
    _selected_image=[None],
) -> None:

    display_surface.blit(load_image(SHOP_BACKGROUND), (0, 0))
    EXIT_SCENE.draw_screen(display_surface)

    # Display a random character image
    if _selected_image[0] is None:
        characters_folder = r"D:\\Projects\\Python-studies\\shop_shop_manager\\images\\characters\\human"
        character_images = [
            # List all images of characters in their folder
            f
            for f in os.listdir(characters_folder)
            if os.path.isfile(os.path.join(characters_folder, f))
        ]
        random_character_image = random.choice(character_images)
        _selected_image[0] = pygame.image.load(
            # Load the chosen character
            os.path.join(characters_folder, random_character_image)
        )

    display_surface.blit(_selected_image[0], (-13, 137))
    # Goes back to town if exit button is clicked
    if EXIT_SCENE.update_state(mouse_event, update_scene):
        GameScenes.in_town, GameScenes.in_shop = True, False

    pygame.display.flip()
