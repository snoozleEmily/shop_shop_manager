# Shop Shop Manager Game

A turn-based management game created with [Pygame](https://github.com/pygame/pygame).

## What is it about?

Manage a shop in a fantasy world! Avoid bankruptcy by balancing your budget, negotiating deals, capitalizing on trades, and handling various items and clients. Trade with other merchants to build your fortune in a dynamic economy.

## Gameplay

Details about gameplay will be explained here.

## Contributing

Contributions are welcome! Below are some guidelines to help you get started:

### Rendering

Rendering functionality is limited due to a workaround implemented to fix a bug that caused all buttons to flicker. To maintain the default rendering behavior, handle specific cases in the **gameplay module** as needed.

### Adding a New Scene

To add a new scene:

1. Define a flag for the scene in the `GameScenes` class within the **scene_manager module**. Add it both as a variable and to the `scene_flags` dictionary.
2. To enable hover updates for buttons in the new scene, include the scene in the `trigger_hover` module within the **utils package**.
3. Declare the scene's flags in the **gameplay module**, ensuring consistency with the existing structure.

### Adding a New Button

To add a button:

1. Declare the button in the **declared_buttons module**. Currently, there are the following button types:
   - **default**: Placeholder box.
   - **caption_btn**: Button that contains text.
   - **checkbox_off**: Unchecked checkbox.
   - **checkbox_on**: Checked checkbox.
   - **exit**: Small door icon to exit scenes.
   - **settings**: Engine-like button that leads to the settings scene.
   - **dice_cup**: Used for the dice minigame.

2. For the hover effect to work, include the button in the `buttons_in_scene` dictionary within the `trigger_hover` module.

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
- Add the dialogue to the `trade` file.

#### Deal Dialogue

For deal-related dialogues:
- Add the dialogue to the `deals` file.

## License

This project is licensed under the GNU General Public License. For more details, see the [license file](\LICENSE).