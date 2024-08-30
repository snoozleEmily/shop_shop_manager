import pygame

from scenes.states import GameScenes
from .volume_controller import VolumeController
from utils.pygame_loads import load_image
from backgrounds import PAPER_BACKGROUND
from utils.buttons import (
    EXIT_SCENE,
    SOUND_UP,
    SOUND_DOWN,
    NEXT_SONG,
    PREVIOUS_SONG,
    ABOUT_INFO,
)


volume_controller = VolumeController()


def render_settings(display_surface, mouse_event, trigger_update=None):
    display_surface.blit(load_image(PAPER_BACKGROUND), (0, 0))

    NEXT_SONG.draw_screen(display_surface)
    PREVIOUS_SONG.draw_screen(display_surface)
    SOUND_UP.draw_screen(display_surface)
    SOUND_DOWN.draw_screen(display_surface)
    ABOUT_INFO.draw_screen(display_surface)
    EXIT_SCENE.draw_screen(display_surface)

    if NEXT_SONG.update_scene(mouse_event, trigger_update):
        pass

    if PREVIOUS_SONG.update_scene(mouse_event, trigger_update):
        pass

    if SOUND_UP.update_scene(mouse_event, trigger_update):
        volume_controller.increase_volume()

    if SOUND_DOWN.update_scene(mouse_event, trigger_update):
        volume_controller.decrease_volume()

    if ABOUT_INFO.update_scene(mouse_event, trigger_update):
        print("The information about the game will be here")

    # Goes back to town if exit button is clicked
    if EXIT_SCENE.update_scene(mouse_event, trigger_update):
        GameScenes.in_town, GameScenes.in_settings = True, False
