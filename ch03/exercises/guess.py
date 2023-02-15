import random
rand = random.randrange(1,11)
guess = int(input("Guess the number: "))

if guess == rand:
   print("correct! the number is ", rand)
else:
    for i in [2,1]:
      if guess > rand:
        print("Too high")
        guess = input(i, " more guesses:")
      elif guess < rand:
        print("Too low")
        guess = input(i, " more guesses:")
      else:
        print("correct!")
    print("The number is ", rand)