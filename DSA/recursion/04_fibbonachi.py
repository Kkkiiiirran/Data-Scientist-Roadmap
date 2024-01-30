def fibb(n, sum):
    if n==0:
        return sum
    
    if n==1:
        return sum+1
    
    return fibb(n-1, sum) + fibb(n-2, sum)

    
print(fibb(4, 0))