"""
        *  
       *** 
      ***** 
     ******* 
    *********
"""
i = 0

for i in range(5):
    for k in range(5-i):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    for k in range(5-i):
        print(" ", end="")
    print(end="\n")
