n = 6
for i in range(n):
    for j in range(i+1):
        print(j+1, end="")

    for k in range(((n*2) - (2*i))-2):
        print(" ", end="")

    for j in range(i+1, 0, -1):
        print(j, end="")
    print(end="\n")
        