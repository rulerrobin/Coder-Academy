def add (num1, num2):
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def division (num1, num2):
    return num1 / num2 

def convert_into_list(num1, num2, num3):
    return [num1, num2, num3]

def get_user_input_double():
    number = int(input("Enter a number: ")) 
    sum = add(number, number)

def get_user_input_add():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = add(num1, num2)
    return sum