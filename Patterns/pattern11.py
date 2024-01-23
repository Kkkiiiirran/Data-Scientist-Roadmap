n = 10

for i in range(n):
    if i%2==0:
          print("1 ", end="")
          for j in range(int(i/2)):
            print("0 1 ", end="")
    else: 
        print(end="\n")
        for j in range(int(i/2+1)):
            print("0 1 ", end="")
        print(end="\n")