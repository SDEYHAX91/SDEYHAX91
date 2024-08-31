print("FUNCTION / PROGRAM TO REMOVE TUPLE ELEMENT WITH THE HELP OF INDEX")
def pop_tuple_val(tup,size):
    x = int(input("\nEnter position to delete element: "))
    pos = x - 1

    if pos < 0 or pos >= size:
        print("Invalid. Try again.")
        pop_tuple_val(tup,size)
    
    else:    
        removed = tup[pos]
        tup = tup[:pos] + tup[pos + 1:]
        
        print("\nRemoved element from the tuple = ",removed)
        print("Updated tuple is = ",tup)
    
size = int(input("Enter total no. of tuple elements: "))
lst = [int(input(f"Enter value for element {i+1} = ")) for i in range(size)]
tup = tuple(lst)

pop_tuple_val(tup,size)
