def printTillCount(count):
    if count == 0:
        print(end="\n")
        return
    print(count, end=" ")
    count-=1
    printTillCount(count)

printTillCount(5)

def printForward(count):
    if count == 1:
        return
    count-=1
    printForward(count)
    print(count, end=" ")

printForward(6)

def SumOfNDigitis(n, sum):
    if n==0:
        return sum
    
    return SumOfNDigitis(n-1, sum+n)

print(SumOfNDigitis(10, 0))

