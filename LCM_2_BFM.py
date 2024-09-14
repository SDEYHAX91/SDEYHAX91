def lcm(x,y):
    m = min(x,y)
    while True:
        if m % x == 0 and m % y == 0:
            return m
        m += 1
    return 1

a = int(input("Enter no. 1 = "))
b = int(input("Enter no. 2 = "))
print(f"LCM of {a} and {b} = {lcm(a,b)}")
