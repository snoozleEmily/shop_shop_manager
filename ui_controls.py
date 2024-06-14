import pygame
# Add a styling module with the default definitions for the font
class Button:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.default_button = pygame.image.load(r"Python-studies\games\shop_shop_manager\images\button_image.png")
        self.hover_button = pygame.image.load(r"Python-studies\games\shop_shop_manager\images\button_image_hover.png")
        
        self.current_image = self.default_button
        self.rect = self.current_image.get_rect(topleft=(x, y))
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(text, True, (255, 255, 255))

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def draw(self, screen):
        screen.blit(self.current_image, self.rect.topleft)
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect)

    def update(self):
        if self.is_hovered():
            self.current_image = self.hover_button
        else:
            self.current_image = self.default_button
