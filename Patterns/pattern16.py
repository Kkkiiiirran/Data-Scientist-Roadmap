n = 5
for i in range(1, n+1, +1):
    for j in range(i):
        print(chr(i+64), end="")
    print(end="\n")