def factorial_number(num):
    if num < 0:
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, num+1):
            factorial *= i
        return factorial
    
while True:
    try: 
        number = int(input("Enter a number or -1 to exit: "))
        if number == -1:
            break
        if factorial_number(number) is not None:
            print(f"The factorial number of {number} is {factorial_number(number)}")
        else:
            print("Factorial is not defined for negative numbers.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")