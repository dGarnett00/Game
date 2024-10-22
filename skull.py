doorChoice = input("> ").strip().lower()  # door choice

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