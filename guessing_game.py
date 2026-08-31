import random

number = random.randint(1, 100)

print("Number guessing game")
guess = int(input("Guess the number: "))

while guess != number:
 if guess > number:
     print("Too high!")
     guess = int(input("Guess the number: "))
 else:
     print("Too low!")
     guess = int(input("Guess the number: "))

print("Correct, You win!")

