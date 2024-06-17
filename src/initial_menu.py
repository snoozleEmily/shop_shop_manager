import pygame
from ui_controls import Button

# Initialize button
pygame.font.init()
button = Button(254, 280, "Play Game")
main_background_image = pygame.image.load(r"D:\Projects\Python-studies\shop_shop_manager\images\shop_shop_manager.png")

def handle_button_click(mouse_event):    
    if mouse_event.type == pygame.MOUSEBUTTONDOWN and mouse_event.button == 1:
        if button.rect.collidepoint(mouse_event.pos):
            return True  # Starts the game 
    return False

def update_game_screen(display_surface, any_mouse_event):
    button.button_update_state(any_mouse_event)
    
    # Draw everything on the screen
    display_surface.blit(main_background_image, (0, 0))
    button.button_draw(display_surface)
