import pygame
import os
import random

from pygame_loads import load_image


# Display a random character image
def display_customer(
    display_surface: pygame.Surface, _selected_image=[None]
) -> pygame.Surface:

    if _selected_image[0] is None:
        characters_folder = r"D:\\Projects\\Python-studies\\shop_shop_manager\\images\\characters\\human"
        character_images = [
            # List all images of characters in their folder
            f
            for f in os.listdir(characters_folder)
            if os.path.isfile(os.path.join(characters_folder, f))
        ]
        random_character_image = random.choice(character_images)
        _selected_image[0] = load_image(
            # Load the chosen character
            os.path.join(characters_folder, random_character_image)
        )

    return display_surface.blit(_selected_image[0], (-13, 137))
