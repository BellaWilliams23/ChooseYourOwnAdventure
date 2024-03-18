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

def main():
    boyfriend = choose_boyfriend()
    # Your story continues here, referencing the chosen boyfriend

if __name__ == "__main__":
    main()
print("\n**********************************************************")
#1. First commit ending
