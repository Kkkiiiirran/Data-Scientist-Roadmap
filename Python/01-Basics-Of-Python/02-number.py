# Q1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

h = 92
w = 48.8 

area = h*w

print(round(area))


# Q2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back

packets = 9
cost = 1.49
given = 20

change = given - (9*1.49)

print(change)

# Q3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python.

length = 5.5
cost = 500
area = 5.5**2

price = area*cost
print(price)

# Print binary representation of number 17 

print(bin(17)) 
print(format(17, 'b'))
# format is a function that takes two arguments, the first is the number to be formatted and the second is the format specifier. In this case, the format specifier is 'b' which means binary.
# what other format specifiers can we use?
# 'o' for octal
# 'x' for hexadecimal
# 'd' for decimal
# 'e' for scientific notation
# 'f' for floating point
# 's' for string
# 'c' for character
# 'r' for repr string
