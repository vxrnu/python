# Excercise 1:Room Structure
room_foyer = {
    "id": "foyer",
    "name": "The Grand Entrance",
    "description": "A vast, marble hall ... ",
    "exits": {}                
}
 
room_hallway = {
    "id": "hallway",
    "name": "The Grand Hallway",
    "description": "A vast, long hallway ... ",
    "exits": {}                
}
 
# Exercise 2: Item Structure
item_key = {
    "name": "Brass Key",
    "description": "A tarnished key.",
    "can_be_picked_up": True
}
 
# Exercise 3: Master Data Structeres
 
# The WORLD holds all rooms
WORLD = {
    "foyer": room_foyer,
    "hallway": room_hallway
}
 
# The INVENTORY is a list
PLAYER_INVENTORY = [item_key]
 
# Validation
print(f"Locations: {len(WORLD)}")
 
# Exercise 4: Connecting Rooms
 
# Add an exit to the Foyer
WORLD["foyer"]["exits"] = {
    "west": "hallway"
}
 
# Add the return path
WORLD["hallway"]["exits"] = {
    "east": "foyer"
}
 
# Test the connection
print(WORLD["foyer"]["exits"]["west"])
# Output: "hallway"
 
# Exercise 5: Adding items to a room
 
# 1. Create the list in the room
WORLD["hallway"]["items"] = []
 
# 2. Create the item
item_map = {
    "name": "Old Map",
    "can_be_picked_up": True
}
 
# 3. Add item to the room
WORLD["hallway"]["items"].append(item_map)
 
#Exercise 6
CURRENT_ROOM_ID = "foyer"
 
def display_room_info(room_id):
    # Retrieve the entire room dictionary
    current_room = WORLD[room_id]
    print(f"\n# {current_room['name'].upper()} #")
    print(current_room['description'])
    # Display keys from the exits dictionary
    print("\nAvailable Exits:", list(current_room['exits'].keys()))
# Test Code:
print("--- Starting Game Location ---")
display_room_info(CURRENT_ROOM_ID)


 