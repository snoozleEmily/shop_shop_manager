import pygame

from utils.pygame_loads import FONT_BUTTON


def display_days(display_surface):
    days_text = FONT_BUTTON.render("Day: 1", True, (255, 255, 255))
    border_surface = FONT_BUTTON.render("Day: 1", True, (0, 0, 0))

    # Get the size of the text
    text_rect = days_text.get_rect()

    # Placing the text on screen
    x, y = 727, 4

    # Draw the black border with larger offsets
    display_surface.blit(border_surface, (x - 2, y - 2))  # Top-left
    display_surface.blit(border_surface, (x + 2, y - 2))  # Top-right
    display_surface.blit(border_surface, (x - 2, y + 2))  # Bottom-left
    display_surface.blit(border_surface, (x + 2, y + 2))  # Bottom-right
    display_surface.blit(border_surface, (x - 2, y))  # Left
    display_surface.blit(border_surface, (x + 2, y))  # Right
    display_surface.blit(border_surface, (x, y - 2))  # Top
    display_surface.blit(border_surface, (x, y + 2))  # Bottom

    # Draw the white text on top
    display_surface.blit(days_text, (x, y))
    pygame.display.flip()
