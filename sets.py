calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a positive number.")
        else:
            print("No negative numbers allowed.")
    except ValueError:
        print("Input is not a valid number!")

# While Loops
user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days to convert it to hours:\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    
    for num_of_days_element in set(user_input.split(",")):
        validate_and_execute()