n = 5
for i in range(65+n,65, -1):
    for j in range(65, i, +1):
        print(chr(j), end=" ")
    print(end="\n")
