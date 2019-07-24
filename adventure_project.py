import time
import random


# Display text, then wait specified amount of time
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# Validate user input if 2 possible valid inputs
def valid_input_2(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("I didn't understand your response.")
            print_pause("Please enter one of the following responses:")
    return response


# Validate user input if 3 possible valid inputs
def valid_input_3(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print_pause("I didn't understand your response.")
            print_pause("Please enter one of the following responses:")
    return response


# Game introduction
def intro():
    print_pause("You find yourself at the entrance of a card "
                "tournament you plan to compete in.")
    print_pause("You've been preparing since it was announced.")
    print_pause("However, you heard that pro players entered the tournament "
                "last minute.")
    print_pause("Your normal cards might not be enough to win.")
    print_pause("As you head inside, you receive a map of the "
                "tournament venue from the polite clerk at the door.")


# Go to lobby
def travel_to_lobby(items):
    print_pause("You are at the tournament lobby.")
    if "legendary card" in items:
        print_pause("With the new card in your possession, "
                    "you should enter the tournament!")
    else:
        print_pause("The design of the lobby is relaxing to look at.")
        print_pause("You forget where you are and begin to space out...")
        print_pause("You shake your head back and forth and snap out of it.")
        print_pause("You contemplate entering the tournament now or"
                    " looking around the venue first.")
    look_at_map(items)


# Buy new legendary card from card merchant
def travel_to_merchant(items):
    print_pause("You approach the card merchant.")
    if "legendary card" in items:
        print_pause("You bought the card merchant's only copy.")
        print_pause("You should go somewhere else.")
    else:
        print_pause("You ask the card merchant if they have any new cards.")
        print_pause("'Got some rare things on sale, stranger!', he responds.")
        print_pause("You look at his collection and...")
        print_pause("Excelsior! The merchant had the exact card we needed!")
        items.append("legendary card")
        print_pause("You thank the merchant and continue on your way.")
    look_at_map(items)


# Generate random card
def legendary_card():
    cards = ["Blue Eyes White Dragon", "Exodia",
             "Holographic Charizard", "Holographic Blastoise", "C'thun",
             "Dark Magician", "Leeroy Jenkins", "SSJ Goku", "SSJ Broly"]
    legendary_card = random.choice(cards)
    return legendary_card


# Enter tournament; legendary card wins, no legendary loses
def travel_to_tournament(items):
    print_pause("You approach the tournament table.")
    if "legendary card" in items:
        print_pause("With the new card, you feel invincible!")
        choice = valid_input_2("Enter competition or come back later?\n"
                               "Enter 1 to compete in the tournament.\n"
                               "Enter 2 to come back later.\n",
                               "1", "2")
        if choice == '1':
            print_pause("You enter the tournament.")
            print_pause("After some grueling matches, you find yourself in "
                        "the tournament finals.")
            print_pause("Your opponent ends their turn with you in bad shape.")
            print_pause("Things are looking grim.")
            print_pause("There's only one card that can win this game.")
            print_pause("You close your eyes and draw from your deck.")
            print_pause("You play the card instantly without looking.")
            print_pause("It's the card from the merchant, the legendary "
                        + legendary_card() + "!!!")
            print_pause("It destroys your opponnent and wins you the game!")
            print_pause("Congratualations! You've won the tournament!")
            play_again()
        else:
            print_pause("You decide to come back later.")
            look_at_map(items)
    else:
        print_pause("You begin to enter the tournament.")
        print_pause("However, something is holding you back.")
        choice = valid_input_2("Enter competition or come back later?\n"
                               "Enter 1 to compete in the tournament.\n"
                               "Enter 2 to come back later.\n",
                               "1", "2")
        if choice == '1':
            print_pause("You brush that feeling off and enter.")
            print_pause("You enter the tournament.")
            print_pause("Even with the heart of the cards, "
                        "you were unable to defeat your first opponnent.")
            print_pause("You have been knocked out of the tournament.")
            play_again()
        else:
            print_pause("You decide to come back later.")
            look_at_map(items)


# Look at map, decide to go to one of three locations: lobby, merchant, and
# tournament areas. Once you complete an area, go to the next.
def look_at_map(items):
    print_pause("You take a look at the map and decide where to go: ")
    area = valid_input_3("Enter 1 to go to the lobby.\n"
                         "Enter 2 to go to card merchant.\n"
                         "Enter 3 to go to compete in the tournament.\n",
                         "1", "2", "3")
    if area == '1':
        travel_to_lobby(items)
    elif area == '2':
        travel_to_merchant(items)
    elif area == '3':
        travel_to_tournament(items)


# Play the card tournament game
def play_game():
    items = []
    intro()
    look_at_map(items)


# Ask user if they want to play again
def play_again():
    answer = valid_input_2("Would you like to play again?(y/n)\n",
                           "y", "n")
    if answer == 'y':
        print_pause("Here we go!")
        play_game()
    if answer == 'n':
        print_pause("See ya next time!")


play_game()
