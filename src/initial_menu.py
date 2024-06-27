import pygame
from ui_controls import *

# Initialize button
pygame.font.init()
button = Clickable(254, 280, "Play Game", identifier_type='button')
main_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\shop_shop_manager.png")

def handle_click(mouse_event):
    if mouse_event.type == pygame.MOUSEBUTTONDOWN and mouse_event.button == 1:
        if button.rect.collidepoint(mouse_event.pos):
            return True  # Starts the game 
    return False

def update_initial_screen(display_surface, any_mouse_event, update_scene=None):
    button.update_state(any_mouse_event, update_scene)
    
    # Draw everything on the screen
    display_surface.blit(main_background_image, (0, 0))
    button.draw_image(display_surface)
