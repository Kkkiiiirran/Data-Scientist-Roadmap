dictionary = {}
with open("poem.txt") as file:
    for line in file:
        words = line.split(' ')
        for word in words:
            if word in dictionary:
                dictionary[word]+=1
            else:
                dictionary[word] = 1

print(dictionary)

frequency = list(dictionary.values())
max_count = max(frequency)
print(max_count)

for word, count in dictionary.items():
    if count == max_count:
        print(word)
    

