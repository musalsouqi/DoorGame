# Mustafa Alsouqi Intro to scripting. Project 2

# Room dictionary
rooms = {
    "Water Treatment Plant": {"items": '', "east": "Sewer Control Room"},
    "Sewer Control Room": {"items": "map", "north": "Maintenance Closet", "east": "Septic Tank",
                           "west": "Water Treatment Plant", "south": "Pump Room"},
    "Storage Chamber": {"items": "hazmat suit", "east": "Maintenance Closet"},
    "Maintenance Closet": {"items": "flashlight", "west": "Storage Chamber", "south": "Sewer Control Room"},
    "Pump Room": {"items": "rat-beating stick", "north": "Sewer Control Room", "east": "Ventilation Shaft"},
    "Ventilation Shaft": {"items": "gas mask", "west": "Pump Room"},
    "Septic Tank": {"items": "wedge of cheese", "north": "Rat King's Hideout", "west": "Sewer Control Room"},
    "Rat King's Hideout": {"items": ''}
}

# Player Inventory
inventory = []

# Starting Room
current_room = "Water Treatment Plant"


# Function to show instructions
def show_instructions():
    print("---------------------------------------------------")
    print("Chicago Sewer Text Adventure Game")
    print("Collect 6 items before you face off with the Rat King, or be defeated by him.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("---------------------------------------------------")


def get_new_state(direction_to_go, player_room):
    if direction_to_go in rooms[player_room]:
        player_room = rooms[player_room][direction_to_go]
        return player_room
    else:
        print("Invalid direction.")
        return player_room


def get_item(item_to_pick_up, player_room):
    if 'items' in rooms[current_room]:
        if item_to_pick_up in rooms[player_room]['items']:
            inventory.append(item_to_pick_up)  # Add item to inventory
            del rooms[player_room]['items']  # Remove item from room
            print("You picked up the " + item_to_pick_up)
        else:
            print("That Item Is not in this room.")
    else:
        print("That Item Is not in this room.")


def show_status():
    print("You are in the " + current_room)
    # print the item if it exists
    if 'items' in rooms[current_room]:
        item_in_room = rooms[current_room]['items']
        print("You see a " + item_in_room)
    else:
        print("There are no items in this room!")
    # prints inventory
    print('Inventory:' + str(inventory))
    # Print available directions
    available_directions = [direction for direction in rooms[current_room] if direction != 'items']
    print("Available directions: " + ', '.join(available_directions))
    print('-----------------')


# Show instructions
show_instructions()

# game loop
while current_room != "Rat King's Hideout":
    show_status()

    # Ask player to move or get item
    action = input("Enter your move:").lower().split()

    # Check if quit
    if action[0] == 'quit':
        print("Thanks for playing!")
        break

    # Check if move or get
    elif action[0] == 'go' or action[0] == 'get':

        # check if the action is to move
        if action[0] == 'go':
            direction_from_user = action[1]
            current_room = get_new_state(direction_from_user, current_room)

        # Check if the action is to get an item
        elif action[0] == 'get':
            item_name = action[1]
            get_item(item_name, current_room)

# checks for game completion
if len(inventory) == 6 and current_room == "Rat King's Hideout":
    print("Congratulations! You've collected all the items and reached the Rat King's Hideout. You Have Defeated "
          "the Rat King!")
elif current_room == "Rat King's Hideout":
    print("GAME OVER! YOU DIDN'T COLLECT ALL THE ITEMS TO DEFEAT THE RAT KING!")
