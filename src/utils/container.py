import pygame


def render_container(
    display_surface: pygame.Surface, x: int, y: int, width: int, height: int
) -> pygame.Surface:
    # Container dimensions and colors
    CONTAINER_COLOR = (50, 50, 50, 128)  # Gray-ish with alpha for transparency

    # Add padding inside the container
    x, y = x + 10, y + 10

    # Draw the container
    container_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    container_surface.fill(CONTAINER_COLOR)
    display_surface.blit(container_surface, (x, y))
