import pygame
from ui_controls.clickables import *
from scenes.states import GameScenes

# Initialize button
pygame.font.init()
button = Clickable(254, 280, "Play Game", type_tag='button')
main_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\backgrounds\shop_shop_manager.png")

def handle_game_start(mouse_event):
    # I SHOULD HANDLE THIS IN CLICKABLE
    if mouse_event.type == pygame.MOUSEBUTTONDOWN and mouse_event.button == 1:
        if button.rect.collidepoint(mouse_event.pos):
            GameScenes.in_beginning, GameScenes.in_town = False, True
            return True  # Starts the game 
    return False

def render_initial_screen(display_surface, mouse_event, update_scene=None):
    
    button.update_state(mouse_event, update_scene)         
    
    # Draw everything on the screen
    display_surface.blit(main_background_image, (0, 0))
    button.draw_image(display_surface)
    
    