import pygame

pygame.init()
pygame.mixer.init()
FONT_DEFAULT = pygame.font.Font(None, 28)
FONT_CURSIVE = pygame.font.Font(
    r"Python-studies\shop_shop_manager\assets\SKEETCH_.TTF", 36
)


def load_image(image_path: str) -> pygame.Surface:
    return pygame.image.load(image_path)


def load_sound(sound_path: str) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(sound_path)
