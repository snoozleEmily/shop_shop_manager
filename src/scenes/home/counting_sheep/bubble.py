import pygame
import random


class Bubble:
    """Class to manage the bubble behavior."""

    container_width = 620
    container_height = 300

    def __init__(self):
        # Dynamically calculate the container's center based on the screen size
        self.container_x = 97
        self.container_y = 40

        # Random position within the centered container area
        self.x = random.randint(
            self.container_x, self.container_x + self.container_width
        )
        self.y = random.randint(
            self.container_y, self.container_y + self.container_height
        )
        self.visible = False  # Initially not visible

    def update_bubble(self):
        """Update the bubble's position and timer."""
        # Randomly update the bubble's position within the container area
        self.x = random.randint(
            self.container_x, self.container_x + self.container_width
        )
        self.y = random.randint(
            self.container_y, self.container_y + self.container_height
        )
        self.visible = True

    def draw_bubble(self, display_surface: pygame.Surface):
        """Draw the bubble if it is visible."""
        if self.visible:
            pygame.draw.circle(display_surface, (255, 255, 0), (self.x, self.y), 20)


"""     # To see the container uncomment this method for debugging purposes      
    def draw_container(self, display_surface: pygame.Surface):
        solid_color = (255, 0, 0)
        solid_surface = pygame.Surface((self.container_width, self.container_height))
        solid_surface.fill(solid_color)
        display_surface.blit(solid_surface, (self.container_x, self.container_y))
        
        # bubble.draw_container(display_surface) Call the method in render_sheep
"""