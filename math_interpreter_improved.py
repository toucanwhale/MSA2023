#ask the user if they want to continue. If y, continue. If n, end





def main():
    while True:
        #prompt user for expression and save it as a variable
        expression = input("please enter in your expression: ")


        #use .split to split the code into the numbers and expressions
        values = expression.split(" ")
        if len(values) != 3:
            print ("ERROR: enter expression in (X Y Z) format\n")
            continue
        try:
            #get values from the list
            x = int(values[0])
            y= int(values[2])
            operation = values[1]

        except ValueError:
            print("Please use numbers\n") 
            continue
    
        if operation not in ["+", "-", "*", "/"]:
            print("use a valid operation")
            continue
           
        #identify the operation with an if/elif statement and determine the correct answer to print to user
        if operation == "+":
            print(f"{x+y:.1f}")
        elif operation == "-":
            print(f"{x-y:.1f}")
        elif operation == "*":
            print(f"{x*y:.1f}")
        elif operation == "/":
            print(f"{x/y:.1f}")
        
        #ask user if they want to continue
        another_calculation = input("Would you like to evaluate another expression? (y/n): " )

        if another_calculation.lower().startswith("n"):
            break


main()