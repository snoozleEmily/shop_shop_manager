[WIP]

# Shop Shop Manager Game

It's a turn-based management game created with [Pygame](https://github.com/pygame/pygame).

## What is it about?

Manage a shop in a fantasy world. Avoid bankruptcy by balancing your budget, negotiating deals, capitalizing on trades, and handling various items and clients. Trade with other merchants to build your fortune in a dynamic economy.

## Gameplay

## License

It is licensed under the GNU General Public License. For more details, see the [full license file](\LICENSE).

## Contributing

Contributions are welcome! 
Here are a few points to consider:

### Rendering

The rendering is limited since it was the solution for a bug making all the buttons flicker. So, to make the game keep rendering in its default mode, you have to handle the specific case in the gameplay module.

### Adding A New Scene

If you want to add a new scene, you have to add a flag for it inside the GameScenes class from the scene_manager module, as a variable and to the scene_flags dictionary. Also, if you want to update the scene when hovering the buttons of it, add the scene to the trigger_hover module from the utils package. Finally, add the declared flags to the gameplay module following the current structure.

### Adding A New Button

If you want to add a button, simply declare it in the declared_buttons module. Currently, there are 5 options for buttons: "caption_btn" which is a placeholder box, "checkbox_off", "checkbox_on", "exit" which is a small door to exit scenes and "dice_cup" for the dice minigame.

In order for the hover effect to work on the new button, it must be added to the 'buttons_in_scene' dictionary in the trigger_hover module.