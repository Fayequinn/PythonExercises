import getpass
password = '4567'
count = 1
while count < 3:
    supplied_pin = getpass.getpass(prompt="Enter you PIN:")

    if supplied_pin == password:
        print("Access granted")
        break
    else:
        print("You have entered the wrong PIN")
    count += 1
if count == 3:
    supplied_pin = getpass.getpass(prompt="Enter you PIN:")

    if supplied_pin == password:
        print("Access granted")
    else: print("You have entered an incorrect PIN too many times, your account is now locked.")