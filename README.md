[WIP]
# Shop Shop Manager Game

[NOTE] The idea is to make a game that allows the player to analyse data while having fun. Please, do take into consideration that developing this kind of program takes some time (specially with a full time job), but eventuall I will finish it because I simply want to play and turn messy data into golden coins.

A fun **data analysis game** created with [Pygame](https://github.com/pygame/pygame).

## What is it about?

Do you have an analitical eye? You better or else you will not win.
Avoid bankruptcy, balancing your budget, negotiating deals, capitalizing on trades, and handling various items and clients by managing a shop in a fantasy world! Trade with other merchants to build your fortune in a dynamic economy. 

## Gameplay

Details about gameplay will be explained here.

## Contributing

**Contributions are welcome!** Below are some guidelines to help you get started:

### Adding a New Scene

To add a new scene you must define a flag for the scene in the `GameScenes` class within the **scene_manager module**.

### Adding a New Button

To add a button:

1. Declare the button in the **declared_buttons module**. Currently, there are the following button types:
   - **default**: Placeholder box. (It is not supposed to be used in the final game; it is solely for development.)
   - **caption_btn**: Button that contains text.
   - **checkbox_off**: Unchecked checkbox.
   - **checkbox_on**: Checked checkbox.
   - **exit**: Small door icon to exit scenes.
   - **settings**: Engine-like button that leads to the settings scene.
   - **dice_cup**: Used for the dice minigame.

### Adding a New Item

To add an item to the game:

1. Edit the **all_items.csv** file located in the `assets > data > items` directory.
2. Add the item's details as follows:
   - **Item**: Name of the item.
   - **Price**: Float value representing the item's price.
   - **Type**: Item category. If unsure, label it as "odd type."

### Adding a New Dialogue

To add dialogue to the game, edit the relevant JSON file in the `assets > data > dialogues` directory.

#### Customer Dialogue

For customer dialogues:
- Add the dialogue to the `sale` file.
- Assign a unique ID (integer).
- Ensure the **text (speech)** includes the word "ITEM" (in all caps). The game relies on this keyword for functionality.

#### Supplier Dialogue

For supplier dialogues:
- Add the dialogue to the `supply` file.
- Assign a unique ID (integer).
- Ensure the **text (speech)** includes the word "SUPPLY_ITEM" and "NUMBER" (in all caps). The game relies on these keyword for functionality.

#### Trade Dialogue

For deal-related dialogues:
- Add the dialogue to the `trade` file.
- Assign a unique ID (integer).
- Ensure the **text (speech)** includes the words "TRADE_ITEM" and "SELF_ITEM" (in all caps). The game relies on these keyword for functionality.

## License

This project is licensed under the GNU General Public License. This means you are free to build upon the current code to develop the game further, but you must credit the original author and distribute any modifications under the same license. For more details, see the [license file](\LICENSE).
