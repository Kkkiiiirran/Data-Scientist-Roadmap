"""
*********  0
 *******   1
  *****    2
   ***     3
    *      4

"""

a = 5

for i in range(5, 0, -1):
    for k in range(5-i): #5-5 0
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    for k in range(5-i):
        print(" ", end="")
    print(end="\n")

# rows = 5

# for i in range(5, 0, -1):
#     # Print spaces
#     for j in range(5-i):
#         print(" ", end="")

#     # Print asterisks
#     for k in range(2 * i - 1):
#         print("*", end="")
    
#     for j in range(5-i):
#         print(" ", end="")

#     # Move to the next line after each row
#     print()



