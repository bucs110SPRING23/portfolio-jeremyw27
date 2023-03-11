import random
rand = random.randrange(1,1001)
guess = int(input("Guess a number between 1 and 1000: "))
tries = 1
print(guess)

while guess != rand:
    if guess > rand:
        print("Too high")
        guess = int(input("Keep guessing!: "))
        tries += 1
    elif guess < rand:
        print("Too low")
        guess = int(input("Keep guessing!: "))
        tries += 1

if guess == rand:
    print("correct! the number is ", rand)
    print("you took ", tries, " tries to guess the number")