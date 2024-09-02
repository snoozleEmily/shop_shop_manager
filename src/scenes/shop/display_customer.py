import pygame
import os
import random

from utils.pygame_loads import load_image


# Display a random character image
def display_customer(
    display_surface: pygame.Surface,
    _selected_character: list = [None],
    force_update: bool = False,
) -> pygame.Surface:
    """
    Display a random character image on the given surface.
    Args:
        display_surface (pygame.Surface): The surface to draw the character on.
        _selected_character (list): A list of one element, the character to display.
            If None, it will load a new character.
        force_update (bool): If True, force the loading of a new character.
    """
    previous_character = _selected_character[0]

    if _selected_character[0] is None or force_update:
        characters_folder = r"D:\\Projects\\Python-studies\\shop_shop_manager\\images\\characters\\human"
        character_images = os.listdir(characters_folder)
        random_character_image = random.choice(character_images)

        # I don't think this works
        # saw some characters being repeated?
        # not sure though

        character_not_allowed = random_character_image == previous_character
        while character_not_allowed:
            random_character_image = random.choice(character_images)

        _selected_character[0] = load_image(
            os.path.join(
                characters_folder,
                random_character_image,
            )
        )

    # I could maybe add a smooth transition from one character to another?
    return display_surface.blit(_selected_character[0], (-13, 137))
