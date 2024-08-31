def unique_list(lst):
    uniq = []
    for i in lst:
        if i not in uniq:
            uniq.append(i)
    print("List without duplicate values = ",uniq)

n = int(input("Enter size: "))
lst = [int(input(f"Enter for element {x+1} = ")) for x in range(n)]
print("Original list = ",lst)
unique_list(lst)
