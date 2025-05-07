calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

# try exept
def validate(user_input):
    try: # try execute logic
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a positive number.")
        else:
            print("No negative numbers allowed.")
    except ValueError: # except ValueError if values is wrong
        print("Input is not a valid number!")

# Get input from user
user_input = input("Enter number of days to convert it to hours:\n")
validate(user_input)
