class Days:
    max_days: int = 30
    current_day: int = 1


def handle_days(turn_day: bool):
    if turn_day:
        Days.current_day += 1

    if Days.current_day == Days.max_days:
        print("Max days reached - game won or lost.")
