from turns.day_turner import Days


class CountingSheep(Days):
    grow_dark = False

    def end_minigame(self, display_surface):
        """Call this method after the minigame ends"""
        # self.grow_dark = False  # Reset background to daylight
        self.handle_days(display_surface)  # Move to next day
