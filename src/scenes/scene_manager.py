import time


class GameScenes:
    """
    Class to manage the current game scene.
    """

    # Flags for each scene that handle which scene is active
    in_beginning: bool = True  # Refers to the initial_scene
    in_town: bool = False
    in_shop: bool = False
    in_inventory: bool = False
    in_tavern: bool = False
    in_home: bool = False
    in_settings: bool = False

    def __init__(self, buttons_in_scene=None, default_hover=None) -> None:
        """
        Args:
            buttons_in_scene (dict): A dictionary where the keys are the names of the scenes and the values are lists of button objects.
            default_hover (function): A function that will be called to check if a button is hovered, if not provided it will default to the hover_check method of this class.
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
            "in_inventory": "inventory",
            "in_settings": "settings",
        }

        for flag, scene_name in scene_flags.items():
            if getattr(self, flag):
                return self.buttons_in_scene.get(scene_name, [])

        return []

    def hover_check(self) -> bool:
        """
        Checks if any button in the current active scene is hovered.
        The function also implements a delay period of 0.5 seconds between
        hover events.

        Returns:
            bool: True if any button that HAS the hover effect is hovered, False otherwise.
        """
        buttons = self.scene_check()
        any_hovered = any(button.is_hovered() for button in buttons)

        if any_hovered:
            # If any button is hovered, store the current time
            self.last_hover_time = time.time()
            self.hovered_last_frame = True
            return True
        else:
            # If no button is hovered, check if the delay has passed
            if self.hovered_last_frame and self.last_hover_time is not None:
                elapsed_time = time.time() - self.last_hover_time
                if elapsed_time >= 0.2:
                    # Reset the flag and return False if the delay has passed
                    self.hovered_last_frame = False
                    return False
                # Return True if still within the delay period
                return True
            # Return False if no button is hovered and delay has passed
            return False
