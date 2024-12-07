import pygame

from .dice import Die
from utils.pygame_loads import load_image
from utils.declared_buttons import DICE_CUP
from backgrounds import DICE_TABLE


first_die: Die = Die()
second_die: Die = Die()

# The dice minigame MUST be set to default (erase result)
# when the day turns

def roll_dice(display_surface, mouse_event, trigger_update=None) -> pygame.Surface:
    # Only display the DICE_CUP if the dice have not been rolled yet
    if not Die.dice_rolled:
        display_surface.blit(load_image(DICE_TABLE), (97, 50))
        
        DICE_CUP.draw_screen(display_surface)
        if DICE_CUP.update_scene(mouse_event, trigger_update):
            first_path = first_die.get_face()
            second_path = second_die.get_face()

            Die.dice_path = [
                load_image(first_path),
                load_image(second_path),
            ]

            # Show the result for both dice
            print(f"You rolled a {first_die.face} and a {second_die.face}!")

            Die.dice_rolled = True

            return Die.dice_path
