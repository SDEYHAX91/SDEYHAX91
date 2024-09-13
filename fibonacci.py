def fibb(n):
    fibb_series = [0,1]
    if n <= 0:
        return None
    elif n == 1:
        return fibb_series[0]
    elif n == 2:
        return fibb_series
    
    for i in range(1,n):
        nxt_val = fibb_series[i] + fibb_series[i-1]
        fibb_series.append(nxt_val)
    return fibb_series

n = int(input("Enter no. of terms = "))
fibonacci = fibb(n)
print(f"\nFibonacci series upto {n}th terms is :")
for i in fibonacci:
    print(i, end = "  ")
    
