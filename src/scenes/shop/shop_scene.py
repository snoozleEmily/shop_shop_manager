import pygame
from typing import Optional, Callable

from ui_controls.clickables import Clickable
from scenes.states import GameScenes, Dialogue
from pygame_loads import load_image
from backgrounds import SHOP_BACKGROUND
from pygame_loads import FONT_DEFAULT
from .display_customer import display_customer
from .get_dialogue import get_dialogue

EXIT_SCENE = Clickable(740, 330, text=None, type_tag="exit_scene")
NEXT = Clickable(700, 200, text=None, type_tag="box")


def display_dialogue(display_surface: pygame.Surface, dialogue_text) -> pygame.Surface:
    # Get and display the dialogue
    if not Dialogue.dialogue_displayed:
        dialogue_dict = get_dialogue()
        dialogue = dialogue_dict.get("speech", "")
        Dialogue.dialogue_text = FONT_DEFAULT.render(dialogue, True, (0, 0, 0))
        Dialogue.displayed_count += 1

        if Dialogue.displayed_count == 1 and Dialogue.dialogue_text:
            Dialogue.dialogue_displayed = True
            print(f"Rendering Dialogue Text: {Dialogue.dialogue_text}")
            display_surface.blit(Dialogue.dialogue_text, (100, 137))
            print(Dialogue.dialogue_displayed)
    else:
        if Dialogue.dialogue_text:
            display_surface.blit(Dialogue.dialogue_text, (100, 137))


def render_shop(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    update_scene: Optional[Callable] = None,
    _selected_character=[None],
):

    display_surface.blit(load_image(SHOP_BACKGROUND), (0, 0))
    display_customer(display_surface, _selected_character)
    display_dialogue(display_surface, Dialogue.dialogue_text)

    NEXT.draw_screen(display_surface)

    # Goes back to town if exit button is clicked
    EXIT_SCENE.draw_screen(display_surface)
    if EXIT_SCENE.update_state(mouse_event, update_scene):
        Dialogue.dialogue_displayed = True
        GameScenes.in_town, GameScenes.in_shop = True, False

    pygame.display.flip()
