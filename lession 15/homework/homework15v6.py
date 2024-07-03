GPA = float(input('Enter your GPA: '))

family_income = int(input('Enter your family income: '))


scholarship = (GPA >= 3 or family_income >= 50000)

if scholarship == True:
    print('You have highest scholarship.')

if scholarship == False:
    print("You don't have scholarship, you need 50k$ for scholarship.")
