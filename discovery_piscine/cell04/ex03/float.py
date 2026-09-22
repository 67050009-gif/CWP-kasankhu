user_input = float(input("Give me a number: "))

if user_input.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")