import time


class GameScenes:
    """
    Class to manage the current game scene.
    """

    # Flags for each scene that handle which scene is active
    in_beginning: bool = True  # Refers to the initial_scene
    in_town: bool = False
    in_shop: bool = False
    in_home: bool = False
    in_sheep_mg: bool = False
    in_tavern: bool = False
    in_sky: bool = False
    in_inventory: bool = False    
    in_settings: bool = False
    # ADD NEW SCENE HERE

    def __init__(self, buttons_in_scene: dict = None, default_hover: callable = None) -> None:
        """
        Args:
            # buttons_in_scene (dict):
            A dictionary where the keys are the names of the scenes and the values are lists of button objects.

            # default_hover (function):
            A function that will be called to check if a button is hovered,
            if not provided it will default to the hover_check method of this class.
        """
        if buttons_in_scene is None:
            buttons_in_scene = {}
        self.buttons_in_scene = buttons_in_scene

        self.default_hover = (
            default_hover if default_hover is not None else self.hover_check
        )

        # Tracks the last hover time to prevent rapid re-triggering
        self.last_hover_time = None

        # Flags if the mouse was hovering over the button in the last frame
        self.hovered_last_frame = False

    def scene_check(self) -> list:
        """
        Get buttons for the active scene based on current flags.
        """
        scene_flags = {
            "in_shop": "shop",
            "in_home": "home",
            "in_sheep_mg": "sheep",
            "in_tavern": "tavern",
            "in_inventory": "inventory",
            "in_settings": "settings",
            # ADD NEW SCENE HERE
        }

        for flag, scene_name in scene_flags.items():
            if getattr(self, flag):
                return self.buttons_in_scene.get(scene_name, [])

        return []

    def hover_check(self) -> bool:
        """
        Checks if any button in the current active scene is hovered.
        The function also implements a delay period of 0.2 seconds between
        hover events.

        Returns:
            bool: True if any button that HAS the hover effect is hovered, False otherwise.
        """
        delay = 0.2
        buttons = self.scene_check()
        any_hovered = any(button.is_hovered() for button in buttons)

        if any_hovered:
            # If any button is hovered, store the current time
            self.last_hover_time = time.perf_counter() 
            self.hovered_last_frame = True
            return True
        else:
            # If no hover event has occurred yet, return False immediately
            if self.last_hover_time is None:
                return False

            # Calculate the elapsed time since the last recorded hover event
            elapsed_time = time.perf_counter() - self.last_hover_time

            # This method returns True in two cases:
            # 1. If a button is actively hovered (hover flag is active).
            # 2. If a button was recently hovered and the elapsed time is still within the delay period.
            # If the delay period has passed, the hover flag is reset and the method returns False.
            return self.hovered_last_frame and elapsed_time < delay


