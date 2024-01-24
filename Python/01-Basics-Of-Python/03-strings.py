# Q1. Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line

street = "1234"
city = "Vancouver"
country = "Canada"

address = street + "\n" + city + "\n"  + country

address2 = f"{street}\n{city}\n{address}"

print(address)
print(address2)

# Q2. Create a variable to store the string "Earth revolves around the sun" and using slice operation print "revolves around the sun"

string = "Earth revolves around the sun"

sliced_string = string[6:14]
print(sliced_string)

last_word = string[-3:]
print(last_word)

# Q3. Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

x = 5
y = 10

print(f" I eat {x} veggiest and {y} fruits daily")
print("I eat " + str(x) + " veggis and " + str(y) + " fruits daily.") 

# Q4. I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

s = "maine 200 and banana khaye"
print(s.replace("200", "10").replace("banana", "samosa"))


