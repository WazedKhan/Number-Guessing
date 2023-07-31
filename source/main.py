from assist import chosen_number, count_point

accurate_number = chosen_number()
number_guess = 3
starting_hints = "You'r number is between 0 - 6, You have maximum 3 guesses"

print(accurate_number)
print(starting_hints)
while number_guess > 0:
    user_input = int(input("Enter You'r guess: "))
    if user_input == accurate_number:
        print(f"You guess it right 😉, the number was {accurate_number}. you'r result is: {count_point(number_guess)}" )
        break
    else:
        number_guess = number_guess - 1
        print(f"Oops, you guessed it wrong 😒, you have {number_guess} guess left ", )

    if number_guess == 0:
        print("=======================Game Over==============================")
        print(f"Sorry you lost the game! better Luck next time 😊, you'r result: {count_point(number_guess)}")
