# Q1. Write a program that asks user to enter a city name and it should tell which country the city belongs to


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = (input("Enter a city name: ")).lower()

if city in india:
    print(f"{city} in India")
elif city in pakistan:
    print(f"{city} in Pakistan")
elif city in bangladesh:
    print(f"{city} in Bangladesh")
else:
    print(f"{city} not in India, Pakistan or Bangladesh")

# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
    
city1 = input("Enter a city name: ").lower()
city2 = input("Enter another city name: ").lower()

if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in Pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")


# Q2. Write a python program that can tell you if your sugar is normal or not. Normal blood sugar range is 80 - 120.

sugar_level = int(input("Enter your sugar level: "))

if sugar_level < 80:
    print("Low sugar level")
elif sugar_level > 100:
    print("High sugar level")
else:
    print("Normal sugar level")

