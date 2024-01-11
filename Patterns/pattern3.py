"""
    1
    12
    123
    1234
    12345
"""

for i in range(6):
    for j in range(i):
        print(j+1, end="")
    print(end="\n")