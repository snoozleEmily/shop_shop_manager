import pygame
import time

pygame.mixer.init()

class Clickable:
    def __init__(self, x, y, item_or_text, is_text=False):
        self.x = x
        self.y = y
        self.item_or_text = item_or_text
        self.is_text = is_text
        
        if is_text:
            self.default_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\button_image.png")
            self.hover_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\button_image_hover.png")
            
            self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\button_click.mp3")
            self.click_delay = 0.5  # Delay between consecutive clicks (in seconds)
            
            self.font = pygame.font.Font(None, 36)
            self.text_surface = self.font.render(item_or_text, True, (255, 255, 255))
        else: 
            self.default_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\box.png")
            #self.hover_image = None // Should I add a hover effect for the box too?

            self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\box_click.mp3")
            self.click_delay = 0.8  # Delay between consecutive clicks (in seconds)

        self.current_image = self.default_image
        self.rect = self.current_image.get_rect(topleft=(x, y))
        
        self.last_click_time = time.time() - self.click_delay  # Allow immediate first click
        
    def is_hovered(self):
        mouse_position = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_position)

    def draw_image(self, screen):
        screen.blit(self.current_image, self.rect.topleft)
        if self.is_text:
            text_rect = self.text_surface.get_rect(center=self.rect.center)
            screen.blit(self.text_surface, text_rect)

    def update_state(self, handle_click_event):
        # Change default image for the image with hover effect
        if self.is_hovered() and self.is_text:            
            self.current_image = self.hover_image
        else:
            self.current_image = self.default_image
        
        if handle_click_event.type == pygame.MOUSEBUTTONDOWN and handle_click_event.button == 1:
            current_time = time.time()  # Get the current time in seconds
            if self.rect.collidepoint(pygame.mouse.get_pos()):                
                # print(pygame.mouse.get_pos()) [BUG] if is_text = False it returns multiple clicks

                # Adds a delay to the sound effect
                if current_time - self.last_click_time >= self.click_delay:                    
                    self.click_sound.play()
                    self.last_click_time = current_time

# Example usage:
# button = Clickable(100, 100, "Click Me", is_button=True)
# box = Clickable(200, 200, "item_name", is_button=False)
