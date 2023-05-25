"""
This is the simplest interactive Python game :-)
"""
import random
the_number = random.randint(0, 9)
print("""
HELLO!
You have to guess the number from 0 to 9
and do it in the minimum number of attempts

STARTED:""")
attempt_counter = 0
while True:
    your_number = input(
        "\nEnter a number from 0 to 9: ")
    if your_number.isdigit():
        attempt_counter += 1
        if int(your_number) < the_number:
            print("\nYour number is less than guessed,")
            print("try again:")
        elif int(your_number) > the_number:
            print("\nYour number is more than guessed,")
            print("try again:")
        else:
            print("\n\nCONGRATULATIONS!!!")
            print(
                f"You guessed with {attempt_counter} attempt(s)!")
            break
    elif not your_number:
        print("\nPlease enter something.")
    else:
        print("\n\nPlease enter numbers from 0 to 9.")
        print(
            f'The entered symbol "{your_number}" is not a number.')
