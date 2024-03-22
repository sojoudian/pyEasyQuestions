year = int(input('Enter a year: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('This is a Leap year')
        else:
            print('This is NOT a Leap year')
    else:
        print('This is a Leap year')
else:
    print('This is NOT a Leap year')
