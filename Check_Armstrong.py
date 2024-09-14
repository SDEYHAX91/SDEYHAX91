def isArmstrong(num):
    ct_digit = i = 0
    digits = []

    while num != 0:
        digits.append(num % 10)
        ct_digit += 1
        num = num // 10
        i += 1
    
    cubicSum = 0
    for x in digits:
        cubicSum += x ** ct_digit

    if cubicSum == n:
        return "\nArmstrong number."
    return "\nNot an Armstrong Number."

n = int(input("Enter a number: "))
print(isArmstrong(n))

    
