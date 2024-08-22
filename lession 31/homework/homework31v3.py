password = "nikobest"
authorized = False

while authorized != True:
    guess_password = input("enter password: ")

    if password == guess_password:
        authorized = True
        print('access granted')
    else:
        print('access denied')