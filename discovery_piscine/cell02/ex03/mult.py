try:
    num1 = float(input("Enter the first number:\n"))
    num2 = float(input("Enter the second number:\n"))
    
    result = num1 * num2
    
    if num1.is_integer(): num1 = int(num1)
    if num2.is_integer(): num2 = int(num2)
    if result.is_integer(): result_display = int(result)
    else: result_display = result
    
    print(f"{num1} x {num2} = {result_display}")
    
    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.")
        
except ValueError:
    pass