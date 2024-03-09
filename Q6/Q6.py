while True:
    filename = input("Enter the name of the file to open: ")
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
            break  # Exit the loop if file is successfully opened and read
    except FileNotFoundError:
        print("File not found. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")

