print("FUNCTION / PROGRAM TO REMOVE A SPECIFIED TUPLE ELEMENT")

def remove_tup_val(tup): 
    rem = int(input("Enter element to be removed: "))
    
    if rem in tup:
        index = tup.index(rem)
        tup = tup[:index] + tup[index + 1:]
        print("Updated Tuple:", tup)
    else:
        print("Specified element not found")

n = int(input("Enter size: "))
lst = [int(input(f"Enter element {x+1}: ")) for x in range(n)]
tup = tuple(lst)

remove_tup_val(tup)
