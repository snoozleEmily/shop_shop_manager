import pygame
from typing import Optional, Callable


from .dice import Die
from scenes.scene_manager import GameScenes
from scenes.tavern.cloud import Cloud
from .render_minigame import roll_dice
from utils.pygame_loads import load_image
from utils.container import render_container
from scenes.tavern.sky_mingame import render_sky
from backgrounds import TAVERN_IMG, DICE_TABLE
from utils.declared_buttons import ROLL_DICE, SKY, RETURN, EXIT_SCENE

minigame_start_time = 0
end_dice_ticks = 0
dice_result = None

# Delays added to prevent rapid button clicks
RETURN_DELAY = 400  # milliseconds
ROLL_DICE_DELAY = 360  # milliseconds


def render_tavern(
    display_surface: pygame.Surface,
    mouse_event: pygame.event.Event,
    trigger_update: Optional[Callable] = None,
) -> None:
    global minigame_start_time, end_dice_ticks, dice_result
    display_surface.blit(load_image(TAVERN_IMG), (0, 0))

    # Display the container
    container_width, container_height = 688, 360
    render_container(
        display_surface,
        47,
        20,
        container_width,
        container_height,
        "black-ish",
    )
    current_time = pygame.time.get_ticks()

    # Show ROLL_DICE button if the minigame is not active
    if not Die.minigame_active and not Cloud.minigame_active:
        # Wait if the minigame has ended before showing ROLL_DICE again
        if current_time - end_dice_ticks >= ROLL_DICE_DELAY:
            
            ROLL_DICE.draw_screen(display_surface)
            if ROLL_DICE.update_scene(mouse_event, trigger_update):
                Die.minigame_active = True
                minigame_start_time = pygame.time.get_ticks()  # Record start time

                # If there was a previous result, use it
                if dice_result:
                    Die.dice_path = dice_result

        # Goes back to town if exit button is clicked
        EXIT_SCENE.draw_screen(display_surface)  # Not visible in minigame
        if EXIT_SCENE.update_scene(mouse_event, trigger_update):
            GameScenes.in_town, GameScenes.in_tavern = True, False    
    
    # Displays the dice minigame
    if Die.minigame_active:
        display_surface.fill((0, 0, 0))  # Make the background black
        roll_dice(display_surface, mouse_event, trigger_update)

        # Keep the result of minigame on screen after it has ended
        if Die.dice_path:
            display_surface.blit(load_image(DICE_TABLE), (97, 50))
            display_surface.blit(Die.dice_path[0], (300, 150))  # Dice 1 positioning
            display_surface.blit(Die.dice_path[1], (383, 180))  # Dice 2 positioning

        # Wait for the delay before showing the RETURN button
        if current_time - minigame_start_time >= RETURN_DELAY:
            RETURN.draw_screen(display_surface)
            if RETURN.update_scene(mouse_event, trigger_update):
                Die.minigame_active = False
                Die.dice_path = None  # Clear path to remove the minigame screen display
                dice_result = Die.dice_path  # Save the result of the dice roll
                end_dice_ticks = pygame.time.get_ticks()  # Record end minigame time

    SKY.draw_screen(display_surface)
    if SKY.update_scene(mouse_event, trigger_update):
        render_sky(display_surface, mouse_event)
        GameScenes.in_sky, GameScenes.in_tavern = True, False 
        return