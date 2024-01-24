alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# test = "ball".lower()
# print(test)
for i in text:
    if i == " ":
        print(" ", end="")
        continue
    index = alphabet.index(i)
    if direction == "encode":
        index+= shift

    else :
        index-= shift

    if index > 26:
        index = (index - 26)
    elif index < 0:
        index = 26 + index
    
    
    print(alphabet[index], end="") 



