import pygame

from utils.pygame_loads import FONT_BUTTON
from scenes.scene_manager import GameScenes
from scenes.tavern.dice import Die 
from scenes.tavern.tavern_scene import (
    dice_result,
    minigame_start_time,
    end_dice_ticks,
    render_tavern,
)

class Days:
    turn_day: bool = False
    max_days: int = 30
    current_day: int = 1

    def handle_days(self, display_surface):
        global dice_result, minigame_start_time, end_dice_ticks
        self.turn_day = True

        # Increment the day counter
        self.current_day += 1
        print(f"Day {self.turn_day} started and it's now {self.current_day} day.")

        # Update the display with the new day
        self.display_days(display_surface, self.current_day)

        # Reset minigame values so it can be played again
        dice_result = None
        minigame_start_time, end_dice_ticks = 0, 0
        Die.reset_dice() 
        
        # Return to town
        GameScenes.in_home, GameScenes.in_town  = False, True

        if self.current_day == self.max_days:
            print("Max days reached - game won or lost.")

    def display_days(self, display_surface, day):
        day = self.current_day
        day_string = f"Day: {day}"
        days_text = FONT_BUTTON.render(day_string, True, (255, 255, 255))
        border_surface = FONT_BUTTON.render(day_string, True, (0, 0, 0))

        # Get the size and position of the text
        text_rect = days_text.get_rect(topleft=(6, 3))

        # Draw the black border by adjusting the rect's position
        offsets = [-2, 2]  # Border offset values for top-left, top-right, etc.
        for dx in offsets:
            for dy in offsets:
                display_surface.blit(border_surface, text_rect.move(dx, dy))

        # Draw the white text on top
        display_surface.blit(days_text, text_rect.topleft)
