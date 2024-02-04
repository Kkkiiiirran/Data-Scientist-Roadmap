a = [5, 6, 7, 1, 2, 3, 4]
cnt = 0
for i in range(len(a)-1):
    if a[i]> a[i+1]:
        cnt+=1

if a[0] < a[-1]:
    cnt+=1

if cnt >1:
    print("Not sorted")

else:
    print("Sorted")

