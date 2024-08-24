import pygame

from scenes.states import Dialogue
from utils.pygame_loads import FONT_DEFAULT
from utils.text_formatter import wrap_text
from .get_dialogue import get_dialogue


def display_dialogue(display_surface: pygame.Surface) -> pygame.Surface:
    # Define the container dimensions and colors
    CONTAINER_WIDTH, CONTAINER_HEIGHT = 557, 183
    CONTAINER_COLOR = (50, 50, 50, 128)  # Gray-ish with alpha for transparency

    # Define the position
    container_x, container_y = 230, 123
    text_x, text_y = container_x + 10, container_y + 10  # Padding inside the container

    # Define the text area width
    text_area_width = CONTAINER_WIDTH - 20

    # Get the text from the sales dialogue
    if not Dialogue.dialogue_displayed:
        dialogue = get_dialogue().get("speech", "")
        Dialogue.dialogue_text = wrap_text(dialogue, FONT_DEFAULT, text_area_width)
        Dialogue.displayed_count += 1
        Dialogue.dialogue_displayed = True

        # Draw the container
        container_surface = pygame.Surface(
            (CONTAINER_WIDTH, CONTAINER_HEIGHT), pygame.SRCALPHA
        )
        container_surface.fill(CONTAINER_COLOR)
        display_surface.blit(container_surface, (container_x, container_y))

        # Render the text within the text area, line by line
        for i, line in enumerate(Dialogue.dialogue_text):
            line_surface = FONT_DEFAULT.render(line, True, (0, 0, 0))
            display_surface.blit(
                line_surface, (text_x, text_y + i * FONT_DEFAULT.get_height())
            )

        # Debugging log to check what dialogue was fetched
        print(f"Dialogue Text: {dialogue}")

    # Display the text from the sales dialogue
    elif Dialogue.dialogue_text:
        # Draw the container again if text is already displayed
        container_surface = pygame.Surface(
            (CONTAINER_WIDTH, CONTAINER_HEIGHT), pygame.SRCALPHA
        )
        container_surface.fill(CONTAINER_COLOR)
        display_surface.blit(container_surface, (container_x, container_y))

        # Render the text within the text area, line by line
        for i, line in enumerate(Dialogue.dialogue_text):
            line_surface = FONT_DEFAULT.render(line, True, (0, 0, 0))
            display_surface.blit(
                line_surface, (text_x, text_y + i * FONT_DEFAULT.get_height())
            )
