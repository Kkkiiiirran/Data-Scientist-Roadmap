b = [10, 43, 73, 63, 90, 125, 345, 1000, 1200, 2500, 25001]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(a)):
    small = i
    for j in range(i, len(a), +1):
        if a[small] > a[j]:
            small = j

    temp = a[i]
    a[i] = a[small]
    a[small] = temp

cnt = 0
for i in range(len(b)):

    for j in range(len(b)-i-1):
        cnt+=1
        if(b[j]>b[j+1]):
            flag = True
            temp = b[j]
            b[j] = b[j+1]
            b[j+1] = temp


for i in range(len(b)):
    flag = False
    for j in range(len(b)-i-1):
        cnt+=1
        if(b[j]>b[j+1]):
            flag = True
            temp = b[j]
            b[j] = b[j+1]
            b[j+1] = temp
    if flag == False:
        break

print(cnt)
print(b)




        


