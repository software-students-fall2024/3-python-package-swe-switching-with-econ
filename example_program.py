from drunkblackjack import module

def main():

    # Function 1: Start game
    # Start a game normally, while sober, and bet $100
    module.start_game(100)

    # Function 2: Take shots
    # Take a 5 shots and become drunk
    print("Taking 5 shots: ")
    print(module.take_shots(5))

    # Play a game while drunk, and bet $100
    module.start_game(100)

    # Function 3: Get commentary (while drunk)
    print("Your 'hit' commentary: ")
    print(module.get_commentary('hit'))
    print("Your 'stand' commentary: ")
    print(module.get_commentary('stand'))
    print("Your 'bust' commentary: ")
    print(module.get_commentary('bust'))

    # Function 4: Get advice
    # Get good advice
    good_advice = module.get_advice('good')
    print("Your 'good' advice: ")
    print(good_advice)
    # Get bad advice
    bad_advice = module.get_advice('bad')
    print("Your 'bad' advice: ")
    print(bad_advice)


if __name__ == "__main__":
    main()