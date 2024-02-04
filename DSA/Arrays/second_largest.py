a = [23, 4, 45, 65,12, 78,24]
maxi =a[0]
s_maxi = a[0]

for i in range(len(a)):
    if a[i] > maxi:
        s_maxi = maxi
        maxi = a[i]
    elif a[i] > s_maxi and a[i] != maxi:
        s_maxi = a[i]

print(s_maxi)