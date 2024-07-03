age = int(input('Enter your age: '))

money_spent = int(input('Enter how much you have spent: '))

discount = (age >= 60 or money_spent > 100)

discount2x = (age >= 60 and money_spent > 100)

if discount2x == True:
    print('You have 2x discount')

if discount == True:
    print('You have discount')

else:
    print("you don't have fasdakleba")