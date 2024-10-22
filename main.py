'''                                                                            import time
import threading

# Initialize player health
player_health = 100

def countdown():
    global player_health
    for _ in range(600):
        time.sleep(1)
        if player_health <= 0:
            return  # Exit if player health reaches zero
        print("", end='', flush=True)
    print("\nTime's up! The shadows have consumed you...")
    player_health = 0
    print("You have met your end.")

# Run countdown in a separate thread
timer_thread = threading.Thread(target=countdown)
timer_thread.start()


# print welcome message
print("Welcome to Dreams and Nightmares!")
print("You awake in a room. With three others. The air is cold, and the only light comes from a flickering candle. Shadows, dance on the walls...")
print("A sinister voice hisses through the darkness: 'Survive till dawn... or be consumed by the shadows forever.'")
print("You see three doors, each marked with a symbol: a decaying skull, a bleeding eye, and a severed hand. Each door whispers promises of salvation and threats of doom. Choose wisely... for your choice may be your last.")

#prompt user for a choice
doorChoice = input("> ").strip().lower()     #.strip(): This removes any extra spaces from the beginning and the end of the user's input. For example, if the user typed "  door  ", it would convert it to "door".
                                            #.lower(): This changes all the letters in the input to lowercase. So if the user typed "Door", it would change it to "door".

if doorChoice == "skull":
    print("You push open the door with the decaying skull symbol. The air grows colder, and the stench of death fills your lungs.")
    print("The room is dimly lit by flickering torches, casting eerie shadows on the walls. You see a long, narrow hallway lined with ancient, crumbling tombs.")
    print("As you step forward, the ground beneath you shifts, and skeletal hands burst from the floor, grasping at your ankles.")
    print("A ghostly figure materializes before you, its hollow eyes staring into your soul. 'You should not have come here,' it whispers, its voice echoing in your mind.")
    print("The walls begin to close in, and you realize you must escape before you are entombed forever...")
    
    action = input("Do you: (1) Struggle to break free, (2) Look for a hidden lever, (3) Scream for help? ").strip().lower()
    
    if action == "1":
        print("You struggle with all your might, but the skeletal hands tighten their grip. Your vision blurs, and you are dragged into the darkness, never to be seen again.")
        player_health = 0
        print("You have met your end.")
    elif action == "2":
        print("You frantically search the walls for a hidden lever. Just as the walls are about to crush you, your hand finds a small, cold lever. You pull it, and a hidden door swings open.")
        print("You stumble through, finding yourself in another chamber. You have narrowly escaped death, but the nightmare continues...")
        player_health -= 20 #Reducing health due to struggle
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
    print("Suddenly, the floor beneath you crumbles, and you fall into a dark pit filled with eerie whispers and shadowy figures.")
    print("Just as you feel despair closing in, you notice a faint, glowing inscription on the wall: 'To find the light, embrace the darkness.'")
    print("You muster your courage and follow the glowing path, which leads you to a hidden door. With trembling hands, you push it open and step into a room bathed in soft, warm light.")
    print("In the center of the room stands a pedestal with a shimmering crystal. You realize this might be your ticket out of this nightmare.")
    print("You reach for the crystal, but the shadows begin to close in around you again. With the last of your strength, you grasp the crystal, and a blinding light engulfs the room...")

    action = input("Do you: (1) Hold on to the crystal, (2) Drop the crystal and run, (3) Look for another exit? ").strip().lower()

    if action == "1":
        print("You hold onto the crystal, its warmth spreading through your body. The shadows retreat, and you feel a sense of calm. The room dissolves into light, and you awaken, safe and sound.")
        print("You have survived.")
    elif action == "2":
        print("You drop the crystal and run, but the shadows close in faster. You stumble and fall, consumed by the darkness.")
        player_health = 0
        print("You have met your end.")
    elif action == "3":
        print("You look for another exit, but the room is sealed tight. The shadows close in, and you are left with no choice but to fight. You clutch the crystal, and it shatters, filling the room with light. You are safe... for now.")
        print("You have narrowly escaped.")
        print("A door opens, Another chamber...")
        player_health -= 30
    else:
        print("Indecision seals your fate. The shadows consume you.")
        player_health = 0
        print("You have met your end.")

elif doorChoice == "hand":
    print("You choose the door marked with the severed hand. As you push it open, the air grows colder and a sense of dread seeps into your bones.")
    print("The room beyond is dimly lit by a flickering lantern hanging from a rusty chain. The walls are adorned with ancient, blood-stained runes, and the floor is covered in a thick layer of dust.")
    print("In the center of the room stands a grotesque statue, its many hands reaching out in silent agony. As you step closer, the hands begin to move, reaching towards you.")
    print("A voice whispers from the shadows, 'To escape this place, you must confront your deepest fears.'")
    print("Suddenly, one of the hands grabs you, pulling you closer to the statue. You feel panic rising, but then you notice a small, glimmering object clutched in one of the hands.")
    print("It's a key, and you realize this might be your way out. With a surge of determination, you grasp the key, feeling the hands tighten around you.")
    print("Just as you begin to lose hope, the statue's grip loosens, and the room starts to crumble. You rush to the door, key in hand, praying it's your escape...")

    action = input("Do you: (1) Use the key on the nearest door, (2) Search for another key, (3) Confront the statue? ").strip().lower()

    if action == "1":
        print("You use the key on the nearest door, and it clicks open. You stumble through, finding yourself outside in the cool night air. You have escaped the nightmare.")
        print("You have survived.")
    elif action == "2":
        print("You search for another key, but the statue's grip tightens, and the room starts to collapse. You are trapped and crushed under the debris.")
        player_health = 0
        print("You have met your end.")
    elif action == "3":
        print("You confront the statue, demanding it release you. The hands tighten, but you do not waver. Suddenly, the statue crumbles, revealing a hidden door behind it. You rush through.")
        print("You find yourself inside another chamber")
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
timer_thread.join()                                                                                              '''