from scenes.tavern.tavern_scene import (
    last_game_result,
    minigame_start_time,
    return_click_time,
)


class Days:
    turn_day: bool = False
    max_days: int = 30
    current_day: int = 1

    def handle_days(self, display_surface, turn_day):
        global last_game_result, minigame_start_time, return_click_time

        if turn_day:
            self.current_day += 1

            last_game_result = None  # Rest dice minigame
            minigame_start_time, return_click_time = 0, 0

        if self.current_day == self.max_days:
            print("Max days reached - game won or lost.")
