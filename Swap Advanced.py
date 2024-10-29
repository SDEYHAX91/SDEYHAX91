def swap(x,y):
    x = x + y
    y = x - y
    x = x - y

a = 67
b = 34
print(f"Before swapping, a = {a}, b = {b}")
swap(a,b)
print(f"After swapping, a = {a}, b = {b}")
