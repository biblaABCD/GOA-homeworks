def simple_calculator(num1,num2,do):
    if do == "-":
        answer = num1 - num2
        print (anws)
    elif do == "+":
        answer = num1 + num2
        print (anws)
    elif do == "*":
        answer = num1 * num2
        print (anws)
    elif do == "/":
        answer = num1 / num2
        print (answer)
    else:
        print ("wrong number try again")

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
do = input("Enter which operation you want to do: ")
simple_calculator(num1,num2,do)