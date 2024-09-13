#PROGRAM TO CREATE A BUDGET CALCULATOR THAT CALCULATE INCOME AND EXPENDITURE, TRACKS EXPENSES AND CHECKS SAVINGS
print('EXPENSE TRACKER\n')
income = {}
expenditure = {}

i = 0
print("INCOME")
while(True):
    src = input(f"\n{i+1}. Enter source(Type 'done/Done/DONE' to finish): ")
    if src.lower() == 'done':
        break
    amount_i = int(input("Enter amount of income: "))
    income[src] = amount_i
    i += 1
    
print("\nEXPENDITURE\n")
j = 0
while(True):
    exp_src = input(f"\n{j+1}. Enter source of expenditure(Type 'done/Done/DONE' to finish): ")
    if exp_src.lower() == 'done':
        break
    exp_amount = int(input("Enter amount of expenditure: "))
    expenditure[exp_src] = exp_amount
    j += 1

total_income = sum(income.values())
total_expenditure = sum(expenditure.values())
balance = total_income - total_expenditure

print("\nTotal income = ",total_income)
print("\nTotal expenditure = ",total_expenditure)
print("\nBalance = ",balance)

if balance > 0:
    print("You are on budget.")
elif balance == 0:
    print("Caution: No savings.")
else:
    print("Warning: You are over budget.")
