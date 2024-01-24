import random

level = input("easy, medium or hard?")

if level == "easy":
    attempts = 10
elif level == "medium":
    attempts = 7
elif level == "hard":
    attempts = 5

number = random.randint(1, 100)

guess = int(input("Guess a number"))
isGame = True

def check(num):
    global attempts
    global isGame
    if guess == num:
        print(f"the number was {num}, you won")
        isGame = False
    elif guess < num:
        print("too low")
        attempts-=1
    else:
        print("too high")
        attempts-=1

    if (attempts == 0):
        print("You lose")
        isGame = False
    
    print(attempts)


while isGame:
    check(num= number)
    guess = int(input("Guess a number "))

# while (guess != number):
