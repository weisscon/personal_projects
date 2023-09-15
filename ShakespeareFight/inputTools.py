'''
Conor Weiss
10/07/22

A personal library for input validation tools

Functions included are:
1. float_input_validation function
2. bounded_integer_input_validation function
'''

'''
float input validation function
inputs: 1 string
prints string and gets an input.  Will not advance until user gives input that can be a float
returns 1 float
'''

def float_input_validation(prompt:str):
    user_input = 'a'
    while (bool(type(user_input) == str)):
        try:
            user_input = float(input(prompt))
        except ValueError:
            print("Input must be a number")
    return(user_input)

'''
bounded integer input validation function
inputs: 2 integers, 1 string
prints string and gets an input.  Will not advance until user gives a number between the upper and lower bounds
returns 1 integer
'''

def bounded_integer_input_validation(upper_bound:int, lower_bound:int, prompt:str):
    user_input = -10000
    while (user_input<lower_bound or user_input > upper_bound):
        try:
             user_input = int(input(prompt))
        except ValueError:
            user_input = -10000
        if (user_input<lower_bound or user_input > upper_bound):
            print("Please enter a number between " + str(lower_bound) +" and " + str(upper_bound) + ".")
    return(user_input)
