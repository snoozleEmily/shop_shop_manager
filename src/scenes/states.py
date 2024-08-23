class Globals:
    """
    Class to store game's global variables.
    Attributes:
        SCREEN_WIDTH (int): Width of the game's window.
        SCREEN_HEIGHT (int): Height of the game's window.
    """

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 800


class Dialogue:
    """
    Class to manage dialogues.
    Attributes:
        dialogue_text (Surface): The current dialogue being displayed.
        dialogue_displayed (bool): If the dialogue is currently being displayed.
        displayed_count (int): The number of times the dialogue was displayed.
    """

    dialogue_text = None
    dialogue_displayed = False
    displayed_count = 0


class GameScenes:
    """
    Class to manage the current game scene.
    """

    in_beginning = True
    in_town = False
    in_shop = False
    in_inventory = False
    in_home = False
    in_settings = False
