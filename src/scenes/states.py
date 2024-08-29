from typing import Callable

from utils.clickables import Clickable
from utils.buttons import EXIT_SCENE, ABOUT_INFO, NEXT_BUTTON


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

    def __init__(self, buttons_in_scene=None, default_hover=None):
        if buttons_in_scene is None:
            buttons_in_scene = {}
        self.buttons_in_scene = buttons_in_scene
        self.default_hover = (
            default_hover if default_hover is not None else self.hover_check
        )

    def hover_check(self) -> bool:
        """
        Checks if any button in the current active scene is hovered.

        Returns:
            bool: True if any button is hovered, False otherwise.
        """
        buttons = self.scene_check()
        any_hovered = any(button.is_hovered() for button in buttons)

        return any_hovered

    def scene_check(self):
        """
        Get buttons for the active scene based on current flags.

        Returns:
            list: List of buttons in the active scene.
        """
        scene_flags = {
            "in_shop": "shop",
            "in_home": "home",
            "in_inventory": "inventory",
            "in_settings": "settings",
        }

        for flag, scene_name in scene_flags.items():
            if getattr(self, flag):
                return self.buttons_in_scene.get(scene_name, [])

        return []


shop: GameScenes = GameScenes(buttons_in_scene={"shop": [EXIT_SCENE, NEXT_BUTTON]})
inventory: GameScenes = GameScenes(buttons_in_scene={"inventory": [EXIT_SCENE]})
home: GameScenes = GameScenes(buttons_in_scene={"home": [EXIT_SCENE]})
settings: GameScenes = GameScenes(
    buttons_in_scene={"settings": [EXIT_SCENE, ABOUT_INFO]}
)
