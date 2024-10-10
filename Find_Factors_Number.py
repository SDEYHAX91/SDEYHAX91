def FindFactors(n):
    factor_list = []
    for i in range(1,n+1):
        if n % i == 0:
            factor_list.append(i)
    for j in factor_list:
        print(j,end='  ')
            
n = int(input("Enter a number: "))
print(f"Factors of {n} : ")
FindFactors(n)

