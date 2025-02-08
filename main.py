# main.py
from world import World
from entities import Player
from inventory import Inventory

def main():
    print("Welcome to AI Dungeon Master!")
    print("1. Start New Game\n2. Quit")

    choice = input("Choose an option: ")
    if choice == "1":
        start_game()
    else:
        print("Goodbye!")

def start_game():
    player = Player("Adventurer")
    inventory = Inventory()
    world = World()
print("Your journey begins...")
    
    while player.health > 0:
        location = world.get_location()
        print(f"You arrive at {location['name']}: {location['description']}")
        
        if location['enemy']:
            print(f"A wild {location['enemy']} appears!")
            battle(player, location['enemy'])
        
        action = input("What do you do? (explore/inventory/quit): ")
        if action == "explore":
            continue
        elif action == "inventory":
            print("Inventory:", inventory.items)
        elif action == "quit":
            break

    if player.health <= 0:
        print("You have perished! Game Over.")
def battle(player, enemy):
    print(f"Battling {enemy}...")
    while player.health > 0:
        print(f"Your HP: {player.health}")
        action = input("Choose an action (attack/flee): ")
        if action == "attack":
            print(f"You attack the {enemy}!")
            # Simple attack logic
            player.health -= 10  # Simulate damage
            print(f"The {enemy} attacks back!")
        elif action == "flee":
            print("You flee back to safety!")
            break

if __name__ == "__main__":
    main()
