# SIMPLE CALCULATOR

def add(x, y):
    result = x + y
    if result == int(result):
        return int(result)
    else:
        return result

def subtract(x, y):
    result = x - y
    if result == int(result):
        return int(result)
    else:
        return result

def product(x, y):
    result = x * y
    if result == int(result):
        return int(result)
    else:
        return result

def division(x, y):
    if y == 0:
        return "Error"
    else:
        result = x/y
        if result == int(result):
            return int(result)
        else:
            return result 

while True:
    print("ENTER CHOICE FOR CALCULATION")
    print('''1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit''')
    n = int(input("Enter choice (1/2/3/4/5 only): "))

    if n in [1, 2, 3, 4]:
        x = float(input("Enter 1st number: "))
        y = float(input("Enter 2nd number: "))

    if n == 1:
        print(f"\nResult = {add(x, y)}\n")
    elif n == 2:
        subtract(x,y)
    elif n == 3:
        print(f"Result = {product(x, y)}\n")
    elif n == 4:
        print(f"Result = {division(x, y)}\n")
    elif n == 5:
        exit()
        break
    else:
        print("Error! Invalid choice.\n")
