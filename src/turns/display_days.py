import pygame

from .day_turner import Days
from utils.pygame_loads import FONT_BUTTON

turns: Days = Days()


def display_days(display_surface, day=turns.current_day):
    # handle_days(display_surface, day)

    day_string = f"Day: {day}"
    days_text = FONT_BUTTON.render(day_string, True, (255, 255, 255))
    border_surface = FONT_BUTTON.render(day_string, True, (0, 0, 0))

    # Get the size of the text
    text_rect = days_text.get_rect()

    # Placing the text on screen
    x, y = 720, 6

    # Draw a black border with larger offsets
    display_surface.blit(border_surface, (x - 2, y - 2))  # Top-left
    display_surface.blit(border_surface, (x + 2, y - 2))  # Top-right
    display_surface.blit(border_surface, (x - 2, y + 2))  # Bottom-left
    display_surface.blit(border_surface, (x + 2, y + 2))  # Bottom-right
    display_surface.blit(border_surface, (x - 2, y))  # Left
    display_surface.blit(border_surface, (x + 2, y))  # Right
    display_surface.blit(border_surface, (x, y - 2))  # Top
    display_surface.blit(border_surface, (x, y + 2))  # Bottom

    print(day)  # DEBUG

    # Draw the white text on top
    display_surface.blit(days_text, (x, y))
    pygame.display.flip()
