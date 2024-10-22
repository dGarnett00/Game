import threading  #for running the countdown in a separate thread
import time       # for the countdown timer
import random       # for random outcomes

# Initialize player health
player_health = 100

def countdown():
    global player_health
    for _ in range(600): # loop for 600seconds (10mins)
        time.sleep(1) # pause for 1 second
        if player_health <= 0: # Check if player health is 0 or less
            return  # Exit function if player health reaches zero
        print("", end='', flush=True) # Print a dot every second to show countdown
    print("\nTime's up! The shadows have consumed you...") # Message when time is up
    player_health = 0 #set player health to 0
    print("You have met your end.") # message when player health reaches 0

# Run countdown in a separate thread
timer_thread = threading.Thread(target=countdown)
timer_thread.start() # start countdown timer   

# Function to add a 10-second timer for each decision
def decision_timer():
    for _ in range(10):
        time.sleep(1)
        print("", end='', flush=True)
    print("\nTime's up! You took too long to decide...")
    return False

# Get user and companions' names
player_name = input("Enter your name: ").strip() # prompt for the user name
companion_names = []
for i in range(3):
    companion_name = input(f"Enter the name of companion {i + 1}: ").strip() # prompt for the companions name
    companion_names.append(companion_name)

# Print welcome message
print(f"Welcome to Dreams and Nightmares, {player_name}!") # greets player
print(f"You awake in a room with your companions, {', '.join(companion_names)}. The air is cold, and the only light comes from a flickering candle. Shadows dance on the walls...")
print("A sinister voice hisses through the darkness: 'Survive till dawn... or be consumed by the shadows forever.'")
print("You see three doors, each marked with a symbol: a decaying skull, a bleeding eye, and a severed hand. Each door whispers promises of salvation and threats of doom. Choose wisely... for your choice may be your last.")

# Prompt user for a choice
doorChoice = input("> ").strip().lower() #door choice

if doorChoice == "exit":  # Check if user wants to exit the game
    print("You have chosen to exit the game. Goodbye!")
    player_health = 0  # End the game
elif doorChoice == "skull":
    print("You push open the door with the decaying skull symbol. The air grows colder, and the stench of death fills your lungs.")
    print("The room is dimly lit by flickering torches, casting eerie shadows on the walls. You see a long, narrow hallway lined with ancient, crumbling tombs.")
    print(f"{companion_names[0]} whispers, 'This place gives me the creeps...'")  # Companion dialogue

    print("As you step forward, the ground beneath you shifts, and skeletal hands burst from the floor, grasping at your ankles.")
    print(f"{companion_names[1]} shouts, 'We need to find a way out, quick!'")  # Companion dialogue


    action = input("Do you: (1) Struggle to break free, (2) Look for a hidden lever, (3) Scream for help? ").strip().lower()
    timer_thread_action = threading.Thread(target=decision_timer)
    timer_thread_action.start()
    timer_thread_action.join()
    
    if action == "1":
        print("You struggle with all your might, but the skeletal hands tighten their grip. Your vision blurs, and you are dragged into the darkness, never to be seen again.")
        player_health = 0
        print("You have met your end.")
    elif action == "2":
        print("You frantically search the walls for a hidden lever. Just as the walls are about to crush you, your hand finds a small, cold lever. You pull it, and a hidden door swings open.")
        print(f"{companion_names[2]} says, 'Good job, let's move!' You stumble through, finding yourself in another chamber. You have narrowly escaped death, but the nightmare continues...")  # Companion dialogue
        player_health -= 20  # Reducing health due to struggle
    elif action == "3":
        print("You scream for help, your voice echoing off the tomb walls. The ghostly figure's laugh fills your ears as the skeletal hands drag you down.")
        player_health = 0
        print("Your screams fade into silence. You have met your end.")
    else:
        print("Indecision seals your fate. The walls close in, and you are entombed forever.")
        player_health = 0
        print("You have met your end.")

elif doorChoice == "eye":
    print("You choose the door with the bleeding eye symbol. As the door creaks open, a chilling breeze sweeps over you, and you find yourself in a pitch-black corridor.")
    print("The walls are lined with ominous paintings of eyes, each one seemingly following your every move. A sense of unease washes over you.")
    print(f"{companion_names[0]} mutters, 'I don't like this one bit...'")  # Companion dialogue
    print("Suddenly, the floor beneath you crumbles, and you fall into a dark pit filled with eerie whispers and shadowy figures.")
    print(f"{companion_names[1]} yells, 'Watch out!'") # Companion dialogue

    action = input("Do you: (1) Hold on to the crystal, (2) Drop the crystal and run, (3) Look for another exit? ").strip().lower()
    timer_thread_action = threading.Thread(target=decision_timer)
    timer_thread_action.start()
    timer_thread_action.join()

    if action == "1":
        print("You hold onto the crystal, its warmth spreading through your body. The shadows retreat, and you feel a sense of calm. The room dissolves into light, and you awaken, safe and sound.")
        print(f"{companion_names[2]} says, 'You did it, we're safe... for now.'")  # Companion dialogue
        print("You have survived.")
    elif action == "2":
        print("You drop the crystal and run, but the shadows close in faster. You stumble and fall, consumed by the darkness.")
        player_health = 0
        print(f"{companion_names[2]}'s voice fades, 'No... not like this...' You have met your end.") # Companion dialogue
    elif action == "3":
        print("You look for another exit, but the room is sealed tight. The shadows close in, and you are left with no choice but to fight. You clutch the crystal, and it shatters, filling the room with light. You are safe... for now.")
        print("You have narrowly escaped.")
        print("A door opens to another chamber...")
        player_health -= 30
    else:
        print("Indecision seals your fate. The shadows consume you.")
        player_health = 0
        print("You have met your end.")

elif doorChoice == "hand":
    print("You choose the door marked with the severed hand. As you push it open, the air grows colder and a sense of dread seeps into your bones.")
    print("The room beyond is dimly lit by a flickering lantern hanging from a rusty chain. The walls are adorned with ancient, blood-stained runes, and the floor is covered in a thick layer of dust.")
    print(f"{companion_names[0]} whispers, 'Stay alert, something's not right...'") # Companion dialogue
    print("In the center of the room stands a grotesque statue, its many hands reaching out in silent agony. As you step closer, the hands begin to move, reaching towards you.")
    print(f"{companion_names[1]} shouts, 'Look out!'") # Companion dialogue

    action = input("Do you: (1) Use the key on the nearest door, (2) Search for another key, (3) Confront the statue? ").strip().lower()
    timer_thread_action = threading.Thread(target=decision_timer)
    timer_thread_action.start()
    timer_thread_action.join()

    if action == "1":
        print("You use the key on the nearest door, and it clicks open. You stumble through, finding yourself outside in the cool night air. You have escaped the nightmare.")
        print("You have survived.")
    elif action == "2":
        print("You search for another key, but the statue's grip tightens, and the room starts to collapse. You are trapped and crushed under the debris.")
        player_health = 0
        print("You have met your end.")
    elif action == "3":
        print("You confront the statue, demanding it release you. The hands tighten, but you do not waver. Suddenly, the statue crumbles, revealing a hidden door behind it. You rush through.")
        print(f"{companion_names[2]} says, 'We made it... barely.' You find yourself inside another chamber.") # Companion dialogue
        player_health -= 20
    else:
        print("Indecision seals your fate. The statue's hands tighten around you, and you are crushed.")
        player_health = 0
        print("You have met your end.")

else:
    print("Invalid choice. The shadows inch closer as your indecision seals your fate...")
    player_health = 0
    print("You have met your end.")

# Display remaining health
if player_health > 0:
    print(f"You have {player_health} health remaining.")
else:
    print("Game over.")

timer_thread.join()
