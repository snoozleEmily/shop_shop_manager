import pygame
import numpy as np

pygame.init()
pygame.mixer.init()

FONT_DEFAULT = pygame.font.Font(
    r"Python-studies\shop_shop_manager\assets\fonts\baby_doll.ttf", 36
)
FONT_CURSIVE = pygame.font.Font(
    r"Python-studies\shop_shop_manager\assets\fonts\skeetch.ttf", 36
)


with open(
    r"Python-studies\shop_shop_manager\assets\data\items\all_items.csv", "r"
) as file:
    all_items = np.genfromtxt(file, delimiter=",", dtype=str)


def load_image(image_path: str) -> pygame.Surface:    
    return pygame.image.load(image_path)


def load_sound(sound_path: str) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(sound_path)
