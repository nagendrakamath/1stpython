print ("hello wold")
print (2)
print (f"20 days are {20 * 24 * 60} min" )
print (f"50 days are {50 * 24 * 60} min" )
print (f"80 days are {80 * 24 * 60} sec" )

calculation_to_unit = 24
name_of_unit ="hours"

def days_to_units(num_of_days):
    print (f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}")

days_to_units(35)
days_to_units(20)


def days_to_units(num_of_days, cust_msg):
    print (f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}")
    print (cust_msg)
days_to_units(35, "hello")
days_to_units(50, "hello1")




def days_to_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}")


my_var = days_to_units(20)

print(my_var)


def days_to_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}")


user_input = input("please enter number of days\n")
user_input_number = int(user_input)
my_var = days_to_units(user_input_number)

print (f"your input is {user_input}")
print(my_var)

