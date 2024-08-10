registered_password = "abc123"
authorized = False

while authorized != True:
    user_input = input("enter your password: ")

    if user_input == registered_password:
        print("accses granted")
        authorized = True
    else:
        print("Access denied")
