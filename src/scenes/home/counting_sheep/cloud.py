import pygame
import random
import math

from utils.pygame_loads import load_image

CLOUDS_PATH = r'Python-studies\\shop_shop_manager\\images\\characters\\sheep\\clouds'

class Cloud:
    """Class to manage the cloud behavior."""

    CONTAINER_WIDTH = 620
    CONTAINER_HEIGHT = 170
    CLOUD_NAMES = ['sheepish', 'sinister', 'sleepy', 'sus']
    CLOUD_IMAGES = [load_image(f"{CLOUDS_PATH}\\{cloud}.png") for cloud in CLOUD_NAMES]
        
    def __init__(self):
        # Dynamically calculate the container's center based on the screen size
        self.container_x = 97
        self.container_y = 11
        self.min_distance = 120  # For clouds to be far apart


        # Random position within the centered container area
        self.x = random.randint(
            self.container_x, self.container_x + self.CONTAINER_WIDTH
        )
        self.y = random.randint(
            self.container_y, self.container_y + self.CONTAINER_HEIGHT
        )
        self.last_x = self.x  # Store the initial position
        self.last_y = self.y  # Store the initial position
        self.current_cloud = random.choice(self.CLOUD_IMAGES)
        self.timer = random.randint(30, 60) # Cloud stays for 30-60 frames
        self.visible = False  # Initially not visible
        
    def _calculate_distance(self, x1, y1, x2, y2):
        """Ensure a large distance between last and current position (for clouds)."""
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def update_cloud(self):
        """Randomly update the cloud's position and timer within the container area."""
        if self.timer > 0:
            self.timer -= 1
        else:
            # Reset the timer and update the cloud
            new_x, new_y = self.x, self.y
            
            while True:
                # Generate new random position
                new_x = random.randint(self.container_x, self.container_x + self.CONTAINER_WIDTH)
                new_y = random.randint(self.container_y, self.container_y + self.CONTAINER_HEIGHT)
                
                # Calculate the distance between the new and old position
                distance = self._calculate_distance(self.last_x, self.last_y, new_x, new_y)
                
                # If the cloud is far from the previous position
                if distance >= self.min_distance:
                    break
                
            # Update position and reset the timer
            self.last_x = new_x
            self.last_y = new_y
            self.x = new_x
            self.y = new_y
            self.current_cloud = random.choice(self.CLOUD_IMAGES)
            self.timer = random.randint(60, 120)  # Reset the timer to a new value
            self.visible = True

    def draw_cloud(self, display_surface: pygame.Surface):
        """Draw the cloud if it is visible."""
        if self.visible and self.current_cloud:
            display_surface.blit(self.current_cloud, (self.x, self.y))

    def kill_cloud(self, mouse_event: pygame.event.Event) -> bool:
        """Check if the cloud is clicked and make it disappear."""
        if mouse_event.type == pygame.MOUSEBUTTONDOWN and mouse_event.button == 1:
            if self.visible and self.current_cloud:
                if self.x <= mouse_event.pos[0] <= self.x + self.current_cloud.get_width() and \
                   self.y <= mouse_event.pos[1] <= self.y + self.current_cloud.get_height():
                    self.visible = False
                    return True
        return False
    
    def sync_clouds(self, clouds):
        """Update multiple clouds with a delay and ensure minimum distance."""
        # Apply delay to cloud timers
        for i in range(1, len(clouds)):
            clouds[i].timer -= int(0.3 * 60)
        
        # Create a spatial partitioning grid
        cloud_positions = set()  # Store cloud positions as tuples (x, y)
        
        for cloud in clouds:
            while True:
                cloud.update_cloud()
                
                # Check if cloud position is valid
                current_position = (cloud.x, cloud.y)
                if all(
                    self._calculate_distance(x, y, cloud.x, cloud.y) 
                       >= self.min_distance 
                       for x, y in cloud_positions
                       ):
                    cloud_positions.add(current_position)
                    break

 
  
"""     # To see the container uncomment this method (for debugging purposes)     
    def draw_cloud_box(self, display_surface: pygame.Surface):
        solid_color = (255, 0, 0)
        solid_surface = pygame.Surface((self.CONTAINER_WIDTH, self.CONTAINER_HEIGHT))
        solid_surface.fill(solid_color)
        display_surface.blit(solid_surface, (self.container_x, self.container_y))
        
        # Call the method in render_sheep like this
        # bubble.draw_container(display_surface)   
"""
