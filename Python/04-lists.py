expense_every_month = [
    ["January", "February", "March", "April", "May"],
    [2200, 2350, 2600, 2130, 2190],
]

#  1. In Feb, how many dollars you spent extra compare to January?

ans1 = expense_every_month[1][1] - expense_every_month[1][0]
print(ans1)

# 2. Find out your total expense in first quarter (first three months) of the year.
expense_list = expense_every_month[1]
quaterly_expense = expense_list[0] + expense_list[1] + expense_list[2]
print(quaterly_expense)

# 3. Find out if you spent exactly 2000 dollars in any month  

print(2000 in expense_list)
# use contains method - https://www.w3schools.com/python/ref_list_contains.asp


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense_every_month[0].append("June")
expense_every_month[1].append(1980)

print(expense_every_month)

# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expense_every_month[1][3] = expense_every_month[1][3] - 200

print(expense_every_month)


# Q2. You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

# length of the list

print(len(heros))

# Add 'black panther' at the end of this list
heros.append("black panther")

print(heros)

# You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'

heros.remove("black panther")
heros.insert(3, "black panther")

print(heros)

# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

print(dir(heros))
heros.sort()
print(heros)
# __add__ - concatenates two lists
l1 = [1,2,3]
l2 = [4,5,6]
# use __add__ to concatenate l1 and l2
l3 = l1.__add__(l2) # cant we use it like add(l1, l2) ? # no, because add is a method of list class
# why can we use dir() like this and not add()? # because dir() is a built-in function, whereas add() is a method of list class
print(l3)

# what other built-in functions are there for lists? # https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

