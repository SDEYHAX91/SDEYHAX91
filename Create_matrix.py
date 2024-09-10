#PROGRAM TO CREATE A MATRIX OF SPECIFIED ROWS AND COLUMNS WITH USER INPUT ELEMENTS
import numpy as np

print("MATRIX CREATOR\n")
row = int(input("Enter row: "))
column = int(input("Enter column(No. of elements in each row): "))

matrix = []
for i in range(row):
    row = []
    for j in range(column):
        element = float(input(f"Enter value for element [{i+1}][{j+1}] = "))
        row.append(element)
    matrix.append(row)
    
arr_matrix = np.array(matrix)
print("\nMatrix:\n")
for x in arr_matrix:
    for y in x:
        if y == int(y):
            print(int(y),end = "       ")
        else:
            print(y,end = "       ")
    print("\n")
    
