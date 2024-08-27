import pygame

from scenes.states import GameScenes
from scenes.shop.shop_scene import render_shop
from scenes.inventory_scene import render_inventory
from scenes.home_scene import render_home
from scenes.settings.settings_scene import render_settings
from turns.display_days import display_days
from backgrounds import TOWN_BACKGROUND
from utils.pygame_loads import load_image
from utils.buttons import (
    SHOP_BUTTON,
    IVENTORY_BUTTON,
    HOME_BUTTON,
    SETTINGS_BUTTON,
)


def main_game(display_surface, mouse_event, trigger_update=None):
    was_clicked = mouse_event.type == pygame.MOUSEBUTTONDOWN

    # Declare which buttons lead to which scenes
    if GameScenes.in_shop and was_clicked:
        # print("In Shop Scene") # Debug
        trigger_update = render_shop(display_surface, mouse_event)

    elif GameScenes.in_inventory and was_clicked:
        # print("In Inventory Scene")  # Debug
        trigger_update = render_inventory(display_surface, mouse_event)

    elif GameScenes.in_home and was_clicked:
        # print("In Home Scene")  # Debug
        trigger_update = render_home(display_surface, mouse_event)

    elif GameScenes.in_settings and was_clicked:
        # print("In Settings Scene")  # Debug
        trigger_update = render_settings(display_surface, mouse_event)

    elif GameScenes.in_town and was_clicked:
        # print("In Town Scene")  # Debug
        display_surface.blit(load_image(TOWN_BACKGROUND), (0, 0))
        display_days(display_surface)

        SHOP_BUTTON.draw_screen(display_surface)
        IVENTORY_BUTTON.draw_screen(display_surface)
        HOME_BUTTON.draw_screen(display_surface)
        SETTINGS_BUTTON.draw_screen(display_surface)

        # Handle button click events:
        # Switch to shop scene
        if SHOP_BUTTON.update_scene(mouse_event, trigger_update):
            GameScenes.in_shop, GameScenes.in_town = True, False

        # Switch to inventory scene
        elif IVENTORY_BUTTON.update_scene(mouse_event, trigger_update):
            GameScenes.in_inventory, GameScenes.in_town = True, False

        # Switch to home scene
        elif HOME_BUTTON.update_scene(mouse_event, trigger_update):
            GameScenes.in_home, GameScenes.in_town = True, False

        # Switch to settings scene
        elif SETTINGS_BUTTON.update_scene(mouse_event, trigger_update):
            GameScenes.in_settings, GameScenes.in_town = True, False
