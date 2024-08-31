# LCM OF 2 NUMBERS USING BRUTE FORCE METHOD
print("LCM AI")
def lcm(x,y):
    for i in range(1, x * y):
        for j in range(1, x * y):
            if x * i == y * j:
                return x*i
    return 1

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print(f"LCM of {a} & {b} = {lcm(a,b)}")
