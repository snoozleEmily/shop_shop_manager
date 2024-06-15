import pygame
import time

class Button:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.default_button_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\button_image.png")
        self.hover_button_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\button_image_hover.png")
        
        self.current_image = self.default_button_image
        self.rect = self.current_image.get_rect(topleft=(x, y))
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(text, True, (255, 255, 255))

        # Load the click sound effect
        self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\button_click.mp3")
        
        # Variables for click sound timing control
        self.last_click_time = time.time() - 0.5  # Allow immediate first click
        self.click_delay = 0.5  # Delay between consecutive clicks (in seconds)

    def is_hovered(self):
        mouse_position = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_position)

    def draw_button(self, screen):
        screen.blit(self.current_image, self.rect.topleft)
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect)

    def update_button_state(self, handle_event):
        if self.is_hovered(): # Check if the cursor is hovering the button
            self.current_image = self.hover_button_image # Switch to hover button image

            # Check if the user clicked the button
            if handle_event.type == pygame.MOUSEBUTTONDOWN and handle_event.button == 1:
                current_time = time.time() # Get the current time in seconds

                 # Check if enough time has passed since the last click to allow another click sound
                if current_time - self.last_click_time >= self.click_delay:
                    self.click_sound.play()  # Play click sound
                    self.last_click_time = current_time  # Update the last click time to the current time
        else:
            self.current_image = self.default_button_image
