import pygame


def render_container(
    display_surface: pygame.Surface,
    x: int,
    y: int,
    width: int,
    height: int,
    color_name: str,
) -> pygame.Surface:
    color_map = {
        "black-ish": (50, 50, 50, 128),
        "white-ish": (240, 240, 240, 128),
    }

    # Get the color from the dictionary, default to black-ish if not found
    color = color_map.get(color_name, (50, 50, 50, 128))

    # Add padding inside the container
    x, y = x + 10, y + 10

    # Draw the container
    container_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    container_surface.fill(color)
    display_surface.blit(container_surface, (x, y))


# Maybe could add a smooth transition for the container to appear on screen?
