import pygame
import numpy as np


pygame.init()
pygame.mixer.init()


class Screen:
    """
    Class to store on screen-related global variables.

    Attributes:
        SCREEN_WIDTH (int): Width of the game's window.
        SCREEN_HEIGHT (int): Height of the game's window.
    """

    SCREEN_WIDTH: int = 400
    SCREEN_HEIGHT: int = 800

    # Table Of The Inventory Scene
    paginated_data = []
    current_page = 0


# Items Game Data
with open(
    r"Python-studies\shop_shop_manager\assets\data\items\all_items.csv", "r"
) as file:
    all_items = np.genfromtxt(file, delimiter=",", dtype=str)


# Fonts
FONT_DEFAULT = pygame.font.Font(
    r"Python-studies\shop_shop_manager\assets\fonts\baby_doll.ttf", 28  # Baby Doll
)
FONT_CURSIVE = pygame.font.Font(
    r"Python-studies\shop_shop_manager\assets\fonts\skeetch.ttf", 36  # Skeetch
)
FONT_BUTTON = pygame.font.SysFont("Roboto", 36)  # Roboto


# Images
def load_image(image_path: str) -> pygame.Surface:
    return pygame.image.load(image_path)


# Sound effects
def load_sound(sound_path: str) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(sound_path)
