import random

number = random.randint(1, 100)
attempt = 10

def check_attempts():
     global attempt
     attempt -= 1
     print(f"{attempt} attempt/s remaining")

print("Number guessing game")
print(f"You have {attempt} attempts")

guess = int(input("Guess the number: "))

while guess != number and attempt > 1:
 if guess > number:
     print("Too high!", end=" ")
     check_attempts()
     guess = int(input("Guess the number: "))
 else:
     print("Too Low!", end=" ")
     check_attempts()
     guess = int(input("Guess the number: "))

if guess == number:
	print("Correct, You win!")
else:
	print("Out of attempts, You lose")
