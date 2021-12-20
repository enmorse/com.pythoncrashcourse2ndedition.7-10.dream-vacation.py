# Write a program that polls users about their dream
# vacation. Write a prompt similar to "If you could
# visit one place in the world, where would you go?".
# Include a block of code that prints the results of
# the poll.
dream_vacations = {}
active_response = True

while active_response:
    prompt = input("\nWhat is your name?: ")
    dream_vacation = input("\nIf you could visit one "
                           "place in the world, where would "
                           "you go?: ")

    dream_vacations[prompt] = dream_vacation

    ask_again = input("Would you like to enter another "
                      "dream vacation location?: (yes / no)")

    if ask_again == 'no':
        active_response = False
    
    for prompt, dream_vacation in dream_vacations.items():
        print(f"{prompt} would like to visit "
              f"{dream_vacation}.")
