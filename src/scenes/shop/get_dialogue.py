import json
import random

with open(
    r"Python-studies\shop_shop_manager\assets\data\dialogues\sale.json", "r"
) as file:
    sale_speech = json.load(file)

# Persistent variable outside of the function
last_dialogue = []


def get_dialogue() -> dict:
    tickets_amount = (
        6
        # Futurely, this should depend on the amount of tickets the user has
        # and add +3 or so to it
    )

    def is_dialogue_new(dialogue: dict) -> bool:
        # Checks if the dialogue has not been seen in the last <tickets_amount> dialogues
        return dialogue["id"] not in [d["id"] for d in last_dialogue]

    while True:
        dialogue = random.choice(sale_speech)
        if is_dialogue_new(dialogue):
            if len(last_dialogue) >= tickets_amount:
                last_dialogue.pop(0)
            last_dialogue.append(dialogue)
            return dialogue


if __name__ == "__main__":
    for _ in range(50):
        print(get_dialogue())
        print("")
