# Chicago Sewer Text Adventure Game

This is a simple text-based adventure game where you navigate through different rooms in the Chicago sewer system, collecting items to prepare for a final showdown with the Rat King. Your goal is to collect all six items before facing the Rat King in his hideout.

## Table of Contents
- [How to Play](#how-to-play)
- [Game Instructions](#game-instructions)
- [Rooms and Items](#rooms-and-items)
- [Code Overview](#code-overview)
- [License](#license)

## How to Play

1. **Run the game:**
   ```sh
   python3 sewer_adventure.py
   ```

2. **Follow the on-screen instructions:**
   - Move between rooms using commands like `go North`, `go South`, `go East`, `go West`.
   - Collect items using the command `get [item name]`.

3. **Objective:**
   - Collect all six items and then enter the Rat King's Hideout to win the game.

## Game Instructions

When the game starts, you will see the following instructions:
```
---------------------------------------------------
Chicago Sewer Text Adventure Game
Collect 6 items before you face off with the Rat King, or be defeated by him.
Move commands: go South, go North, go East, go West
Add to Inventory: get 'item name'
---------------------------------------------------
```

## Rooms and Items

### Room Dictionary
The game features the following rooms and items:

- **Water Treatment Plant**: No items, East to Sewer Control Room.
- **Sewer Control Room**: Contains "map", North to Maintenance Closet, East to Septic Tank, West to Water Treatment Plant, South to Pump Room.
- **Storage Chamber**: Contains "hazmat suit", East to Maintenance Closet.
- **Maintenance Closet**: Contains "flashlight", West to Storage Chamber, South to Sewer Control Room.
- **Pump Room**: Contains "rat-beating stick", North to Sewer Control Room, East to Ventilation Shaft.
- **Ventilation Shaft**: Contains "gas mask", West to Pump Room.
- **Septic Tank**: Contains "wedge of cheese", North to Rat King's Hideout, West to Sewer Control Room.
- **Rat King's Hideout**: Final room, no items.

### Player Inventory
- Start with an empty inventory.
- Collect items as you explore rooms.

## Code Overview

The game is implemented in Python and features the following functions:

- **`show_instructions()`**: Displays game instructions.
- **`get_new_state(direction_to_go, player_room)`**: Updates the player's current room based on the direction they move.
- **`get_item(item_to_pick_up, player_room)`**: Adds an item to the player's inventory if it is in the current room.
- **`show_status()`**: Displays the player's current status, including current room, items in the room, inventory, and available directions.

The game loop continues until the player reaches the Rat King's Hideout. Depending on whether all items have been collected, the player either defeats the Rat King or loses the game.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Enjoy your adventure in the Chicago sewers! If you have any questions or suggestions, feel free to reach out. Happy adventuring!
