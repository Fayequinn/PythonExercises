print("Welcome to my Python Calculator!")
response = 'Y'
while response.upper()=='Y':

    num1 = float(input("Give me a number... "))
    operation = input("Choose an operation: +, -, x or / ...")
    num2 = float(input("Give me your second number... "))
    if operation == '+':
        print("{} + {} = ".format(num1, num2))
        print(num1+num2)

    elif operation == '-':
        print("{} - {} =".format(num1, num2))
        print(num1-num2)


    elif operation == 'x':
        print("{} * {} =".format(num1, num2))
        print(num1*num2)

    elif operation == '/':
        print("{} / {} =".format(num1, num2))
        print(num1/num2)


    else:print("You have not typed in a valid operator, please try again")
    response = input("Do you want to continue? Y/N : ")
    if response.upper()=='N':
        print("Goodbye!")
