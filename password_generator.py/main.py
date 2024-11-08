import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        print("Generated password:", password)
    except ValueError:
        print("Invalid input! Please enter a number for the length.")
