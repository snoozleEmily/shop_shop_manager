import pygame

from scenes.states import Dialogue
from pygame_loads import FONT_DEFAULT
from .get_dialogue import get_dialogue


def display_dialogue(display_surface: pygame.Surface) -> pygame.Surface:
    # Get and display the dialogue
    if not Dialogue.dialogue_displayed:
        dialogue = get_dialogue().get("speech", "")
        Dialogue.dialogue_text = FONT_DEFAULT.render(dialogue, True, (0, 0, 0))
        Dialogue.displayed_count += 1

        print(f"Dialogue Text: {dialogue}")  # Debugging log
        display_surface.blit(Dialogue.dialogue_text, (100, 137))
        Dialogue.dialogue_displayed = True
    elif Dialogue.dialogue_text:
        display_surface.blit(Dialogue.dialogue_text, (100, 137))
