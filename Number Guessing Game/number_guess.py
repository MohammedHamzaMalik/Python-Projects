import random
import math

# Give your input for starting and ending number for your guessing range
start = int(input('Enter the starting number: '))
end = int(input('Enter the ending number: '))

rnd = random.randint(start, end)
print("You have ", round(math.log(end - start + 1, 2)), " chances for guessing the number\n")

count = 0

while count < math.log(end - start + 1, 2):
    count += 1

    guess = int(input("Guess your lucky number : "))

    if guess == rnd:
        print("Congratulations, you guessed the number in just ", count, " try")
    elif rnd > guess:
        print("You guessed a small number, in ", count, " try")
    elif rnd < guess:
        print("You guesses a large number in ", count, " try")

    if count >= math.log(end - start + 1, 2):
        print("\nThe number is %d" % rnd)
        print("Try out next time, with some great amount of luck")
        
 #Source: https://www.geeksforgeeks.org/number-guessing-game-in-python/
