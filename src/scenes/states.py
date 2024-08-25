from typing import Callable


class Globals:
    """
    Class to store game's global variables.
    Attributes:
        SCREEN_WIDTH (int): Width of the game's window.
        SCREEN_HEIGHT (int): Height of the game's window.
    """

    SCREEN_WIDTH: int = 400
    SCREEN_HEIGHT: int = 800


class GameScenes:
    """
    Class to manage the current game scene.
    """

    in_beginning: bool = True
    in_town: bool = False
    in_shop: bool = False
    in_inventory: bool = False
    in_home: bool = False
    in_settings: bool = False


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
