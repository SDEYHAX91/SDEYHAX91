def lcm(x, y, z):
    m = max(x, y, z)
    
    while True:
        if m % x == 0 and m % y == 0 and m % z == 0:
            return m
        m += 1

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

print(f"LCM of {a}, {b}, and {c} = {lcm(a, b, c)}")
