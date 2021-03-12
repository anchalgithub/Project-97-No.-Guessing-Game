import random

print("Welcome to the Number Guessing Game.")

number = random.randint(1,9)
chances=0

print("Guess a number from between 1-9! : ")

while chances <5: 
    guess=int(input("Write your guess:"))

    if guess==number:
        print("Awesome! You guessed it!")
        break

    elif guess<number:
        print("Too low. Please guess a number higher than", guess)

    else:
        print("Too high. Please guess a number lower than", guess)

    chances+=1

if not chances <5:
    print("Not quite. The number was", number)