#ROCK PAPER SCISSOR CUT
import random

def Rock_Paper_Scissor_Cut():
    print('''PRESS 
1 FOR ROCK
2 FOR PAPER
3 FOR SCISSOR''')
    
    mac = random.randint(1,3)
    usr = int(input("Enter choice(1/2/3): "))
    choice = {1:"Rock", 2:"Paper", 3:"Scissor"}
    
    if usr in choice:
        print(f"Machine chose {choice[mac]}, you chose {choice[usr]}")
    
    if mac == usr:
        print("Draw")
    else:
        if (mac == 1 and usr == 2) or (mac == 2 and usr == 3) or (mac == 3 and usr == 1):
            print("You Win")
        elif (mac == 1 and usr == 3) or (mac == 2 and usr == 1) or (mac == 3 and usr == 2):
            print("You Lose")
        else:
            print("Invalid choice. Try again")
            Rock_Paper_Scissor_Cut()

Rock_Paper_Scissor_Cut()

