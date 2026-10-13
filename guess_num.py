n = 1
from secret_number import secretNum
guess = int(input("Guess a number : "))
while guess != secretNum:
    if guess <= secretNum:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Guess a number : "))
    n = 1 + n
    if n == 5:
        break
if guess == secretNum:
    print("Congratulations! You guessed the number.")
while n == 5:
    print("Oh!Noooooo")