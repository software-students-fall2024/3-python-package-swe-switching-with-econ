import random

# Global variable to keep track of the number of shots taken
global shots_taken

def start_game(bet amount):
    return
def get_commentary(action):
    return
def get_advice(advice_type):
    good_advice = [
        "Remember to take a break!",
        "Stopping after losing is the smarter option",
        "Drink water and stay hydrated!",
        "If you’re not having fun, it’s time to step away.",
    ]
    
    bad_advice = [
        "99 percent of all gamblers quit before they make it big",
        "You haven't really lost your money until you walk away",
        "No one remembers the person who lost 100 times but everyone remembers the person who won once",
        "It takes just 1 win to earn everything back",
        "If you lose you can just walk away and come back later. If you win once you're set for life",
    ]
    if advice_type.lower() == 'good':
        return random.choice(good_advice)
    elif advice_type.lower() == 'bad':
        return random.choice(bad_advice)
    else:
        return "I can only give 'good' or 'bad' advice!"
def calculate_hand_value(cards in hand):
    return

def take_shots(number_of_shots):

    # Check if the input is valid
    if type(number_of_shots) != int:
        print("Please enter a valid number of shots!")
    elif number_of_shots < 0:
        print("You can't take negative shots!")

    # Print the number of shots taken and increment the total number of shots taken
    print("You took {number_of_shots} shots!")
    shots_taken += number_of_shots

    # Print a message based on the number of shots taken
    if shots_taken <= 1:
        print("You feel great!")
    elif shots_taken <= 3:
        print("You feel tipsy!")
    elif shots_taken <= 5:
        print("You feel drunk!")
    elif shots_taken <= 7:
        print("Get me some car keys and let's go for a drive!")
    elif shots_taken <= 9:
        print("I am invincible!")
    elif shots_taken >= 10:
        print("You are wasted! Go home!")
        shots_taken = 0
    return