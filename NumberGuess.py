import math

number_max = 100
number_guesses = 0
guess_min = 0
guess_max = number_max / 2

print("Think of a number between 1 and 100. Press any key to begin.")
input()

while guess_min != number_max:
    response = input("Is your number between " + str(guess_min) + " and " + str(int(guess_max)) + "? (y/n): ")

    if len(response) != 0 and response[0].lower() == 'y':
        number_guesses += 1
        print("You answered Yes!")
        number_max = math.ceil(guess_max)
        guess_max = math.ceil(guess_max - (guess_max - guess_min) / 2)

    elif len(response) != 0 and response[0].lower() == 'n':
        number_guesses += 1
        print("You answered no!")
        guess_min = math.ceil(guess_max + 1)
        remaining_difference = int(number_max) - int(guess_max)
        guess_max += math.ceil(remaining_difference / 2.0)

    else:
        print("Invalid Answer. Please enter y or n.")
        continue

    # if there are only two numbers left, guess one.
    if (math.ceil(guess_min) + 1) == math.ceil(number_max):
        number_guesses += 1

        # ask if it's the lower number
        response = input("Is your number " + str(guess_min) + "? ")
        if len(response) != 0 and response[0].lower() == 'y':
            break
        else:
            guess_min = math.ceil(number_max)


print("Your number is " + str(int(guess_min)) + "!")
print("It took " + str(number_guesses) + " guesses to guess your number.\n")
input("Press enter to close.")
