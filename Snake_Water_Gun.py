import random

def Snake_Water_Gun():
    print('''Press 
1 FOR SNAKE
2 FOR WATER
3 FOR GUN''')
    
    usr = int(input("Enter choice (1/2/3): "))
    
    if usr not in [1, 2, 3]:
        print("Invalid input. Try again")
        Snake_Water_Gun()
        return
    
    mac = random.randint(1, 3)
    choice = {1: "Snake", 2: "Water", 3: "Gun"}
    
    print(f"Machine chose {choice[mac]}, you chose {choice[usr]}")
    
    if usr == mac:
        print("Draw")
    else:
        if (mac == 1 and usr == 2) or (mac == 2 and usr == 3) or (mac == 3 and usr == 1):
            print("You Lose")
        elif (mac == 1 and usr == 3) or (mac == 2 and usr == 1) or (mac == 3 and usr == 2):
            print("You Win")
        else:
            print("Invalid input. Try again")

Snake_Water_Gun()
