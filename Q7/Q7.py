contacts = {"Alice": "123-456-7890", "Bob": "987-654-3210", "Charlie": "555-555-5555"}

while True:
    name = input("Enter the name to look up their phone number: ").strip()
    try:
        if not name.isalpha():
            raise ValueError("Name should only contain letters. Please try again.")
        
        if name in contacts:
            print(f"The phone number of {name} is {contacts[name]}")
            break
        else:
            print("Name not found. Please try again.")
    except ValueError as e:
        print(e)

