def welcome():
    print("Welcome to my Python Calculator!")


def get_num():
    number = input("Choose a number: ")
    while not number.isdecimal():
        print("This is not a number!")
        number = input("Choose a number: ")
    return float(number)


def get_op(options):
    op = input("Choose an operation: +, -, x or / ...")
    while op not in options:
        print("You have not typed in a valid operator, please try again")
        op = input("Choose an operation: +, -, x or / ...")
    return op


def calculate(num1, num2, op):
    if op == '+':
        return num1+num2
    if op == '-':
        return num1-num2
    if op == 'x':
        return num1*num2
    if op == '/':
        return num1/num2


history = []


def add_history(answer, list=history):
    list.append(answer)


def view_hist(list):
    see_history  = input("Press # if you want to see history, else press any other key.")
    if see_history == '#':
        print("Calculator History:")
        for i, cal in enumerate(list):
            print('{}   {}'.format(i + 1, cal))


welcome()
response = 'Y'
op_list = ['+', '-', 'x', '/']

while response.upper()=='Y':
    first_num = get_num()
    operator = get_op(op_list)
    second_num = get_num()
    ans = calculate(first_num, second_num, operator)
    calc = ("{} {} {} = {}".format(first_num, operator, second_num, ans))
    print(calc)
    # print(first_num, operator, second_num, " = ", ans )
    add_history(calc)
    response = input("Do you want to continue? Y/N : ")
    view_hist(history)
    if response.upper()=='N':
        print("Goodbye!")


