def Frequency(st):
    freq = {}
    for i in st:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

st = input("Enter phrase: ")
wrd_freq = Frequency(st)

for char,freq in wrd_freq.items():
    print(f"{char}: {freq}")
