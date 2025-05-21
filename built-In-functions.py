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
    print (type(user_input.split(", ")))
    print (user_input.split(", "))
    for num_of_days_element in user_input.split(","):
        validate_and_execute()


# Built-in-Functions
# Eeach data type has it own built-in functions
print("text")
input("enter value")
set([1, 3, 5])
int("20")

"2, 3".split()
[1, 3, 5].count()