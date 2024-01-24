###
    # 3 3 3 3 3 
    # 3 2 2 2 3 
    # 3 2 1 2 3 
    # 3 2 2 2 3 
    # 3 3 3 3 3
###
# how to print this pattern?

n = 3
for i in range(2*n-1):
    for j in range(2*n-1):
         top = i;
         bottom = j;
         right = (2*n - 2) - j;
         left = (2*n - 2) - i;
         k = n- min(min(top,bottom), min(left,right))
         print(k, end=" ")
    print(end="\n")