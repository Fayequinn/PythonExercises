print("Welcome to my Python Calculator!")
response = 'Y'
history = []
while response.upper()=='Y':

    input1 = input("Give me a number... ")
    while not input1.isdecimal():
        print("This is not a number")
        input1 = input("Give me a number... ")

    operation = input("Choose an operation: +, -, x or / ...")

    input2 = input("Give me your second number... ")
    while not input2.isdecimal():
        print("This is not a number")
        input2 = input("Give me your second number... ")

    if operation == '+':
        num1=float(input1)
        num2=float(input2)
        ans = ("{} + {} = {}".format(num1, num2, num1+num2))
        print(ans)
        history.append(ans)


    elif operation == '-':
        num1 = float(input1)
        num2 = float(input2)
        ans = ("{} - {} = {}".format(num1, num2, num1-num2))
        print(ans)
        history.append(ans)


    elif operation == 'x':
        num1 = float(input1)
        num2 = float(input2)
        ans = ("{} * {} = {}".format(num1, num2,num1*num2))
        print(ans)
        history.append(ans)

    elif operation == '/':
        num1 = float(input1)
        num2 = float(input2)
        ans = ("{} / {} = {}".format(num1, num2, num1/num2))
        print(ans)
        history.append(ans)


    else:print("You have not typed in a valid operator, please try again")
    response = input("Do you want to continue? Y/N : ")
    see_history = input("Press # if you want to see history, else press any other key.")
    if see_history =='#':
        print("Calculator History:")
        for i, calc in enumerate(history):
            print('{}   {}'.format(i + 1, calc))
            
            # print('{} {}'.format(history.index(calc)+1, calc))

            # print(history.index(calc)+1, end=' ')
            # print(" ", calc)

    if response.upper()=='N':
        print("Goodbye!")