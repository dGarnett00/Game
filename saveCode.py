''' 
def decision_timer():
    for _ in range(10):
        time.sleep(1)
        print("", end='', flush=True)
    print("\nTime's up! You took too long to decide...")
    return False



timer_thread_action = threading.Thread(target=decision_timer)
    timer_thread_action.start()
    timer_thread_action.join() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if doorChoice == "exit":  # Check if user wants to exit the game
    print("You have chosen to exit the game. Goodbye!")
    player_health = 0  # End the game
elif doorChoice == "skull":
    print("You push open the door with the decaying skull symbol. The air grows colder, and the stench of death fills your lungs."
    
        
    
    
    '''
    
    
    
    
elif doorChoice == "skull":
    print("You push open the door with the decaying skull symbol. The air grows colder, and the stench of death fills your lungs.")
    print("The room is dimly lit by flickering torches, casting eerie shadows on the walls. You see a long, narrow hallway lined with ancient, crumbling tombs.")
    print(f"{companion_names[0]} whispers, 'This place gives me the creeps...'")  # Companion dialogue

    print("As you step forward, the ground beneath you shifts, and skeletal hands burst from the floor, grasping at your ankles.")
    print(f"{companion_names[1]} shouts, 'We need to find a way out, quick!'")  # Companion dialogue

    action = input("Do you: (1) Struggle to break free, (2) Look for a hidden lever, (3) Scream for help, or (4) Use your weapon? ").strip().lower()
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
        print("In this chamber, you notice two paths: one leads deeper into the tomb, while the other seems to have an exit sign written in glowing runes.")

        next_action = input("Do you: (1) Follow the path into the depths, (2) Head towards the glowing exit, or (3) Examine the tombs for treasure? ").strip().lower()

        if next_action == "1":
            print("You venture deeper into the tomb, the air thickening with secrets and shadows. You feel a sense of dread creeping up your spine as laughter echoes around you.")
            # Add more scenarios for this path
        
        elif next_action == "2":
            print("You decide to follow the glowing runes. As you step into the light, the skeletal hands retreat. You find yourself at the exit, but must solve a riddle to leave.")
            # Add riddle logic here
        
        elif next_action == "3":
            print("Among the tombs, you discover a glimmering artifact! However, it awakens the spirits of the tomb, and they lash out for your soul.")
            # Add combat logic here

        else:
            print("Confused by your choices, you hesitate. The tomb begins to trap you, and you must make a decision!")
        
    elif action == "3":
        print("You scream for help, your voice echoing off the tomb walls. The ghostly figure's laugh fills your ears as the skeletal hands drag you down.")
        player_health = 0
        print("Your screams fade into silence. You have met your end.")
        
    elif action == "4":
        print(f"You draw your weapon, preparing to fight off the skeletal hands. With a swift movement, you slash through the grip of the undead.")
        print(f"{companion_names[0]} cheers, 'That’s the spirit! Let’s fight our way through.'")
        # Assuming a combat scenario
        combat_result = combat_skeletons()  # A function that handles combat mechanics

        if combat_result:
            print("You have successfully defeated the skeletal hands! However, the chamber begins to collapse.")
            # Continue exploring options after combat
            
            print("You notice a pristine, glowing skull lying on the ground amidst the rubble.")
            treasure_action = input("Do you: (1) Take the skull, (2) Leave it be and exit, or (3) Examine it carefully? ").strip().lower()

            if treasure_action == "1":
                print("As you take the skull, a rush of power courses through you. Maybe this will aid you in your adventure...")
                player_inventory.append("glowing skull")  # Assuming you have an inventory system
            
            elif treasure_action == "2":
                print("You decide that some treasures are not worth the risk. You run towards the exit just in time as the room crumbles behind you.")
            
            elif treasure_action == "3":
                print("Your careful examination reveals ancient inscriptions. They provide clues about the tombs ahead. You gain valuable knowledge for your quest.")
            
            else:
                print("Indecision seals your fate. The walls close in, and you are entombed forever.")
                player_health = 0
                print("You have met your end.")
        
    else:
        print("Indecision seals your fate. The walls close in, and you are entombed forever.")
        player_health = 0
        print("You have met your end.")