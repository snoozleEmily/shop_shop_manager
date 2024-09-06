import pygame

from .dialogue import Dialogue
from scenes.scene_manager import GameScenes
from utils.pygame_loads import FONT_DEFAULT
from utils.text_formatter import wrap_text
from utils.container import render_container
from .get_dialogue import get_dialogue


def display_dialogue(display_surface: pygame.Surface) -> pygame.Surface:
    # Container dimensions
    CONTAINER_WIDTH, CONTAINER_HEIGHT = 557, 183

    # Define the position
    container_x, container_y = 220, 115
    text_x, text_y = container_x + 20, container_y + 20  # Padding inside the container

    # Define the text area width
    text_width = CONTAINER_WIDTH - 20

    # Get the text from the sales dialogue
    if not Dialogue.dialogue_displayed:
        dialogue = get_dialogue().get("speech", "")
        Dialogue.dialogue_text = wrap_text(dialogue, FONT_DEFAULT, text_width)
        Dialogue.displayed_count += 1
        Dialogue.dialogue_displayed = True

        print(f"Dialogue Text: {dialogue}")

    # Draw the container
    render_container(
        display_surface,
        container_x,
        container_y,
        CONTAINER_WIDTH,
        CONTAINER_HEIGHT,
        "black-ish",
    )

    # Render the text within the text area, line by line
    for i, line in enumerate(Dialogue.dialogue_text):
        line_surface = FONT_DEFAULT.render(line, True, (0, 0, 0))
        display_surface.blit(
            line_surface, (text_x, text_y + i * FONT_DEFAULT.get_height())
        )
