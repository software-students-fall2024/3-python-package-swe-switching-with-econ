import pytest
from drunkblackjack import module
import random


class Tests:

    random.seed(0)

    # Test if the function returns one of the good advices
    def test_get_good_advice(self):
        advice = module.get_advice('good')
        assert advice in [
            "Remember to take a break!",
            "Stopping after losing is the smarter option",
            "Drink water and stay hydrated!",
            "If you’re not having fun, it’s time to step away"
        ]

    # Test if the function returns one of the bad advices
    def test_get_bad_advice(self):
        advice = module.get_advice('bad')
        assert advice in [
            "99 percent of all gamblers quit before they make it big",
            "You haven't really lost your money until you walk away",
            "No one remembers the person who lost 100 times but everyone remembers the person who won once",
            "It takes just 1 win to earn everything back",
            "If you lose you can just walk away and come back later. If you win once you're set for life"
        ]

    # Test if the function returns an error message for invalid advice type
    def test_get_advice_invalid_input(self):
        advice = module.get_advice('neutral')
        assert advice == "I can only give 'good' or 'bad' advice!"

    # Test if the function is case insensitive for 'good' and 'bad'
    def test_get_advice_case_insensitivity(self):
        good_advice_lower = module.get_advice('good')
        good_advice_upper = module.get_advice('GOOD')
        bad_advice_lower = module.get_advice('bad')
        bad_advice_upper = module.get_advice('BAD')
    
        assert good_advice_lower == good_advice_upper
        assert bad_advice_lower == bad_advice_upper
        assert good_advice_lower in [
            "Remember to take a break!",
            "Stopping after losing is the smarter option",
            "Drink water and stay hydrated!",
            "If you’re not having fun, it’s time to step away"
        ]
        assert bad_advice_lower in [
            "99 percent of all gamblers quit before they make it big",
            "You haven't really lost your money until you walk away",
            "No one remembers the person who lost 100 times but everyone remembers the person who won once",
            "It takes just 1 win to earn everything back",
            "If you lose you can just walk away and come back later. If you win once you're set for life"
        ]

    # Test for the function take_shots_reset
    def test_take_shots_reset(self):
        assert module.take_shots_reset() == "You are sober again!"

    # Test for the function take_shots with invalid inputs
    def test_take_shots_negative(self):
        assert module.take_shots(-1) == "You can't take negative shots!"
    def test_take_shots_invalid(self):
        assert module.take_shots("a") == "Please enter a valid number of shots!"

    # Test for the function take_shots with valid inputs
    def test_take_shots_0(self):
        assert module.take_shots(0) == "You feel great!"
    def test_take_shots_1(self):
        module.take_shots_reset()
        assert module.take_shots(1) == "You feel great!"
    def test_take_shots_2(self): 
        module.take_shots_reset()
        assert module.take_shots(2) == "You feel tipsy!"
    def test_take_shots_3(self):
        module.take_shots_reset()
        assert module.take_shots(3) == "You feel tipsy!"
    def test_take_shots_4(self):
        module.take_shots_reset()
        assert module.take_shots(4) == "You feel drunk!"
    def test_take_shots_5(self):
        module.take_shots_reset()
        assert module.take_shots(5) == "You feel drunk!"
    def test_take_shots_6(self):
        module.take_shots_reset()
        assert module.take_shots(6) == "Get me some car keys and let's go for a drive!"
    def test_take_shots_7(self):
        module.take_shots_reset()
        assert module.take_shots(7) == "Get me some car keys and let's go for a drive!"
    def test_take_shots_8(self):
        module.take_shots_reset()
        assert module.take_shots(8) == "I am invincible!"
    def test_take_shots_9(self):
        module.take_shots_reset()
        assert module.take_shots(9) == "I am invincible!"
    def test_take_shots_10(self):
        module.take_shots_reset()
        assert module.take_shots(10) == "You are wasted! Go home!"
    def test_take_shots_100(self):
        module.take_shots_reset()
        assert module.take_shots(100) == "You are wasted! Go home!"
    
    # Test for the function take_shots with a binge
    def test_take_shots_binge(self):
        module.take_shots_reset()
        assert module.take_shots(1) == "You feel great!"
        assert module.take_shots(2) == "You feel tipsy!"
        assert module.take_shots(1) == "You feel drunk!"
        assert module.take_shots(2) == "Get me some car keys and let's go for a drive!"
        assert module.take_shots(3) == "I am invincible!"
        assert module.take_shots(6) == "You are wasted! Go home!"

    def test_get_commentary_invalid(self):
        assert module.get_commentary('invalid') == "I can only commentate on 'hit', 'stand', or 'bust' actions."

    def test_get_commentary_hit_normal(self):
        module.take_shots_reset()
        commentary = module.get_commentary('hit')
        assert commentary in [
            "Taking a chance, I see!",
            "Not satisfied yet?",
            "Feeling lucky?", 
            "Brace yourself for another card!",
        ]
    
    def test_get_commentary_hit_drunk(self):
        module.take_shots_reset()
        module.take_shots(5)
        commentary = module.get_commentary('hit')
        assert commentary in [
            "This is DEFINITELY a good idea!",
            "There's no way this can backfire!",
            "You NEED another card! And maybe another drink!",
        ]

    def test_get_commentary_stand_normal(self):
        module.take_shots_reset()
        commentary = module.get_commentary('stand')
        assert commentary in [
            "Playing it safe, I like it.",
            "Happy with what you have?", 
            "A wise choice, perhaps?", 
            "Let's see what the dealer has...",
        ]

    def test_get_commentary_stand_drunk(self):
        module.take_shots_reset()
        module.take_shots(5)
        commentary = module.get_commentary('stand')
        assert commentary in [
           "But what if you got another card anyway...?",
            "Aww, but what if your total could be higher?",
            "You're SO confident that you'll win with this hand!"
        ]

    def test_get_commentary_bust(self):
        commentary = module.get_commentary('bust')
        assert commentary in [
            "Ouch! That's a bust!", 
            "Over 21, better luck next time.", 
            "You flew too close to the sun.",
            "Unlucky! The dealer takes it!"
        ]
