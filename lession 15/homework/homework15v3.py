weight = int(input('Enter your weight in kilograms: '))
height = int(input('Enter your height in metres: '))

BMI = weight / height

print(BMI)

if BMI < 18.5:
    print('Underweight')

if BMI >= 18.5 < 24.9:
    print('Normal weight')

if BMI >= 25 < 29.9:
    print('Overweight')

if BMI >= 30:
    print('Fat')



