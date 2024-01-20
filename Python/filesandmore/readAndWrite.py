# file = open("Python/filesandmore/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("Python/filesandmore/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # writing to a file
    
with open("Python/filesandmore/my_file.txt", mode="w") as file:
    file.write("I\n.\n.\n\n.\n\n.\n\n.\n\n.\n\n.\n\n.\n\n.\n.\n.\n\n.\n\n.\n\n.\n.\n.\n.\n.\n.\n.\n.")

# appending a files content
    
with open("Python/filesandmore/my_file.txt", mode="a") as file:
    file.write("LOVE\n\n.\n.\n\n.\n\n.\n\n.\n\n.\n\n.\n\n.\n\n.\n.\n.\n\n.\n\n.\n\n.\n.\n.\n.\n.\n.\n.\n.Everything About You!!")

# creating a new file
    
with open("Python/filesandmore/new_file.txt", mode="w") as file:
    file.write("\nI have a confession....\n.\n.\n\n.\n\n.\n\n.\n\n.\n\n.\n\n.\n\n.\n.\n.\n\n.\n\n.\n\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n\n.\n.\n\n.\n\n.\n\n.\n\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.I'll tell you tomorrow")
