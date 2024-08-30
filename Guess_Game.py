import random

correct = random.randint(1, 100)
print("GUESS GAME (1-100)")
while True:
    n = int(input("Enter a number between 1 and 100: "))

    if n < 1 or n > 100:
        print("Out of range. Try again.")
    elif n == correct:
        print("Correct guess. You won!")
        break
    elif abs(n - correct) >= 10:
        print("Too far. Try again.")
    elif abs(n - correct) < 10:
        print("Too close. Try again.")
    else:
        print("Invalid Input. Try again.")
