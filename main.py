import random
import time
print("Hi! Welcome to the guessing game. Please guess a number between 1 to 100.")
guess = int(input("what is your guess: "))
correct_number = random.randint(1,100)
guess_count = 0
time.sleep(2)

while guess != correct_number:  
  guess_count += 1
  if guess < correct_number:
    guess = int(input(f"Wrong! You need to guess lower. What is your guess?: "))
  else:
    guess = int(input("Wrong! You need to guess higher. What is your guess?: "))

print(f"You got the right answer. The correct answer was {correct_number}. It took you to {guess_count} guesses")
