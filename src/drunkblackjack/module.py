import random

# Global variable to keep track of the number of shots taken
global shots_taken

def start_game(bet_amount):
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
        if shots_taken < 4:
            return random.choice(hit_normal)
        else:
            return random.choice(hit_drunk)
    elif action.lower() == 'stand':
        if shots_taken < 4:
            return random.choice(stand_normal)
        else:
            return random.choice(stand_drunk)
    elif action.lower() == 'bust':
        return random.choice(bust)
    else:
        return "I can only commentate on 'hit', 'stand', or 'bust' actions."
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
def calculate_hand_value(cards_in_hand):
    return


def take_shots_reset():
    global shots_taken
    shots_taken = 0
    return "You are sober again!"

def take_shots(number_of_shots):

    # Validates the input
     if type(number_of_shots) != int:
        return "Please enter a valid number of shots!"
     elif number_of_shots < 0:
        return "You can't take negative shots!"
     else:
        # Increments the global variable shots_taken by the number of shots taken
        # Print a message based on the total number of shots taken
        global shots_taken
        shots_taken += number_of_shots
        if shots_taken <= 1:
            return "You feel great!"
        elif shots_taken <= 3:
            return "You feel tipsy!"
        elif shots_taken <= 5:
            return "You feel drunk!"
        elif shots_taken <= 7:
            return "Get me some car keys and let's go for a drive!"
        elif shots_taken <= 9:
            return "I am invincible!"
        elif shots_taken >= 10:
            take_shots_reset()
            return "You are wasted! Go home!"
        return