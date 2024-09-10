n = int(input("Enter a number: "))
sum = i = 0
print(f"Sum of digits in {n} : ",end = "")
while n != 0:
    sum += n % 10
    n //= 10
    i += 1
print(sum)
