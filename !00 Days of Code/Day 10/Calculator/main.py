from art import logo
from os import system


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        print("Invalid value provided for second number!!")
        return None
    return num1 / num2


def operations(f_num=None):
    if f_num is None:
        f_num = float(input("Enter the first number = "))
    operator = input("Enter the operator (+,-,*,/) : ")
    s_num = float(input("Enter the second number = "))
    dict_of_operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    calculation_function = dict_of_operations[operator]
    result = calculation_function(f_num, s_num)
    print(f"{f_num} {operator} {s_num} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation and "
                   f"'exit' to terminate the program: ").lower()
    if choice == 'y':
        operations(result)
    elif choice == 'n':
        calc()
    elif choice == 'exit':
        return


def calc():
    system("cls")
    print(logo)
    operations()


calc()
