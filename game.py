import random

hatmanclue1 = False
hatmanclue2 = False
hatmanclue3 = False

eirahint1 = False
eirahint2 = False
eirahint3 = False


# Initialize player's health
player_health = 100  # Starting amount

def display_health():
    """Displays the player's current amount of health."""
    print(f"\nYou have {player_health} hp.\n")

def earn_health(amount):
    """Adds health to the player's total."""
    global player_health
    player_health += amount
    print(f"You earned {amount} hp!")

def spend_health(amount):
    """Deducts health from the player's total if they have enough."""
    global player_health
    if player_health >= amount:
        player_health -= amount
        print(f"You lost {amount} hp.")
    elif player_health <= 0:
        print("GAME OVER - You lost all your hp and died.")
        quit()
    else:
        ("Error - Please report to owner of code.")
        quit()




# Create an empty inventory
inventory = []

# Add an item
def add_item(item):
    inventory.append(item)
    print(f"You picked up: {item}")

# Remove an item
def remove_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"You dropped: {item}")
    else:
        print(f"You don't have {item}.")

# Show inventory
def show_inventory():
    print("Your inventory:")
    for item in inventory:
        print(f" - {item}")



















def scene1(): #Entrance
    choice = input("Trees tower above you, blocking the sun. You hear distant whispers and a crow caws overhead. What do you do? 'Wait' or 'Walk'>").lower
    if choice == "wait":
        print("After a few moments of silence, you hear a low whisper behind you. You spin around - nothing. But a faint set of footprints in the mud weren’t there before...")
        print("You go to follow the footsteps but they end as soon as they begin. Ultimately you keep moving in that direction after collecting a branch from the floor.")
        hatmanclue1 = True
        add_item("Stick")
        scene2()
    elif choice == "walk":
        print("You collect a branch and begin your journey")
        add_item("Stick")
        scene2()
    else:
        print("ERROR - INCORRECT INPUT")
        scene1()




def scene2(): #Mossy Path
    choice = input("You walk until you find a mossy path. The path is slippery and lined with strange, glowing mushrooms. A small river cuts across the trail. You hear rustling in the bushes. What do you do? 'Check' the bushes, 'Investigate' the river, 'Ignore' the surroundings and cross the river> ").lower
    if choice == "check":
        print("Before you can check over the bush, you notice a note on a branch. You open it and it reads:")
        print("'I marked the safe paths with moss bundles. Do not trust the signs.'")
        print("It also includes a hand-drawn picture of a man with wide-brimmed hat, scribbled out. And a following sentence.")
        print("'He followed me too...'")
        eirahint1 = True
        print("After reading the note you explore the area past the bush and you find it curled beneath a fallen log - a small fox, whimpering, its leg twisted unnaturally. Blood mats the fur. It watches you with wide, pained eyes, but doesn't run. It couldn't.")
        fox = input("What do you do? 'Help' it, 'Kill' it, 'Leave' it> ").lower
        if fox == "help":
            print("You lift the log up and the fox scurries away you feel a quick sense of warm wind flowing past your pushing the fox to safety.")
            fox_status = "Saved"
            scene2()
        elif fox == "kill":
            print("You steady your hand. It doesn't scream - it just... stops.")
            fox_status = "Killed"
            scene2()
        elif fox == "leave":
            print("You take a step back over the bush. It watches. You walk on. The sound of its cries follow you for a while.")
            fox_status = "Left"
            scene2()
        else:
            print("ERROR - INCORRECT INPUT")
            scene2()
    elif choice == "investigate":
        print("You see a mysterious black hat flow past on the river. It's old. Torn. Still wet. You pick the hat up to examine it more.")
        print("Suddenly you hear footsteps behind you. You turn quickly in hope to catch your stalker but see no one. You pick up the hat and carry on your journey.")
        add_item("Wet Hat")
        hatmanclue2 = True
    elif choice == "ignore":
        print("You decide to cross the river.")
        scene3()
    else:
        print("ERROR - INCORRECT INPUT")
        scene2()    

print("A LIGHT IN THE DARK")
print("You wake up on a bed of moss, beneath a sky you don't recognize.")
scene1()