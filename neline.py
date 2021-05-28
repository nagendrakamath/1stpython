calculation_to_unit = 24
name_of_unit ="hours"

def days_to_units(num_of_days):
    print (num_of_days > 0)
    con_check = num_of_days >0
    print (type(con_check))

    if num_of_days > 0:
        return (f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}")
    elif num_of_days == 0:
        return "you have enterd Zero, Please correct it"
    else:
        return "you entered -ve value, please correct it"

user_input = input("please enter number of days\n")
if user_input.isdigit():
    user_input_number = int(user_input)
    my_var = days_to_units(user_input_number)

    print (f"your input is {user_input}")
    print(my_var)

else:
    print ("Please enter only number")