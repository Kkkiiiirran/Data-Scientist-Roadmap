# Q1. After flipping a coin 10 times you got this result,

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

heads = 0;

for i in result:
    if i == "heads":
        heads += 1

print(heads)

#  Q2. Print square of all numbers between 1 to 10 except even numbers


for i in range(11):
    if i % 2 != 0:
        print(i**2)


#Q3. Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.
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
    
    
# Q4.Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

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


# Q5. Write a program that prints following shape
    # *
    # **
    # ***
    # ****
    # *****


for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print(end="\n")

