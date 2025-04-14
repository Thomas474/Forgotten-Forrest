import random

# Define all global variables properly
fox_status = None  # <- Initialize fox_status

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
    choice = input("Trees tower above you, blocking the sun. You hear distant whispers and a crow caws overhead. What do you do? 'Wait' or 'Walk'>").lower()
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
    choice = input("You walk until you find a mossy path. The path is slippery and lined with strange, glowing mushrooms. A small river cuts across the trail. You hear rustling in the bushes. What do you do? 'Check' the bushes, 'Investigate' the river, 'Ignore' the surroundings and cross the river> ").lower()
    if choice == "check":
        print("Before you can check over the bush, you notice a note on a branch. You open it and it reads:")
        print("'I marked the safe paths with moss bundles. Do not trust the signs.'")
        print("It also includes a hand-drawn picture of a man with wide-brimmed hat, scribbled out. And a following sentence.")
        print("'He followed me too...'")
        eirahint1 = True
        print("After reading the note you explore the area past the bush and you find it curled beneath a fallen log - a small fox, whimpering, its leg twisted unnaturally. Blood mats the fur. It watches you with wide, pained eyes, but doesn't run. It couldn't.")
        fox = input("What do you do? 'Help' it, 'Kill' it, 'Leave' it> ").lower()
        if fox == "help":
            print("You lift the log up and the fox scurries away you feel a quick sense of warm wind flowing past your pushing the fox to safety. You grab a glowing mushroom off the bush and return to the path.")
            fox_status = "Saved"
            add_item("Glowing Mushroom")
            scene2()
        elif fox == "kill":
            print("You steady your hand. It doesn't scream - it just... stops. You grab a glowing mushroom off the bush and return to the path.")
            fox_status = "Killed"
            add_item("Glowing Mushroom")
            scene2()
        elif fox == "leave":
            print("You take a step back. It watches. You walk on. The sound of its cries follow you for a while. You grab a glowing mushroom off the bush and return to the path.")
            fox_status = "Left"
            add_item("Glowing Mushroom")
            scene2()
        else:
            print("ERROR - INCORRECT INPUT")
            scene2()
    elif choice == "investigate":
        print("You see a mysterious black hat flow past on the river. It's old. Torn. Still wet. You pick the hat up to examine it more.")
        print("Suddenly you hear footsteps behind you. You turn quickly in hope to catch your stalker but see no one. You pick up the hat and carry on your journey.")
        add_item("Wet Hat")
        hatmanclue2 = True
        scene2()
    elif choice == "ignore":
        print("You decide to cross the river.")
        scene3()
    else:
        print("ERROR - INCORRECT INPUT")
        scene2()    




def scene3(): #Fork Path
    print("You cross the river and come across a fork in the path. A wooden signpost points in two directions: Left: 'Shelter' Right: 'Darkness' The sign is scratched and weathered - someone tried to alter the wording.")
    choice = input("What will you do? Go 'Left' , go 'Right' , or 'Inspect' the sign.> ").lower()
    if choice == "left":
        print("You turn left and head towards the shelter.")
        scene4()
    elif choice == "right":
        print("You head towards the darkness.")
        scene5()
    elif choice == "inspect":
        print("There's something scratched just below the arrows. A warning? 'He waits in the dark, but the fire makes him flee.'")
        hatmanclue3 = True
        print("You look down after reading the warning and discover a broken compass which lies half-buried in the dirt. There is a note scratched on the back: 'The cave entrance was hidden. Found it by accident. Could be a way out... if I survive it.'")
        eirahint2 = True
        print("You take a step back and return to the path.")
        scene3()
    elif eirahint3 == True:
        secretscene()
    else:
        print("ERROR - INCORRECT INPUT")
        scene3()




def scene4(): #Shelter
    choice = input("An old wooden cabin stands silently. Windows are shattered, and the door creaks open. Inside, it's dusty and cluttered with old survival gear. Will you 'Explore' the cabin or 'Turn' around?").lower()
    if choice == "explore":
        print("You decide to explore the cabin and enter it.")
        area4()
    elif choice == "turn":
        print("You turn around and head back to the fork in the road.")
        scene3()
    else:
        print("ERROR - INCORRECT INPUT")
        scene4()




def area4(): #Exploring the cabin
    choice = input("You enter the cabin and see a 'fire' place and a 'key' holder. What will you explore first? Or will you 'leave'?").lower()
    if choice == "fire":
        print("Using the fire you light your stick on fire to use as a torch.")
        remove_item("Stick")
        add_item("Torch")
        area4()
    elif choice == "key":
        print("You find a key and open the rusty chest in the corner with it.You find a letter")
        print("Eira's Final Letter:")
        print("If you're reading this, then maybe... maybe someone else made it here after all.")
        print("I don't know what day it is. I don't know how long I've been running. The forest doesn't keep time - it stretches it, wraps it around your ankles until you forget who you were.")
        print("I used to think I could map this place. I drew trees, marked stones, left string like breadcrumbs. But the forest moves. I swear it moves.")
        print("I've heard things. Whispers, mostly. One voice louder than the rest. It's kind, sometimes. It warned me once. Told me not to open the gate near the roots. I didn’t listen.")
        print("If you found the chest, maybe you're close. Or maybe you're already lost. Either way, listen to me:")
        print("Don't trust the light. It can be false.")
        print("Don't follow your own footprints. They may not be yours.")
        print("And if you see him - the man with no face but a hat too heavy - don't run. Just close your eyes. Sometimes he forgets things that way.")
        print("I'm going to stay here. The forest took everything else, but it won't take what's left of me.")
        print("I hope you're braver than I was. Or luckier. Or maybe just smarter.")
        print("There's still a path. Not the one on the map. The past the water.")
        print("Good luck, stranger.")
        print("- Eira")
        print("")
        eirahint3 = True
        area4()
    elif choice == "leave":
        print("You exit the cabin and return to the fork in the road.")
        scene3()
    else:
        print("ERROR - INCORRECT INPUT")
        area4()




def secretscene():
    print("You head towards the waterfall in hope of the exit told to you by Eira.")
    if fox_status == "Saved":
        print("Before you go, you hear a whisper - 'The forest remembers kindness.'")
        print("When you step through the water, it doesn't feel wet - just weightless. Like stepping into a memory. You vanish. No pain. No sound. Just light.")
        quit()
    elif fox_status == "Killed":
        print("The waterfall is silent. Too silent. When you step into the mist, your reflection waits for you. But its eyes aren't yours. Behind you, branches creak. The Hatted Man doesn't move - he doesn't have to. The fox is there, too. Bones now. But its eyes glow all the same. You chose survival over mercy. The water rejects you. The forest keeps what it claims. Your torch flickers. Then dies.")
        quit()
    elif fox_status == "Left":
        print("You approach the waterfall, but something's wrong. The mist is thick. Wrong. It coils like smoke, not water. As you step forward, you hear it again - a whimper. Weak. Familiar. The fox is still there. Still waiting. Still in pain. You didn't help it then. You can't help it now. You try to walk through the falls... but it's not a passage. It's a mirror. You didn't choose cruelty. But you chose nothing. The forest offers nothing in return.")
        quit()
    else:
        print("ERROR - REPORT TO OWNER OF CODE.")
        quit()




def scene5():
    print("You head to the darkness which turns out to be a cave.")
    if fox_status == "Saved":
        print("The cave is pitch black. Your torch flickers.. But then, just when it starts to die - another glow joins it. The fox. Its fur now glows with the light of something not-of-this-world. It leads you deeper... and deeper still... You crawl through a narrow crevice. A final squeeze. Then: light. You emerge into a new place. Not the forest. Not the world you left. But peace. Not all paths out are paths back.")
        quit()
    elif fox_status == "Killed":
        print("The cave collapses behind you as you move deeper. The air thickens. The stone walls feel too warm. You hear breathing that's not yours. Then - a light. A figure in the dark. The Hatted Man, but... different. He's not chasing you. He's waiting. You realize: This was never an exit. This was a feeding ground. You don't scream. There's no time. The forest doesn't waste what it takes.")
        quit()
    elif fox_status == "Left":
        print("The cave twists downward, deeper and deeper, like the throat of a beast. You don't notice when your torch goes out. You just keep moving. Eventually, you find an opening. A way out. But when you step outside... The trees are the same. The stone is the same. You're back at the start. Except it's not the same forest. It never is. You escaped the forest. But you didn't escape the story.")
        quit()




print("A LIGHT IN THE DARK")
print("You wake up on a bed of moss, beneath a sky you don't recognize.")
scene1()