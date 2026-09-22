try:
    num1 = float(input("Give me the first number: "))
    num2 = float(input("Give me the second number: "))
    print("Thank you!")

    if num1.is_integer(): num1 = int(num1)
    if num2.is_integer(): num2 = int(num2)
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    
    if num2 != 0:
        if isinstance(num1, int) and isinstance(num2, int) and num1 % num2 == 0:
             print(f"{num1} / {num2} = {num1 // num2}")
        else:
             print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print(f"{num1} / {num2} = Error: Division by zero")
        
    print(f"{num1} * {num2} = {num1 * num2}")

except ValueError:
    pass