import random

# Lists of characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Personalized greeting
name = input("Welcome! What's your name?\n")
print(f"Hello, {name}! Let's generate a strong password for you.")

# Existing input collection with personalized messages
nr_letters = int(input(f"{name}, how many letters would you like in your password?\n"))
nr_symbols = int(input(f"And how many symbols would you like, {name}?\n"))
nr_numbers = int(input(f"Finally, how many numbers would you like in your password?\n"))

# Generate password (same as original)
password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

# Convert list to a string
password = ""
for char in password_list:
    password += char

# Output the final password with a personalized message
print(f"{name}, your new password is: {password}")
print(f"Thanks for using the PyPassword Generator, {name}! Stay safe and secure!")
