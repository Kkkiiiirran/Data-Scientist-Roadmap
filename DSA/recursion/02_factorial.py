def factorial(n, fact):
    if n==0:
        return fact

    return factorial(n-1, fact*n)

print(factorial(5, 1))

def reverseArray(n, array, li):
    if n<=0:
        return li
    li.append(array[n-1])
    n-=1
    return reverseArray(n, array, li)

print(reverseArray(5, [55, 43, 31, 22, 181], []))


