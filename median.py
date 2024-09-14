def median(lst):
    t = len(lst)
    if t % 2 != 0:
        return lst[(t-1)//2]
    else:
        med = (lst[(t-1)//2] + lst[t//2])/2
        return med
    
lst = [1,2,3,4,5,6,8,9]
print("Median = ",median(lst))
