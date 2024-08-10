while True:
    mid_term = int(input('Enter your mid term grade: '))
    final = int(input('Enter your final grade: '))
    project = int(input('Enter your project grade: '))
    if 0 < mid_term <= 100 and 0< final <= 100 and 0 < project < 100:
        average = (mid_term + final + project) / 3
        if  average >= 70:
            print('You passed')

        else:
            print('You failed')

        break
    else:
        print('Please enter valid grade')