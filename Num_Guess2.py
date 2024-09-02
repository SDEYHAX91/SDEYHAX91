from random import randint

target = randint(1,100)
print("          NUMBER GUESS GAME\n      ENTER ANY NO. BETWEEN 1 AND 100 ONLY\n")

while True:
    n = int(input("Enter the correct number: "))    

    if n > 100 or n < 0:
        print("Invalid. Try again.")
    else:
        if n > target:
            print("\nLower number please.\n")
        elif n < target:
            print("\nHigher number please.\n")
        elif n == target:
            print("Congrats! You have guessed the correct number.\nEnjoy")
            break
