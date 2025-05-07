calculation_to_units = 24
name_of_unit = "hours"
# Functions

def days_to_units_1(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

days_to_units_1(20)
days_to_units_1(35)
days_to_units_1(60)
days_to_units_1(110)


calculation_to_hours = 24
name_of_unit = "hours"

# Define a function
def days_to_units_2(num_of_days, custom_massage):
    print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")
    print (custom_massage)

# Call the function with different day values
days_to_units_2(20, "Great")
days_to_units_2(35, "Awesome")
days_to_units_2(60, "Magnificent")   
days_to_units_2(110, "Scooby-dooo")


def scope_check(custom_massage):
    my_var= "Lolipop" # internal variable
    print(name_of_unit) # global variable
    print(custom_massage)
    print(my_var)

scope_check("Yaba-daba-doo")