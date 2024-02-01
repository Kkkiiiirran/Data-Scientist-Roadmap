a = [4, 6, 2, 5, 7, 9, 1, 3]

def qs(a, left, right):
    if left < right:
        mid_Index = mid(a, left, right)
        qs(a, left, mid_Index-1)
        qs(a, mid_Index+1, right)
    else: return

    
def mid(a, left, right):
    pivot = a[left]
    i= left
    j=right
    while i<j:
        while a[i] <= pivot and i<=right-1:
            i+=1
        while a[j]> pivot and j>=left+1:
            j-=1
        if i<j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

    shaam = a[j]
    a[j] = a[left]
    a[left] = shaam
    return j

qs(a, 0, len(a)-1)
print(a)