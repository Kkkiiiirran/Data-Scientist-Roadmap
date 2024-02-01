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