import pygame

from scenes.states import GameScenes
from scenes.shop.shop_scene import render_shop
from scenes.inventory_scene import render_inventory
from scenes.home_scene import render_home
from scenes.settings.settings_scene import render_settings
from backgrounds import TOWN_BACKGROUND
from utils.pygame_loads import load_image
from utils.buttons import (
    SHOP_BUTTON,
    IVENTORY_BUTTON,
    HOME_BUTTON,
    SETTINGS_BUTTON,
)


def main_game(display_surface, mouse_event, update_scene=None):
    # Declare which buttons lead to which scenes
    if GameScenes.in_shop:
        update_scene = render_shop
        update_scene(display_surface, mouse_event)

    elif GameScenes.in_inventory:
        update_scene = render_inventory
        update_scene(display_surface, mouse_event)

    elif GameScenes.in_home:
        update_scene = render_home
        update_scene(display_surface, mouse_event)

    elif GameScenes.in_settings:
        update_scene = render_settings
        update_scene(display_surface, mouse_event)

    else:
        # Handle button click events

        display_surface.blit(load_image(TOWN_BACKGROUND), (0, 0))
        SHOP_BUTTON.draw_screen(display_surface)
        IVENTORY_BUTTON.draw_screen(display_surface)
        HOME_BUTTON.draw_screen(display_surface)
        SETTINGS_BUTTON.draw_screen(display_surface)

        # Switch to shop scene
        if SHOP_BUTTON.update_state(mouse_event, update_scene):
            GameScenes.in_shop, GameScenes.in_town = True, False

        # Switch to inventory scene
        elif IVENTORY_BUTTON.update_state(mouse_event, update_scene):
            GameScenes.in_inventory, GameScenes.in_town = True, False

        # Switch to home scene
        elif HOME_BUTTON.update_state(mouse_event, update_scene):
            GameScenes.in_home, GameScenes.in_town = True, False

        # Switch to settings scene
        elif SETTINGS_BUTTON.update_state(mouse_event, update_scene):
            GameScenes.in_settings, GameScenes.in_town = True, False

    pygame.display.flip()
