from typing import Callable


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
