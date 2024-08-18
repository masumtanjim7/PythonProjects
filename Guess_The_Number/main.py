import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")

count = 0
flag = False

while count < total_chances:
    count += 1
    guess = int(input("Guess a number:- "))

    # Condition
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        flag = True
        break                   # Once guessed, loop will break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")

# Better to use This source Code on pycharm!
