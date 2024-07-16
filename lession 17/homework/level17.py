#1
for txt in range(30):
    print('GOA IS THE BEST')
#2
for i in range(5, 150):
    print(i)
#3
for i in range(2, 50, 4):
    print(i)
#4
for i in range(10):
    print(i, 'GOA')
#5
for i in range(0, 11, 1):
    print(i)
#6
num1 = int(input('Enter number: '))
guess_number = int(input('Guess the number: '))

while num1 != guess_number:
    guess_again_number = int(input('Guess number again: '))

if guess_again_number == num1:
    print(True)