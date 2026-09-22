try:

    number = int(input("Enter a number\n"))
    
    for i in range(10):
        result = i * number
        print(f"{i} x {number} = {result}")
        
except ValueError:
    pass