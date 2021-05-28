calculation_to_unit = 24
name_of_unit ="hours"



def days_to_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}")

def validate():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            my_var = days_to_units(user_input_number)
            print (f"your input is {user_input} days")
            print(my_var)
        elif user_input_number == 0:
            print ("you have enterd Zero, Please correct it")
        else:
            print ("you have enterd -ve number, Please correct it")

    except:
        print ("Please enter only +ve number")
while True:
    user_input = input("please enter number of days\n")
    validate()
