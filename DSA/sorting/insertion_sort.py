a = [1, 2, 54, 23, 1, 7, 5]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]

b = [5, 6, 4, 1, 2]
cnt = 0
for i in range(len(a)):
    small = i
    for j in range(i, len(a), +1):
        cnt+=1
        if a[small] > a[j]:
            small = j
            temp  = a[small]
            while(small>i):
                a[small] = a[small-1]
                small-=1
            a[small] = temp

print(cnt)
print(a)