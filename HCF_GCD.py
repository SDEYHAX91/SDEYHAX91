def hcf(x , y):
    while (y != 0):
        x , y = y , x %y
    return x

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print(f"HCF/GCD of {a} & {b} = {hcf(a,b)}")
