n = 5
for i in range(n):
    for j in range(n, i, -1):
        print("*", end="")
    for k in range(i*2):
        print(" ", end="")
    for j in range(n, i, -1):
        print("*", end="")
    print(end="\n")

for i in range(n, 0, -1):
    for j in range(n-i+1):
            print("*", end="")
    for k in range((i-1)*2):
        print(" ", end="")
    for j in range(n-i+1):
        print("*", end="")
    print(end="\n")
    
    