import random

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