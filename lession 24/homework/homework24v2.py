for i in range(0,101):
    if i % 3 == 0:
        print(i)
        print("fizz")
    if i % 5 == 0:
        print("buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")