n = 5

for stars in range(n+1):
    for star in range(stars):
        print("*", end="")
    print(end="\n")

for stars in range(n-1, 0, -1):
    for star in range(stars):
        print("*", end ="")
    print(end="\n")
