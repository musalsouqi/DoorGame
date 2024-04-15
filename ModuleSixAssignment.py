#Mustafa Alsouqi Intro to scripting. Module six game

#room dict
rooms = {
    "Water Treatment Plant": {"items": [], "East": "Sewer Control Room"},
    "Sewer Control Room": {"items": ["map"], "North": "Maintenance Closet", "East": "Septic Tank", "West": "Water Treatment Plant", "South": "Pump Room"},
    "Storage Chamber": {"items": ["hazmat suit"], "East": "Maintenance Closet"},
    "Maintenance Closet": {"items": ["flashlight"], "West": "Storage Chamber", "South": "Sewer Control Room"},
    "Pump Room": {"items": ["rat-beating stick"], "North": "Sewer Control Room", "East": "Ventilation Shaft"},
    "Ventilation Shaft": {"items": ["gas mask"], "West": "Pump Room"},
    "Septic Tank": {"items": ["wedge of cheese"], "North": "Rat King's Hideout", "West": "Sewer Control Room"},
    "Rat King's Hideout": {"items": [], "South": "Septic Tank"}
}

# Player Inventory
inventory = []

# Starting Room
current_room = "Water Treatment Plant"


# Pick up item automatically when called
def pick_up_item(room):
    for item in rooms[room]['items']:
        inventory.append(item)  # Add item to inventory
        print("You picked up the " + item)
    rooms[room]['items'] = []

# game loop
while True:
    # current room
    print("You are in the " + current_room)


    # Ask Player TO move
    direction = input("Which direction do you want to go? (North, South, East, West): ")

    # Update the room and check if it's actually a room
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
        print("Invalid direction.")


    # Check if all items are collected and if the player is in the Rat King's Hideout
    if all(item in inventory for room in rooms for item in
           rooms[room]['items']) and current_room == "Rat King's Hideout":
        print(
            "Congratulations! You've collected all the items and reached the Rat King's Hideout. You Have Defeated the Rat King!")
        break
    #this picks up items
    pick_up_item(current_room)