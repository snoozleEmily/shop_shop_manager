from PIL import Image
import pygame
import time

pygame.mixer.init()

def handle_gif_frames(gif_path):
    """
    Loads frames from a GIF file and converts them to Pygame images.

    Args:
    gif_path (str): The file path to the GIF image.

    Returns:
    list: A list of Pygame images representing each frame of the GIF.
    """
    pil_image = Image.open(gif_path)
    frames = []
    try:
        while True:
            frame = pil_image.copy()
            frame = frame.convert('RGBA')
            frame_data = frame.tobytes()
            frame_image = pygame.image.fromstring(frame_data, frame.size, frame.mode)
            frames.append(frame_image)
            pil_image.seek(pil_image.tell() + 1)
    except EOFError:
        pass
    return frames

class Clickable:
    def __init__(self, x, y, text, identifier_type):
        """
        Initializes a clickable object with its position, type, and specific attributes

        Args:
        x and y (int): X and y coordinates positions on the screen
        text (str): Text displayed on the clickable object (e.g. 'button' type)
        identifier_type (str): Type of clickable object (e.g. 'button', 'exit_scene', 'settings')
        """
        self.x = x
        self.y = y
        self.item_or_text = text
        self.identifier_type = identifier_type
        self.enabled = True
        self.has_hover = False
        self.current_frame_index = 0
        self.last_frame_time = time.time()
        
        if identifier_type == 'button':
            self.has_hover = True
            self.default_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\button_image.png")
            self.hover_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\button_image_hover.png")
            
            self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\button_click.mp3")
            self.click_delay = 0.5
            
            self.font = pygame.font.Font(None, 36)
            self.text_surface = self.font.render(text, True, (255, 255, 255))            

        elif identifier_type == 'exit_scene':
            self.has_hover = True
            self.default_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\exit_scene_default_image.png")
            self.hover_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\exit_scene_hover_image.png")
            
            self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\exit_scene_click.mp3")
            self.click_delay = 1          
            
        elif identifier_type == 'box': 
            self.default_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\box.png")
            #self.hover_image = None // Should I add a hover effect for the box too?
           
            self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\box_click.mp3")
            self.click_delay = 0.8 

        elif identifier_type == 'settings': 
            self.has_hover = True
            self.default_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\settings_default.png")
            self.hover_images = handle_gif_frames(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\settings_hover.gif")
            self.hover_image = self.hover_images[self.current_frame_index]

            self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\settings_click.mp3")
            self.click_delay = 1.5 

        self.current_image = self.default_image
        self.rect = self.current_image.get_rect(topleft=(x, y))
        
        self.last_click_time = time.time() - self.click_delay  # Allow immediate first click
        
    def disable(self):
        self.enabled = False
        
    def enable(self):
        self.enabled = True

    def is_hovered(self):
        mouse_position = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_position) # bool: True if the mouse is hovering over the object

    def draw_image(self, screen):
        screen.blit(self.current_image, self.rect.topleft)
        if self.identifier_type == 'button':
            text_rect = self.text_surface.get_rect(center=self.rect.center)
            screen.blit(self.text_surface, text_rect)

    def update_state(self, handle_click_event, update_scene):
        if not self.enabled:
            return False
        
        current_time = time.time()
        if self.is_hovered() and self.has_hover:
            if hasattr(self, 'hover_images') and self.identifier_type == 'settings':
                # Update the hover frame if enough time has passed for GIF
                if current_time - self.last_frame_time >= 0.1:
                    self.current_frame_index = (self.current_frame_index + 1) % len(self.hover_images)
                    self.hover_image = self.hover_images[self.current_frame_index]
                    self.last_frame_time = current_time

            self.current_image = self.hover_image
        else:
            self.current_image = self.default_image

        if handle_click_event.type == pygame.MOUSEBUTTONDOWN and handle_click_event.button == 1:
            current_time = time.time()  # Get the current time in seconds
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                # Adds a delay to the sound effect
                if current_time - self.last_click_time >= self.click_delay:
                    self.click_sound.play()
                    self.last_click_time = current_time
                    # Updates the scene by returning bool: True if the object was clicked, False otherwise.
                    return True
        return False 