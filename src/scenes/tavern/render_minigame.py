import pygame

from .dice import Die
from utils.pygame_loads import load_image
from utils.declared_buttons import DICE_CUP
from backgrounds import DICE_TABLE


die1: Die = Die()
die2: Die = Die()


def roll_dice(display_surface, mouse_event, trigger_update=None) -> pygame.Surface:
    # Only display the DICE_CUP if the dice have not been rolled yet
    if not Die.dice_rolled:
        display_surface.blit(load_image(DICE_TABLE), (97, 50))
        DICE_CUP.draw_screen(display_surface)
        if DICE_CUP.update_scene(mouse_event, trigger_update):
            dice_path1 = die1.get_face()
            dice_path2 = die2.get_face()

            Die.dice_path = [
                load_image(dice_path1),
                load_image(dice_path2),
            ]

            # Show the result for both dice
            print(f"You rolled a {die1.face} and a {die2.face}!")

            Die.dice_rolled = True

            return Die.dice_path
