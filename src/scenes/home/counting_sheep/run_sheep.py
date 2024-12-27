import pygame
import math

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
        self.jump_timer = 0
        self.jump_height = 100  # Maximum jump height in pixels
        self.initial_y = 200
        self.current_frame = 0
        self.frame_counter = 0
        self.ANIMATION_SPEED = 5
        
    def extended_width(self):
        """ If the width isn't muplipled by 2 the sheep appears only in half of the screen """
        return Global.SCREEN_WIDTH * 2  

    def reset_sheep_position(self):
        """Update the sheep's position and reset when it goes off-screen."""
        self.x += self.velocity
        if self.x < -sheep_sprite[0].get_width():
            self.x = self.extended_width()

    def animate_jump(self):
        """Calculate jump height using sine wave for smooth motion"""
        if self.is_jumping:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.jump_timer
            progress = min(elapsed_time / 1000.0, 1.0)  # 1000ms = 1 second duration
            
            # Sine wave creates smooth up/down motion
            jump_offset = math.sin(progress * math.pi) * self.jump_height
            self.y = self.initial_y - jump_offset
        else:
            self.y = self.initial_y

    def animate_sheep(self):
        """Animate the sheep by cycling through frames and handling jump"""
        self.animate_jump()  # Handle jump animation
        
        if not self.is_jumping:  # Only animate running when not jumping
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