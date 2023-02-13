print("WARNING: The order you type in the operations is the order I will carry them out. I am not using BIDMAS!")

user_calc=input("Please enter your multi-step calculation with a space between your numbers and operators: ")

list=user_calc.split(" ")
print(' '.join(list)+' =')
num1=int(list[0])
num2=int(list[2])
num3=int(list[4])

if list[1]=='+':
    first_ans=num1+num2
    if list[3] == '+':
        final_ans = first_ans + num3
        print(final_ans)
    if list[3] == '-':
        final_ans = first_ans - num3
        print(final_ans)
    if list[3] == 'x':
        final_ans = first_ans * num3
        print(final_ans)
    if list[3] == '/':
        if num3 == 0:
            print("MATH ERROR:You can't divide by 0!")
        else:
            final_ans = first_ans / num3
            print(final_ans)

if list[1]=='-':
    first_ans=num1-num2
    if list[3] == '+':
        final_ans = first_ans + num3
        print(final_ans)
    if list[3] == '-':
        final_ans = first_ans - num3
        print(final_ans)
    if list[3] == 'x':
        final_ans = first_ans * num3
        print(final_ans)
    if list[3] == '/':
        if num3 == 0:
            print("MATH ERROR:You can't divide by 0!")
        else:
            final_ans = first_ans / num3
            print(final_ans)
if list[1]=='x':
    first_ans=num1*num2
    if list[3] == '+':
        final_ans = first_ans + num3
        print(final_ans)
    if list[3] == '-':
        final_ans = first_ans - num3
        print(final_ans)
    if list[3] == 'x':
        final_ans = first_ans * num3
        print(final_ans)
    if list[3] == '/':
        if num3 == 0:
            print("MATH ERROR:You can't divide by 0!")
        else:
            final_ans = first_ans / num3
            print(final_ans)
if list[1]=='/':
    if num2==0:
        print("MATH ERROR:You can't divide by 0!")
    else:
        first_ans=num1/num2
        if list[3] == '+':
            final_ans = first_ans + num3
            print(final_ans)
        if list[3] == '-':
            final_ans = first_ans - num3
            print(final_ans)
        if list[3] == 'x':
            final_ans = first_ans * num3
            print(final_ans)
        if list[3] == '/':
            if num3 == 0:
                print("MATH ERROR:You can't divide by 0!")
            else:
                final_ans = first_ans / num3
                print(final_ans)

# if list[3]=='+':
#     final_ans=first_ans+num3
# if list[3]=='-':
#     final_ans =first_ans-num3
# if list[3] == 'x':
#     final_ans = first_ans * num3
# if list[3] == '/':
#     if num3==0:
#         print("MATH ERROR:You can't divide by 0!")
#     else:
#         final_ans = first_ans / num3
#         print(final_ans)