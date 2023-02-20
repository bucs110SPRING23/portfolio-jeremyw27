import random
rand = random.randrange(1,11)
guess = int(input("Guess the number: "))
print(guess)

if guess == rand:
   print("correct! the number is ", rand)
else:
    for i in [2,1]:
      if guess > rand:
        print("Too high")
        guess = int(input(str(i) + " more guesses: "))
      elif guess < rand:
        print("Too low")
        guess = int(input(str(i) + " more guesses: "))
      elif guess == rand:
        print("correct!")
    if guess != rand:
        print("incorrect!")
    elif guess == rand:
        print("correct!")
    print("The number is ", rand)