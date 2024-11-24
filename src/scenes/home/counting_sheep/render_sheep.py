import pygame
import random
from typing import Optional, Callable

from scenes.scene_manager import GameScenes
from .sheep_sprite import sheep_sprite, jumping_sheep
from utils.pygame_loads import Global, load_image
from utils.declared_buttons import RETURN
from backgrounds import SHEEP_FIELD


# Constants
current_frame: int = 0  # Current frame index for the sheep animation
frame_counter: int = 0  # Counter to control the speed of the animation
SHEEP_AXIS_X: int = 800  # Starting X position (right edge of the screen)
SHEEP_AXIS_Y: int = 200  # Fixed Y position
SHEEP_VELOCITY: int = -5  # Speed at which the sheep moves left


class Sheep:
    """Class to manage sheep animation and movement."""
    ANIMATION_SPEED: int = 5  # Number of frames to wait before moving to the next animation frame
    
    def __init__(self, x: int, y: int, velocity: int):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.current_frame = 0
        self.frame_counter = 0
        self.is_jumping = False
        
    def extended_width(self):
        """ If the width isn't muplipled by 2 the sheep appear only in half of the screen """
        return Global.SCREEN_WIDTH * 2  

    def reset_position(self):
        """Update the sheep's position and reset when it goes off-screen."""
        self.x += self.velocity
        if self.x < -sheep_sprite[0].get_width():
            self.x = self.extended_width()

    def animate(self):
        """Animate the sheep by cycling through frames."""
        if not self.is_jumping:  # Only animate when not jumping
            self.frame_counter += 1
            if self.frame_counter >= self.ANIMATION_SPEED:
                self.current_frame = (self.current_frame + 1) % len(sheep_sprite)
                self.frame_counter = 0

    def draw(self, display_surface: pygame.Surface):
        """Draw the sheep at its current position."""
        if self.is_jumping:
            display_surface.blit(jumping_sheep, (self.x, self.y))
        else:
            display_surface.blit(sheep_sprite[self.current_frame], (self.x, self.y))


class Bubble:
    """Class to manage the bubble behavior."""

    container_width = 620
    container_height = 300

    def __init__(self):
        # Dynamically calculate the container's center based on the screen size
        self.container_x = 97
        self.container_y = 40

        # Random position within the centered container area
        self.x = random.randint(self.container_x, self.container_x + self.container_width)
        self.y = random.randint(self.container_y, self.container_y + self.container_height)
        self.visible = False  # Initially not visible

    def update(self):
        """Update the bubble's position and timer."""
        # Randomly update the bubble's position within the container area
        self.x = random.randint(self.container_x, self.container_x + self.container_width)
        self.y = random.randint(self.container_y, self.container_y + self.container_height)
        self.visible = True

    def draw(self, display_surface: pygame.Surface):
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

# Initialize the bubble
bubble = Bubble()

# Initialize the sheep
sheep = Sheep(SHEEP_AXIS_X, SHEEP_AXIS_Y, SHEEP_VELOCITY)


def render_sheep(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
):
    """
    Render the sheep game screen, including background, sheep animation, and buttons.
    """
    # Draw the sheep game background
    display_surface.blit(load_image(SHEEP_FIELD), (0, 0))

    # Check for spacebar press to make the sheep jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        sheep.is_jumping = True
    else:
        sheep.is_jumping = False

    # Update and draw sheep
    sheep.reset_position()
    sheep.animate()
    sheep.draw(display_surface)

    # Update and draw bubble
    # bubble.draw_container(display_surface)
    bubble.update()
    bubble.draw(display_surface)

    # Render the exit button
    RETURN.draw_screen(display_surface)
    if RETURN.update_scene(mouse_event, trigger_update):
        GameScenes.in_sheep_mg = False  # End the sheep game