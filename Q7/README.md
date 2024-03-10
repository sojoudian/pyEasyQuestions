# Question 7: Contact Information Lookup
Task: Write a Python program that simulates a simple contact information lookup system. The program should start by asking the user to enter a name. It then looks up the name in a predefined dictionary containing names as keys and phone numbers as values. If the name is found, the program should display the corresponding phone number. If the name is not found or if the user enters invalid input (anything not a string or empty input), the program should handle these errors gracefully by informing the user and allowing them to try again.

# Requirements:

Use a dictionary to store contact names and phone numbers.
Use exception handling to catch and handle cases where the input is not a string.
Use a loop to allow the user multiple attempts to enter a valid name.
Use if statements to check if the name exists in the dictionary.

# Expected Output:
```javascript
Enter the name to look up their phone number: 123
Name should only contain letters. Please try again.
Enter the name to look up their phone number: John
Name not found. Please try again.
Enter the name to look up their phone number: Alice
The phone number of Alice is 123-456-7890
```
