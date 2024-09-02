from scenes.tavern.tavern_scene import die_face


class Days:
    max_days: int = 30
    current_day: int = 1


def handle_days(turn_day: bool):
    global die_face
    if turn_day:
        print(die_face)

        # This doesn't work - How can I get rid of the global die_face?
        if die_face is not None:
            del die_face

        Days.current_day += 1
        print(die_face)

    if Days.current_day == Days.max_days:
        print("Max days reached - game won or lost.")


# I'm making a day (turns) file for my pygame. What am I missing?
