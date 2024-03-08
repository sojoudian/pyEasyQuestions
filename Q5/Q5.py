while True:
    try:
        number = int(input("Enter a positive number to generate its multiplication table: "))
        if number <= 0:
            print("Please enter a positive number.")
        else:
            for i in range(1, 11):
                print(f"{number} x {i} = {number*i}")
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

