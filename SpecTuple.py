def t_replace(tup, index, element):  # Replaces tuple element at specified index with specified element and returns updated tuple
    if index < 0 or index >= len(tup):
        raise IndexError("Index out of range")
    # Replace the element at the specified index
    tup = tup[:index] + (element,) + tup[index+1:]
    return tup


def uniq_tuple(tup): #Returns updated tuple with no duplicate elements
    tup1 = ()
    for i in tup:
        if i not in tup1:
            tup1 += (i,)
    return tup1


def t_pop(tup,index): #removes tuple element from specified index and returns updated tuple
    if index < 0 or index >= len(tup):
        raise IndexError
    else:
        for i in range(len(tup)):
            if i == index:
                tup = tup[:i] + tup[i+1:]
                break
        return tup
    

def t_remove(tup, element):  # Removes the first occurrence of the element in the tuple and returns the updated tuple
    if element not in tup:
        raise ValueError(f"{element} not found in tuple")
    for i in range(len(tup)):
        if tup[i] == element:
            tup = tup[:i] + tup[i+1:]
            break
    return tup


def t_insert(tup,index,element): #Insert specified element at specified index in a tuple and returns updated tuple
                                #It can also insert any iterables
    if index < 0 or index > len(tup):
        raise IndexError
    else:
        for i in range(len(tup)):
            if index == i:
                tup = tup[:i] + (element,) +tup[i:]
                break
    return tup

