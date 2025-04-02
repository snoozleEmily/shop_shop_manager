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

    def __init__(self, buttons_in_scene: dict = None) -> None:
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