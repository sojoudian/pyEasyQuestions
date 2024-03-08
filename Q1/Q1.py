while True:
    try:
        # Prompt the user for input
        user_input = input("Enter a number between 1 and 10: ")
        number = int(user_input)  # Attempt to convert the input to an integer
        
        # Check if the number is within the valid range
        if 1 <= number <= 10:
            # Calculate and print the square of the number
            print(f"The square of {number} is {number ** 2}")
            break  # Exit the loop
        else:
            # Number is out of range
            print("Error: Invalid input. Please enter a number between 1 and 10.")
            
    except ValueError:
        # Handle non-numeric input
        print("Error: Invalid input. Please enter a number between 1 and 10.")

