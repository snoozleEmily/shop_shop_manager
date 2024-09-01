from typing import Callable

from .scene_manager import GameScenes
from utils.buttons import EXIT_SCENE, ABOUT_INFO, NEXT_BUTTON

# Which buttons trigger the rerendering of the scene if hovered
shop: GameScenes = GameScenes(
    buttons_in_scene={
        "shop": [
            EXIT_SCENE,
            NEXT_BUTTON,
        ]
    }
)
inventory: GameScenes = GameScenes(
    buttons_in_scene={
        "inventory": [
            EXIT_SCENE,
        ]
    }
)
home: GameScenes = GameScenes(
    buttons_in_scene={
        "home": [
            EXIT_SCENE,
        ]
    }
)
tavern: GameScenes = GameScenes(
    buttons_in_scene={
        "tavern": [
            EXIT_SCENE,
        ]
    }
)
settings: GameScenes = GameScenes(
    buttons_in_scene={
        "settings": [
            EXIT_SCENE,
            ABOUT_INFO,
        ]
    }
)


class Screen:
    """
    Class to store game's global variables.
    Attributes:
        SCREEN_WIDTH (int): Width of the game's window.
        SCREEN_HEIGHT (int): Height of the game's window.
    """

    SCREEN_WIDTH: int = 400
    SCREEN_HEIGHT: int = 800


class Dialogue:
    """
    Class to manage dialogues.
    Attributes:
        dialogue_text (Surface): The current dialogue being displayed.
        dialogue_displayed (bool): If the dialogue is currently being displayed.
        displayed_count (int): The number of times the dialogue was displayed.
    """

    dialogue_text: Callable = None
    dialogue_displayed: bool = False
    displayed_count: int = 0
