import json
import random

from .get_item import get_item

with open(
    r"Python-studies\shop_shop_manager\assets\data\dialogues\sale.json", "r"
) as file:
    sale_speech = json.load(file)

# Persistent variable outside of the function
last_dialogue = []


def get_dialogue() -> tuple:
    energy_level = (
        6  # Maximum number of dialogues to store in memory
        # Futurely, this should depend on the amount of energy levels the user has
        # and add +3 or so to it to avoid repeated dialogues
    )

    def is_dialogue_new(dialogue: dict) -> bool:
        """
        Checks if the dialogue has not been seen in the last few dialogues.

        Parameters:
            dialogue (dict): The dialogue dictionary to check.

        Returns:
            bool: True if the dialogue is new, False otherwise.
        """
        return dialogue["id"] not in [d["id"] for d in last_dialogue]

    while True:
        dialogue = random.choice(sale_speech)
        
        if is_dialogue_new(dialogue):
            
            # Manage the memory of past dialogues
            if len(last_dialogue) >= energy_level:
                last_dialogue.pop(0)
                
            last_dialogue.append(dialogue)            

            # Replace 'ITEM' in the dialogue text with a random item
            updated_text, item_details = get_item(dialogue["speech"])
            dialogue["speech"] = updated_text

            return dialogue, item_details


if __name__ == "__main__":
    # To test if is_dialogue_new is working
    # run for _ in range(len(sale_speech))
    print(get_dialogue())