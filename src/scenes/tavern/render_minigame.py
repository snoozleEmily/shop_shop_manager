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
        Dice.dice_path = load_image(dice_path)

        if die.face == 1:
            print("You rolled a 1!")
        elif die.face == 2:
            print("You rolled a 2!")
        elif die.face == 3:
            print("You rolled a 3!")
        elif die.face == 4:
            print("You rolled a 4!")
        elif die.face == 5:
            print("You rolled a 5!")
        elif die.face == 6:
            print("You rolled a 6!")

        return Dice.dice_path
