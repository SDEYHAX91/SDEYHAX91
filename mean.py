def findMean(lst):
    sum = 0
    for i in lst:
        sum += i
    avg = sum / len(lst)
    return avg

n = int(input("Enter no. of values = "))    
lst = [float(input(f"{i+1}. Enter no. = "))for i in range(n)]
print("Mean = ",findMean(lst))
