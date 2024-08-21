import pygame

from ui_controls.clickables import Clickable
from scenes.states import GameScenes
from .volume_controller import VolumeController
from pygame_loads import load_image
from backgrounds import PAPER_BACKGROUND

EXIT_SCENE = Clickable(740, 330, text=None, type_tag="exit_scene")
SOUND_UP = Clickable(15, 15, text=None, type_tag="box")
SOUND_DOWN = Clickable(67, 15, text=None, type_tag="box")

volume_controller = VolumeController()


def render_settings(display_surface, mouse_event, update_scene=None):
    display_surface.blit(load_image(PAPER_BACKGROUND), (0, 0))

    SOUND_UP.draw_screen(display_surface)
    SOUND_DOWN.draw_screen(display_surface)
    EXIT_SCENE.draw_screen(display_surface)

    # Goes back to town if exit button is clicked
    if EXIT_SCENE.update_state(mouse_event, update_scene):
        GameScenes.in_town, GameScenes.in_settings = True, False

    if SOUND_UP.update_state(mouse_event, update_scene):
        volume_controller.increase_volume()

    if SOUND_DOWN.update_state(mouse_event, update_scene):
        volume_controller.decrease_volume()

    pygame.display.flip()
