n = 26

for i in range(n, 0, -1):
    for j in range(i):
        print(" ", end="")
    for k in range(0, n-i+1, +1):
        print(chr(k+65), end="")
    for k in range(n-i, 0, -1):
        print(chr(k+64), end="")
    for j in range(i):
        print(" ", end="")
    print(end="\n")

