calculation_to_units = 24
calculation_to_units_1 = 24
name_of_unit = "hours"
# Functions

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")


user_input = input("Enter number of days to convert it to hours:\n")

print(user_input)



#function with return values

def days_to_units_1(num_of_days):
    return(f"{num_of_days} days are {num_of_days * calculation_to_units_1} {name_of_unit}")
# Input always return a string 
user_input = input("Enter number of days to convert it to hours:\n")

#Casting - turning one datatype in to another one 
# int - converts specified value into an integer number
user_input_number = int(user_input)

calcutated_value = days_to_units_1(user_input_number)
print(calcutated_value)

