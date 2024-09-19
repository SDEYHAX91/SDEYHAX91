def isPrime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,int((n**0.5)+1)):
            if n%i==0:
                return False
        return True   
        
x = int(input("Enter a number = "))
if isPrime(x)==True:
    print("It is a prime number.")
else:    
    print("It is not a prime number.")             