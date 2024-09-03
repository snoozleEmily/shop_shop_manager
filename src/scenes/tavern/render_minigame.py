import pygame

from .dice import Dice
from utils.pygame_loads import load_image
from utils.declared_buttons import DICE_CUP

die: Dice = Dice()


def render_minigame(
    display_surface, mouse_event, trigger_update=None
) -> pygame.Surface:
    DICE_CUP.draw_screen(display_surface)
    if DICE_CUP.update_scene(mouse_event, trigger_update):
        dice_path = die.roll()
        Dice.die_face = load_image(dice_path)

        return Dice.die_face
