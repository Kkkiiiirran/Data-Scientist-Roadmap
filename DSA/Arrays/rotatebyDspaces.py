a = [1, 2, 3, 4, 5, 6]

d = 2

n = len(a)

d = d%n

a[:] = a[-d:] + a[:-d]
# a[-d] = from the last d elements to the end
# a[:-d] = from the 0 to the last n-d elements
print(a)

# a[:] means that we are changing the original array and not creating a new one
# a[-d:] means that we are taking the last d elements of the array
# a[:-d] means that we are taking the first n-d elements of the array

# a[-d:] refers to 4, 5, 6 if d = 3
# a[:-d] refers to 1, 2, 3 if d = 3

# why -d? because we are rotating the array to the left by d spaces

# a[-d:] + a[:-d] means that we are concatenating the last d elements with the first n-d elements

# how would you rotate the array to the right by d spaces? by reversing the array and then reversing the first d elements and then reversing the last n-d elements
# how? 

# reverse the array to right rotate by d spaces

b = [1, 2, 3, 4, 5, 6]
# b = [3, 4, 5, 6, 1, 2] if d = 2

d = 2
n = len(b)
# b[:d] = [1, 2]
# b[d:] = [3, 4, 5, 6]
b[:] = b[d:] + b[:d]

print(b)

# why does roatting by left and right same?


