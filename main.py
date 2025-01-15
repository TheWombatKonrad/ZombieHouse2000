from math import inf, ceil
from os import system, name
import random
from time import sleep

def input_valid_int(question, error_text, min=0, max=inf):
    while True:
        try:
            value = int(input(question))
            if min <= value <= max:
                return value
            else:
                print(error_text, end=" ")
        except ValueError:
            print(error_text, end=" ")

def input_valid_str(question, error_text, possible_answers):
    answer = input(question)
    while answer not in possible_answers:
        answer = input(f'{error_text}\n{question}')

    return answer

# Clears the screen depending on the OS used.
def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

# Returns a parameter that has been used less than the max amount.
def get_parameter(max_repeats, previous_numbers):
    while True:
        parameter = random.randint(0, 12)
        if previous_numbers.count(parameter) < max_repeats:
            return parameter

# Runs the operation based on the assigned method.
def run_math(method, constant_parameter, random_parameter):
        if method == "*":    
            return constant_parameter * random_parameter

        elif method == "//":
            return random_parameter // constant_parameter

        elif method == "%":
            return random_parameter % constant_parameter

continue_playing = True
eaten_by_zombies = False

while continue_playing:
    # If true, the player has lost the previous round, and the previous conditions are repeated.
    if not eaten_by_zombies:
        print("*********************************" +
          "\nZombie House 2000" +
          "\n*********************************")

        number_of_questions = input_valid_int("How many questions would you like? ",
            "Please enter a number between 12 and 39.", 12, 39)
    
        method = input_valid_str(f"What calculation method would you like? Choose between *, //, and %: ", 
            f"Please choose between *, //, and %. ", ["*", "//", "%"])
    
        if method == "*":
            table = input_valid_int("On which table, between 2 and 12, do you want to answer? ", 
                "Please enter a number between 2 and 12.", 2, 12)
        else:
            table = input_valid_int("Which divisor between 2 and 5 would you like? ",
                "Please enter a number between 2 and 5.", 2, 5)
        
    clear_screen()
    print("*********************************" +
          "\nZombie House 2000" +
          "\n*********************************")
    
    previous_numbers = []
    remaining_doors = number_of_questions
    max_repeats = ceil(number_of_questions / 13)
    # Resets the game if the player has already lost once.
    eaten_by_zombies = False
    
    for i in range(number_of_questions):
        print(f"Question {i + 1} of {number_of_questions}:", end=" ")

        # This is the factor or dividend.
        parameter = get_parameter(max_repeats, previous_numbers)
        previous_numbers.append(parameter)

        # Multiplication
        if method == "*":    
            user_answer = input_valid_int(f"{table} * {parameter} = ", "Please enter a number. ")
            correct_answer = run_math("*", table, parameter)
                
        # Integer division
        elif method == "//":
            user_answer = input_valid_int(f"{parameter} // {table} = ", "Please enter a number. ")
            correct_answer = run_math("//", table, parameter)

        # Modulus
        elif method == "%":
            user_answer = input_valid_int(f"{parameter} % {table} = ", "Please enter a number. ")
            correct_answer = run_math("%", table, parameter)

        if user_answer != correct_answer:
            print("No! Because of your bad math the zombies got you.")
            sleep(2)
            eaten_by_zombies = True

        # If the player survived the math test, they get to choose a door.
        if not eaten_by_zombies and remaining_doors > 1:
            door_with_zombie = random.randint(1, remaining_doors)
            print(door_with_zombie)
            user_door = input_valid_int(f"You see {remaining_doors} doors, which one do you choose? ",
             f"Please enter a number between 1 and {remaining_doors}.", 1, remaining_doors)

            if door_with_zombie == user_door:
                print("Zombies! You're dead.")
                sleep(2)
                eaten_by_zombies = True
            else:
                print("Whew! No zombies.", end="\n\n") 
                remaining_doors -= 1 

        if eaten_by_zombies:
            break

    clear_screen()

    # If the player survived the game.
    if not eaten_by_zombies:
        print("You have survived the zombie house!")
        sleep(2)
        clear_screen()

    answer = input_valid_str("Do you want to play again? y/n: ",
        "Please choose y or n. ", ["y", "n"])
    if answer == "n":
        continue_playing = False
    
    clear_screen()
