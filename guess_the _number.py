import random

print("🎮 WELCOME TO THE GUESS THE NUMBER 🎮")
print("=====    Happy Gaming 😊    =====")

while True:
    print("How Difficulty could you choose? 👾")
    print("1️⃣ Easy (1 to 50)")
    print("️2️⃣ Medium (1 to 100)")
    print("3️⃣ Hard (1 to 500)")

    attempts = 0
    score = 100

    difficulty = input("Choose difficulty (1/ 2/ 3): ")

    if difficulty == "1":
        max_num = 50
    elif difficulty == "2":
        max_num = 100
    elif difficulty == "3":
        max_num = 500
    else:
        max_num = 100
        print(f"🎯 I'm thinking of a number from 1 to {max_num}")

    target = random.randint(1, max_num)

    while True:
        userChoice = input("Guess the number or type q to quit: ")
        if userChoice == "q":
            break

        userChoice = int(userChoice)
        attempts += 1

        if userChoice == target:
            print("You guessed right!🎉")
            print(f"You guessed in {attempts}th attempts!❤️")
            print("Score:", score)
            break

        if userChoice != target:
            score -= 5

        if userChoice > target:
            print(f"You guessed too high.📉Take a lower number... You scored {score}")

        else:
            print(f"You guessed too low.📈Take a higher number... You scored {score}")

    playAgain = input("Would you like to play again? ♾️(y/n): ")

    if playAgain == "n":
        print("---- GAME OVER ----")
        break