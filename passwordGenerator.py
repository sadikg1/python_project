import random
import string

def generate_password(length=8):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password with random characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Prompt the user to enter the desired length of the password
length = int(input("Enter the desired length of the password: "))

# Generate and display the password
password = generate_password(length)
print("Generated Password:", password)
