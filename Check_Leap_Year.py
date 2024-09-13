def check_Leap_Year(year):
    if (year % 400 == 0 and year % 100 ==0) and (year % 4 == 0 and year % 100 != 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

print("Leap Year Checker\n\n")    
year = int(input("Enter year: "))
print(check_Leap_Year(year))

''' A YEAR IS A LEAP YEAR IF
1. IT IS DIVISIBLE BY 4, AND
2. IT IS DIVISIBLE BY 400 IF AND ONLY IF IT IS DIVISBLE BY 100 , i.e A FOR A CENTURY'''
