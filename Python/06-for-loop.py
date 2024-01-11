# Q1. After flipping a coin 10 times you got this result,

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

heads = 0;

for i in result:
    if i == "heads":
        heads += 1

print(heads)


for i in range(11):
    if i % 2 != 0:
        print(i**2)

expense_list = [2340, 2500, 2100, 3100, 2980]

months = ["Jan", "Feb", "Mar", "Apr", "May"]

expense = int(input("Enter an expense: "))
expense_found = False;
for i in range(len(expense_list)):
    if expense_list[i] == expense:
        print(f"You spent {expense} in {months[i]} month.")
        expense_found = True;
        break

if not expense_found:
    print("Expense not found")

race_completed = True
for i in range(5):
    tired = input("Are you tired?")
    if tired == "yes":
        print("you didn't finish the race")
        race_completed = False
        break
    else:
        print(f"{4-i} laps remaining")
if race_completed:
    print("Congratulations! You finished your race")


for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print(end="\n")

