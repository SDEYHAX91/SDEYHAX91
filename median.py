def median(lst):
    c = len(lst)
    if c % 2 == 0:
        med = (lst[c//2] + lst[(c//2)-1])/2
    elif c % 2 != 0:
        med = lst[c//2]
    else:
        return None
    if med == int(med):
        return int(med)
    return med
    
    
n = int(input("Enter size: "))
lst = []
for i in range(n):
    el = float(input(f"{i+1}. Enter value =  "))
    lst.append(el)
print("Median = ",median(lst))    
