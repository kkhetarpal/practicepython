# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (_Hint: remember to use the user input lessons from the very first exercise
# Extras:

#     Keep the game going until the user types "exit" Keep track of
#     how many guesses the user has taken, and when the game ends,
#     print this out.




import random
number = random.randint(2,6)
guess =0;
count =0;

while guess != number and guess != "exit":
    guess = input("What is your guess")

    if guess =="exit":
         break

    guess = int(guess)
    count += 1

    if guess < number:
        print("Too Low!")
    elif (guess > number):
        print("Too High")
    else:
        print("you got it!")
        print("And it only took you",count,"tries")
