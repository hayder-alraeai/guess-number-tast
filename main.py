win_number = 9
amount_guesses = 5


def play():
    guess_counter = 0

    print("Welcome to our game. you need to guess the secret number")
    while True:
        if guess_counter > 0 and not guess_counter == amount_guesses:
            print(f"You have {amount_guesses - guess_counter} try left!")
        elif guess_counter == amount_guesses:
            lose = input(
                f"You have used all your available try {amount_guesses} Type any key to try again or 'q' to quit"
            )
            if lose.lower() == "q":
                break
            else:
                guess_counter = 0
        guessed_number = input("Enter a number: press 'q' to quit the game!")
        if not guessed_number.isdigit() and guessed_number.lower() == "q":
            break
        if win_number > int(guessed_number):
            print("The number you entered is less than the secret number")
        elif win_number < int(guessed_number):
            print("The number you entered is more than the secret number")
        else:
            win = input("you win! Type any key to continue or 'q' to quit")
            if win.lower() == "q":
                break
        guess_counter = guess_counter + 1


play()
