# თამაში 1: გამოიცანით რიცხვი
# პროგრამა აგენერირებს შემთხვევით რიცხვს 1-დან 100-მდე.
# მოთამაშეს აქვს 10, 5 ან 3 ცდა რომ გამოიცნოს რიცხვი.
# არასწორი რიცხვის შემთხვევაში პროგრამა მომხმარებელს აძლევს მინიშნებას (უფრო მაღალი/უფრო დაბალი).
# თამაში აკონტროლებს მცდელობების რაოდენობას
# თამაში აჩვენებს გამოსაცნობ რიცხვს როგორ მოგების ასევე წაგების შემთხვევაში
# მოგების/წაგების შემდეგ პროგრამა მოთამაშეს ეკითხება, უნდა თუ არა თამაშის გაგრძელება.

import random


def guessing_game():

    print("👋 Welcome to the Number Guessing Game! You have to guess number between 1 and 100🎉.")

    while True:
        difficulty = input("\nEasy: 10 tries\nNormal: 5 tries\nHard: 3 tries\n\nChoose a difficulty level: ").lower()
        if difficulty in ["easy", "normal", "hard"]:
            break
        else:
            print("Invalid difficulty level. Please choose from easy, normal, or hard.")

    # Difficulty levels: easy (10 tries), normal (5 tries), hard (3 tries)
    if difficulty == "easy":
        max_tries = 10
    elif difficulty == "normal":
        max_tries = 5
    elif difficulty == "hard":
        max_tries = 3
    else:
        print("Invalid difficulty level. Please choose from easy, normal, or hard.")
        return
    # generate a random number between 1 and 100. player has 10 attempts.
    number_to_guess = random.randint(1, 100)
    print("\n the number to guess is", number_to_guess)
    tries_left = max_tries

    print(f"\n You have {tries_left} tries to guess the number between 1 and 100. 🎉")

    while tries_left > 0:
        guess = input("Enter your guess: ")
        # check if the input is an integer
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter an integer.")
            continue

        # check if the guess is within the range of 1-100
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100. ❌")
            continue
        # if the number is correct, player wins. otherwise they get a hint.
        if guess == number_to_guess:
            print("Congratulations! You guessed the number correctly! 🎉")
            break
        elif guess < number_to_guess:
            print("The number is higher than your guess. ⬆️")
        else:
            print("The number is lower than your guess. ⬇️")

        tries_left -= 1  # the player loses 1 attempt after every guess
        print(f"You have {tries_left} tries left. ⏳ \n")

    if guess != number_to_guess:
        print(f"Sorry, you have run out of tries. The number was {number_to_guess} ❌ \n")


# ask the player if they want to play another round
# the answer should be 'yes' or 'no'.
def continue_game():
    while True:
        play_again = input("Do you want to play another round? Enter Yes or No: \n").lower()
        if not isinstance(play_again, str) or play_again not in ["yes", "no"]:
            print("Please enter YES or NO.")
        elif play_again == "no":
            print("Thank you for playing!")
            return False
        else:
            return True


def main():
    # to continue or end the game depending on the player's input
    while True:

        guessing_game()
        if not continue_game():
            break


if __name__ == "__main__":
    main()
