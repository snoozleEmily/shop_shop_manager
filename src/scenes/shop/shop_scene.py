import pygame
from typing import Optional, Callable

from utils.clickables import Clickable
from scenes.states import GameScenes, Dialogue
from utils.pygame_loads import load_image
from backgrounds import SHOP_BACKGROUND
from .display_customer import display_customer
from .display_dialogue import display_dialogue

EXIT_SCENE = Clickable(740, 330, text=None, type_tag="exit_scene")
NEXT = Clickable(327, 309, text=None, type_tag="box")


def render_shop(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    update_scene: Optional[Callable] = None,
    _selected_character=[None],
):

    display_surface.blit(load_image(SHOP_BACKGROUND), (0, 0))
    display_dialogue(display_surface)
    display_customer(display_surface, _selected_character, force_update=False)

    # Goes to next sales dialogue if next button is clicked
    NEXT.draw_screen(display_surface)
    if NEXT.update_state(mouse_event, update_scene):
        Dialogue.dialogue_displayed = False
        display_dialogue(display_surface)
        display_customer(display_surface, _selected_character, force_update=True)

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_state(mouse_event, update_scene):
        Dialogue.dialogue_displayed = True
        GameScenes.in_town, GameScenes.in_shop = True, False

    pygame.display.flip()
