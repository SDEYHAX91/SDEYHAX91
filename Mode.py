def mode(lst):
    freq = {}
    for i in lst:
        # Increment frequency of each element
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    # Find the maximum frequency value
    maxval = max(freq.values())
    
    # Find and return the element with the maximum frequency
    for i in freq:
        if freq[i] == maxval:
            return i
    return None

# Example usage
lst = [1, 6, 6, 7, 3, 6, 3, 7, 4, 2]
print("Mode =", mode(lst))
