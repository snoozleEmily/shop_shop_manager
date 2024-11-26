import pygame

from .sheep_sprite import sheep_sprite, jumping_sheep
from utils.pygame_loads import Global


class RunSheep:
    """Class to manage sheep animation and movement."""
    
    # Number of frames to wait before moving to the next animation frame
    ANIMATION_SPEED: int = 5 
    
    def __init__(self, x: int, y: int, velocity: int):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.current_frame = 0
        self.frame_counter = 0
        self.is_jumping = False
        
    def extended_width(self):
        """ If the width isn't muplipled by 2 the sheep appears only in half of the screen """
        return Global.SCREEN_WIDTH * 2  

    def reset_sheep_position(self):
        """Update the sheep's position and reset when it goes off-screen."""
        self.x += self.velocity
        if self.x < -sheep_sprite[0].get_width():
            self.x = self.extended_width()

    def animate_sheep(self):
        """Animate the sheep by cycling through frames."""
        if not self.is_jumping:  # Only animate when not jumping
            self.frame_counter += 1
            if self.frame_counter >= self.ANIMATION_SPEED:
                self.current_frame = (self.current_frame + 1) % len(sheep_sprite)
                self.frame_counter = 0

    def draw_sheep(self, display_surface: pygame.Surface):
        """Draw the sheep at its current position."""
        if self.is_jumping:
            display_surface.blit(jumping_sheep, (self.x, self.y))
        else:
            display_surface.blit(sheep_sprite[self.current_frame], (self.x, self.y))