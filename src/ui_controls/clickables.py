import pygame
import time

pygame.mixer.init()

class Clickable:
    def __init__(self, x, y, text, type_tag):
        """
        Initializes a clickable object with its position, type, and specific attributes

        Args:
        x and y (int): X and y coordinates positions on the screen
        text (str): Text displayed on the clickable object (e.g. 'button' type)
        identifier_type (str): Type of clickable object (e.g. 'button', 'exit_scene', 'settings')
        """
        self.x = x
        self.y = y
        self.text = text
        self.identifier_type = type_tag

        self.current_frame_index = 0
        self.last_frame_time = time.time()

        self.enabled, self.toggled, self.toggle_count = True, False, 0
        self.has_hover = False        
        
        if type_tag == 'button':
            self.has_hover = True
            self.default_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\button_image.png")
            self.hover_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\button_image_hover.png")
            
            self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\button_click.mp3")
            self.click_delay = 0.5
            
            self.font = pygame.font.Font(None, 36)
            self.text_surface = self.font.render(text, True, (255, 255, 255))            

        elif type_tag == 'exit_scene':
            self.has_hover = True
            self.default_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\exit_scene_default_image.png")
            self.hover_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\exit_scene_hover_image.png")
            
            self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\exit_scene_click.mp3")
            self.click_delay = 1          
            
        elif type_tag == 'box': 
            self.default_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\box.png")
            #self.hover_image = None // Should I add a hover effect for the box too?
           
            self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\box_click.mp3")
            self.click_delay = 0.8 

        elif type_tag == 'settings':
            self.has_hover = True
            self.default_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\settings_default.png")
            self.hover_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\clickables\settings_hover.png")

            self.click_sound = pygame.mixer.Sound(r"D:\Projects\Python-studies\shop_shop_manager\music\sound_effects\settings_click.mp3")
            self.click_delay = 1.5 

        self.current_image = self.default_image
        self.rect = self.current_image.get_rect(topleft=(x, y))
        
        self.last_click_time = time.time() - self.click_delay  # Allow immediate first click        

    def is_hovered(self):
        mouse_position = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_position) # bool: True if the mouse is hovering over

    def draw_image(self, screen):
        screen.blit(self.current_image, self.rect.topleft)
        if self.identifier_type == 'button':
            text_rect = self.text_surface.get_rect(center=self.rect.center)
            screen.blit(self.text_surface, text_rect)

    def update_state(self, handle_click_event, update_scene):  
            current_time = time.time()

            if self.is_hovered() and self.has_hover: self.current_image = self.hover_image
            else: self.current_image = self.default_image

            # Adds a delay to the sound effect
            if handle_click_event.type == pygame.MOUSEBUTTONDOWN and handle_click_event.button == 1:
                current_time = time.time()

                if self.enabled and self.rect.collidepoint(pygame.mouse.get_pos()):                
                    if current_time - self.last_click_time >= self.click_delay:
                        self.click_sound.play()
                        self.last_click_time = current_time

                        # Updates the scene by returning bool: True if the object was clicked:
                        return True
            return False