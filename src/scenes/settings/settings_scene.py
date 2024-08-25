import pygame

from scenes.states import GameScenes
from utils.buttons import EXIT_SCENE, SOUND_UP, SOUND_DOWN, ABOUT_INFO
from .volume_controller import VolumeController
from utils.pygame_loads import load_image
from backgrounds import PAPER_BACKGROUND


volume_controller = VolumeController()


def render_settings(display_surface, mouse_event, update_scene=None):
    display_surface.blit(load_image(PAPER_BACKGROUND), (0, 0))

    SOUND_UP.draw_screen(display_surface)
    SOUND_DOWN.draw_screen(display_surface)
    EXIT_SCENE.draw_screen(display_surface)
    ABOUT_INFO.draw_screen(display_surface)

    # Goes back to town if exit button is clicked
    if EXIT_SCENE.update_state(mouse_event, update_scene):
        GameScenes.in_town, GameScenes.in_settings = True, False

    if SOUND_UP.update_state(mouse_event, update_scene):
        volume_controller.increase_volume()

    if SOUND_DOWN.update_state(mouse_event, update_scene):
        volume_controller.decrease_volume()

    if ABOUT_INFO.update_state(mouse_event, update_scene):
        print("The information about the game will be here")

    pygame.display.flip()
