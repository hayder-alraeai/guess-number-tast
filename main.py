win_number = 9


def play():
    print("Welcome to our game. you need to guess the secret number")
    while True:
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


play()
