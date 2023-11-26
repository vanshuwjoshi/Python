import random
import math

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

if lower_bound >= upper_bound:
    print("Please enter valid bounds")
    exit()

random_number = random.randint(lower_bound, upper_bound)

iterations = round(math.log(upper_bound - lower_bound + 1, 2))

print("You have ",iterations, " number of chances to guess the number.")

guesses = 0

while guesses < iterations:
    guesses += 1
    guess = int(input("Take a guess: "))

    if random_number == guess:
        print("Congratulations! You did it in ", guesses, " tries.")
        guesses -= 1
        break
    elif random_number > guess:
        print("Think higher!")
    elif random_number < guess:
        print("Think smaller!")

if guesses >= iterations:
    print("The number is ", random_number)
    print("Better luck next time")
