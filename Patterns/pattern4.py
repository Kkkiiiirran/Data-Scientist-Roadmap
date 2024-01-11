"""
    1
    22
    333
    4444
    5555
"""

for i in range(6):
    for j in range(i):
        print(i, end="")
    print(end="\n")