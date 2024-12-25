import pygame
import random

from utils.pygame_loads import load_image

CLOUDS_PATH = r'Python-studies\\shop_shop_manager\\images\\characters\\sheep\\clouds'

class Bubble:
    """Class to manage the cloud behavior."""

    CONTAINER_WIDTH = 620
    CONTAINER_HEIGHT = 300
    CLOUD_NAMES = ['sheepish', 'sinister', 'sleepy', 'sus']
    CLOUD_IMAGES = [load_image(f"{CLOUDS_PATH}\\{cloud}.png") for cloud in CLOUD_NAMES]
        
    def __init__(self):
        # Dynamically calculate the container's center based on the screen size
        self.container_x = 97
        self.container_y = 40

        # Random position within the centered container area
        self.x = random.randint(
            self.container_x, self.container_x + self.CONTAINER_WIDTH
        )
        self.y = random.randint(
            self.container_y, self.container_y + self.CONTAINER_HEIGHT
        )
        self.current_cloud = random.choice(self.CLOUD_IMAGES)
        self.visible = False  # Initially not visible
        
    def update_cloud(self):
        """Update the cloud's position and timer."""
        # Randomly update the cloud's position within the container area
        self.x = random.randint(
            self.container_x, self.container_x + self.CONTAINER_WIDTH
        )
        self.y = random.randint(
            self.container_y, self.container_y + self.CONTAINER_HEIGHT
        )
        self.current_cloud = random.choice(self.CLOUD_IMAGES)
        self.visible = True

    def draw_cloud(self, display_surface: pygame.Surface):# Replace this with the clouds images
        """Draw the cloud if it is visible."""
        if self.visible and self.current_cloud:
            display_surface.blit(self.current_cloud, (self.x, self.y))

"""     # To see the container uncomment this method for debugging purposes      
    def draw_container(self, display_surface: pygame.Surface):
        solid_color = (255, 0, 0)
        solid_surface = pygame.Surface((self.container_width, self.container_height))
        solid_surface.fill(solid_color)
        display_surface.blit(solid_surface, (self.container_x, self.container_y))
        
        # bubble.draw_container(display_surface) Call the method in render_sheep
"""