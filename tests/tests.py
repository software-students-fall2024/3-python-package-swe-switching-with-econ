import pytest
from blackjack import module


class Tests:

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
        assert module.take_shots(4) == "You feel tipsy!"
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
