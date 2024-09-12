import pygame


from scenes.shop.shop_scene import render_shop
from scenes.inventory_scene import render_inventory
from scenes.tavern.tavern_scene import render_tavern
from scenes.home.home_scene import render_home, CountingSheep
from scenes.settings_scene import render_settings
from turns.day_turner import Days
from backgrounds import TOWN_IMG
from utils.pygame_loads import load_image
from utils.declared_buttons import (
    SHOP_BUTTON,
    IVENTORY_BUTTON,
    TAVERN_BUTTON,
    HOME_BUTTON,
    SETTINGS_BUTTON,
)
from utils.trigger_hover import (
    GameScenes,
    shop,
    inventory,
    tavern,
    home,
    settings,
)

days_instance = Days()


def main_game(display_surface, mouse_event, trigger_update=None):
    was_clicked = mouse_event.type == pygame.MOUSEBUTTONDOWN

    # Declare which buttons lead to which scenes
    if GameScenes.in_shop:
        if was_clicked:
            trigger_update = render_shop(display_surface, mouse_event)
        if shop.hover_check():
            render_shop(display_surface, mouse_event)

    elif GameScenes.in_inventory:
        if was_clicked:
            trigger_update = render_inventory(display_surface, mouse_event)
        if inventory.hover_check():
            render_inventory(display_surface, mouse_event)

    elif GameScenes.in_home:
        if was_clicked:
            trigger_update = render_home(display_surface, mouse_event)
        if home.hover_check():
            render_home(display_surface, mouse_event)

    elif GameScenes.in_tavern:
        if was_clicked:
            trigger_update = render_tavern(display_surface, mouse_event)
        if tavern.hover_check():
            render_tavern(display_surface, mouse_event)

    elif GameScenes.in_settings:
        if was_clicked:
            trigger_update = render_settings(display_surface, mouse_event)
        if settings.hover_check():
            render_settings(display_surface, mouse_event)

    elif (GameScenes.in_town and was_clicked) or days_instance.turn_day:
        display_surface.blit(load_image(TOWN_IMG), (0, 0))
        print(days_instance.turn_day)
        days_instance.display_days(display_surface, days_instance.current_day)

        # THE DAYS AREN'T BEING UPDATED ON SCREEN!!!!

        SHOP_BUTTON.draw_screen(display_surface)
        IVENTORY_BUTTON.draw_screen(display_surface)
        TAVERN_BUTTON.draw_screen(display_surface)
        HOME_BUTTON.draw_screen(display_surface)
        SETTINGS_BUTTON.draw_screen(display_surface)

        # Handle button click events:
        # Switch to shop scene
        if SHOP_BUTTON.update_scene(mouse_event, trigger_update):
            GameScenes.in_shop, GameScenes.in_town = True, False

        # Switch to inventory scene
        elif IVENTORY_BUTTON.update_scene(mouse_event, trigger_update):
            GameScenes.in_inventory, GameScenes.in_town = True, False

        # Switch to tavern scene
        elif TAVERN_BUTTON.update_scene(mouse_event, trigger_update):
            GameScenes.in_tavern, GameScenes.in_town = True, False

        # Switch to home scene
        elif HOME_BUTTON.update_scene(mouse_event, trigger_update):
            GameScenes.in_home, GameScenes.in_town = True, False

        # Switch to settings scene
        elif SETTINGS_BUTTON.update_scene(mouse_event, trigger_update):
            GameScenes.in_settings, GameScenes.in_town = True, False
