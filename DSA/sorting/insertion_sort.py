# a = [55, 44, 43, 32, 31, 25, 11, 10, 9, 5, 3, 2, 1]
a = [1, 2, 3, 4, 5]
cnt = 0
for i in range(len(a)):
    small = i
    flag = False
    for j in range(i, len(a), +1):
        cnt+=1
        if a[small] > a[j]:
            flag = True
            small = j
            temp  = a[small]
            while(small>i):
                a[small] = a[small-1]
                small-=1
            a[small] = temp
    if flag == False:
        break

print(cnt)
print(a)