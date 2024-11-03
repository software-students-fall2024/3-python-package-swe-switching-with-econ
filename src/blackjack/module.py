import random

# Global variable to keep track of the number of shots taken
global shots_taken

def start_game(bet amount):
    return
def get_commentary(action):
    hit_normal = [
        "Taking a chance, I see!",
        "Not satisfied yet?",
        "Feeling lucky?", 
        "Brace yourself for another card!",
    ]
    stand_normal = [
        "Playing it safe, I like it.",
        "Happy with what you have?", 
        "A wise choice, perhaps?", 
        "Let's see what the dealer has...",
    ]
    hit_drunk = [
        "This is DEFINITELY a good idea!",
        "There's no way this can backfire!",
        "You NEED another card! And maybe another drink!",
    ]
    stand_drunk = [
        "But what if you got another card anyway...?",
        "Aww, but what if your total could be higher?",
        "You're SO confident that you'll win with this hand!"
    ]
    bust = [
        "Ouch! That's a bust!", 
        "Over 21, better luck next time.", 
        "You flew too close to the sun.",
        "Unlucky! The dealer takes it!"
    ]
    if action.lower() == 'hit':
        if shots_taken < 5:
            return random.choice(hit_normal)
        else:
            return random.choice(hit_drunk)
    elif action.lower() == 'stand':
        if shots_taken < 5:
            return random.choice(stand_normal)
        else:
            return random.choice(stand_drunk)
    elif action.lower() == 'bust':
        return random.choice(bust)
    else:
        return "I can commentate on 'hit', 'stand', or 'bust' actions."
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