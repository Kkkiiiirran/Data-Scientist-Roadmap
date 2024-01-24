n=5
for i in range(1, n+1, +1):
    for j in range(i):
        print(chr(j+n-i+65), end=" ")
    print(end="\n")

for i in range(1, n+1, +1):
    for j in range(n-i, n, +1):
        print(chr(j+65), end=" ")
    print(end="\n")