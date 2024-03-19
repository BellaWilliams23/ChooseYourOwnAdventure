# Programmer: Bella Williams
# Date: 3.15.2024
# Program: Choose Your Own Adventure

import sys

print("**********************************************************")
print("\nWelcome to Boyfriend Simulator!\n")
print("In this simulation you will be given scenarios and options")
print("that will determine how your relationship works out!")
print("\nThis is your opportunity to see what encounters you might come")
print("across in a relationship and play around with it.")
print("\n**********************************************************\n")

# Prompt the player to start
start_game = input("Type 'start' to begin: ")
if start_game.lower() != "start":
    print("Invalid input. Please type 'start' to begin the game.")
    sys.exit()

#1. AI code to pick boyfriend's name

def choose_boyfriend():
    print("\nWelcome to the Choose Your Boyfriend Simulator!")
    print("Please choose your boyfriend from the following options:")
    print("1. Lewis")
    print("2. Pierce")
    print("3. Andrew")
    print("4. Blake")

    while True:
        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            boyfriend = "Lewis"
            break
        elif choice == "2":
            boyfriend = "Pierce"
            break
        elif choice == "3":
            boyfriend = "Andrew"
            break
        elif choice == "4":
            boyfriend = "Blake"
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    print("You've chosen", boyfriend, "as your boyfriend.")

    return boyfriend

def story_intro(boyfriend):
    print("\nYou and", boyfriend, "met under interesting circumstances. Here's how it happened:\n")
    if boyfriend == "Lewis":
        print("You matched with Lewis on a dating app and decided to meet for coffee. The conversation flowed effortlessly, and you both felt an instant connection.")
    elif boyfriend == "Pierce":
        print("You bumped into Pierce at a coffee shop while waiting in line. You struck up a conversation, and he ended up asking for your number before you left.")
    elif boyfriend == "Andrew":
        print("You met Andrew at a friend's party. Despite the noisy atmosphere, you found yourselves engrossed in conversation the whole night.")
    elif boyfriend == "Blake":
        print("You were browsing books at the library when Blake approached you, mistaking you for someone else. The mix-up led to a humorous conversation and eventually exchanging numbers.")

def loyalty_test():
    print("\nYou and your boyfriend have been together for a while now, and you're deeply committed to each other.")
    print("While you're out shopping, another guy approaches you and asks for your number, seemingly interested in you.")
    print("What do you do?")
    print("1. Give him your number.")
    print("2. Politely decline and mention you're in a committed relationship.")

    strike = 0
    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            print("\nYou decided to give him your number.")
            strike += 1
            break
        elif choice == "2":
            print("\nYou politely declined and mentioned that you're in a committed relationship.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    return strike

def main():
    boyfriend = choose_boyfriend()
    story_intro(boyfriend)
    strikes = loyalty_test()
    print("\nYou currently have", strikes, "strike(s) against you.")
    if strikes >= 3:
        print("Unfortunately, your relationship didn't survive the loyalty test. You've been dumped.")
    else:
        print("Congratulations! Your relationship passed the loyalty test.")

if __name__ == "__main__":
    main()
print("\n\**********************************************************")
#1. First commit ending
