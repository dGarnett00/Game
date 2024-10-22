import random

# Initialize player health and weapons
player_health = 100
weapon_health = {"gun": 10, "shovel": 75, "stick": 50}
chosen_weapon = None

def weapon_durability(weapon):
    if weapon:
        if weapon == "gun":
            weapon_health[weapon] -= 1
            if weapon_health[weapon] <= 0:
                print(f"Your {weapon} has run out of bullets!")
                return None
        else:
            weapon_health[weapon] -= 10
            if weapon_health[weapon] <= 0:
                print(f"Your {weapon} has broken!")
                return None
    return weapon

print("You find yourself in another chamber, heart pounding. The air is thick with tension, and shadows twist and turn, hiding the insidious devil lurking within.")
print("Suddenly, you spot three potential weapons: a Gun (10 bullets), a Shovel, and a Stick. Choose one to take with you for the remainder of your journey, but be warned, each use will degrade its durability.")

# Prompt user to choose a weapon
weapon_choice = input("Choose your weapon (gun, shovel, stick): ").strip().lower()
if weapon_choice in weapon_health:
    chosen_weapon = weapon_choice
    print(f"You pick up the {chosen_weapon}, feeling a slight sense of relief. But this is no time to relax.")
else:
    print("You hesitate, unsure of which weapon to choose. The devil lurks closer...")

print("The insidious devil emerges from the shadows, a grotesque figure with eyes burning like coals. It snarls, and you must act fast.")

# Scenarios with health-damaging situations
while player_health > 0:
    action = input("Do you: (1) Attack with your weapon, (2) Dodge the attack, (3) Look for an escape route? ").strip().lower()
    
    if action == "1" and chosen_weapon:
        chosen_weapon = weapon_durability(chosen_weapon)
        if chosen_weapon:
            print(f"You strike with your {chosen_weapon}. The devil recoils, but your weapon's durability decreases.")
            player_health -= 10
        else:
            print("With no weapon left, you are defenseless. The devil lunges at you.")
            player_health -= 30
    elif action == "2":
        if random.random() < 0.5:  # 50% chance to dodge successfully
            print("You successfully dodge the attack, but the devil is relentless.")
        else:
            print("You try to dodge, but the devil slashes at you, reducing your health.")
            player_health -= 20
    elif action == "3":
        if random.random() < 0.3:  # 30% chance to find escape route
            print("You find a narrow passage and squeeze through, escaping the devil's immediate grasp.")
            break
        else:
            print("You search frantically for an escape, but the devil catches up, and you are forced to fight.")
            player_health -= 15
    else:
        print("Indecision is deadly. The devil strikes, and you are left vulnerable.")
        player_health -= 25
    
    if player_health <= 0:
        print("You have succumbed to your injuries. The devil has won.")
        break

if player_health > 0:
    print(f"You have survived the encounter with {player_health} health remaining. Your journey continues, but the horror is far from over...")
else:
    print("Game over.")
