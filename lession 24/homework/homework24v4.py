while True:
    age = int(input('Enter your age: '))
    experience = int(input("Enter your experience(how many years you have been driving)"))
    if age < 18:
        print('You are not old enough to have license: ')

    elif age >= 18 and experience >= 1:
        print('You can have license')

    elif age >= 18 and experience < 1:
        print('You do not have enough experience to have a driving license')
    break
else:
    print('please enter valid number')
