print("Welcome to my extended Python calculator!")
response='Y'
while response.upper()=='Y':
    user_num_list=input("Enter a list of numbers you would like to perform an operation on. Seperate your numbers with a space: ")
    num_list=user_num_list.split(" ")

    int_list=list(map(int,num_list))
    print("You entered:",(int_list))

    user_op=input("What operation would you like to perform on these numbers? +, -, x or / : ")

    answer=int_list[0]
    if user_op== '+':
        for x in int_list[1:]:
            answer+=x
        print('+'.join(num_list))
        print(answer)

    if user_op== '-':
        for x in int_list[1:]:
            answer-=x
        print('-'.join(num_list))
        print(answer)

    if user_op== 'x':
        for x in int_list[1:]:
            answer*=x
        print('x'.join(num_list))
        print(answer)

    if user_op== '/':
        err=int(0)
        if err in int_list[1:]:
            print("MATH ERROR: You cannot divide by 0!")
        else:
            for x in int_list[1:]:
                answer /= x
            print('/'.join(num_list))
            print(answer)
    response = input("Do you want to continue? Y/N : ")
    if response.upper()=='N':
        print("Goodbye!")









# answer1=0
# list1 = [2, 3, 5, 7]
# for i in list1:
#     answer1+=i
# print(answer1)

# list = [2, 3, 11, 4]
# answer = list[0]
# for i in list[1:]:
#     answer-=i
# print(answer)

# answer2=1
# list2 = [2, 4, 6, 2]
# for i in list2:
#     answer2*=i
# print(answer2)

# list3 = [20, 4, 5]
# answer3 = list3[0]
# for i in list3[1:]:
#     answer3/=i
# print(answer3)