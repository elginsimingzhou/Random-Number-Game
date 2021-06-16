
from art import logo
import random

print(logo)

is_playing = True
easy_attempts = 10
hard_attempts = 5

def check_guess(guess_no, random_no, attempts):
  global is_playing

  if guess_no> random_no:
    print("Too high")
    attempts-=1
      
  elif guess_no<random_no:
    print("Too low")
    attempts -=1
      
  else:
    print("You are right!")
    is_playing = False
  
  return attempts


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
choice=input("Choose a difficulty. Type 'easy' or 'hard': ")

random_number = random.randint(1,100)


if choice == 'easy':
  while is_playing:
    if easy_attempts>0:
      print(f"You have {easy_attempts} attempts remaining to guess the number.")
      guess= int(input("Make a guess: "))
      easy_attempts = check_guess(guess, random_number, easy_attempts)
      if easy_attempts>0:
        print("Guess again")


    else:
      print("You ran out of guesses")
      is_playing = False
    
      
  
else:
  while is_playing:
    if hard_attempts>0:
      print(f"You have {hard_attempts} attempts remaining to guess the number.")
      guess= int(input("Make a guess: "))
      hard_attempts = check_guess(guess, random_number, hard_attempts)

      if hard_attempts>0:
        print("Guess again")

    else:
      print("You ran out of guesses")
      is_playing = False
