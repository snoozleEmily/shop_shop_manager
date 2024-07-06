import pygame
import settings
import scenes
from ui_controls import *

# Initialize button
pygame.font.init()
button = Clickable(254, 280, "Play Game", identifier_type='button')
settings_button = Clickable(758, 10, text = None, identifier_type='settings')
main_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\shop_shop_manager.png")

def handle_game_start(mouse_event):
    # I SHOULD HANDLE THIS IN CLICKABLE
    if mouse_event.type == pygame.MOUSEBUTTONDOWN and mouse_event.button == 1:
        if button.rect.collidepoint(mouse_event.pos):
            scenes.in_town = True
            return True  # Starts the game 
    return False

def render_initial_screen(display_surface, mouse_event, update_scene=settings.render_settings_screen):
    if settings_button.update_state(mouse_event, update_scene):
        scenes.in_settings, scenes.in_town = True, False

    elif scenes.in_settings:
        update_scene(display_surface)
        button.enabler()
        
    else:
        button.update_state(mouse_event, update_scene)
        settings_button.update_state(mouse_event, update_scene=None)  
        
        # Draw everything on the screen
        display_surface.blit(main_background_image, (0, 0))
        button.draw_image(display_surface)
        settings_button.draw_image(display_surface)
    
    