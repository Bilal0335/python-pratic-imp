import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    # Define character sets based on user preferences
    character_set = ''
    
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_digits:
        character_set += string.digits
    if use_special_chars:
        character_set += string.punctuation

    if not character_set:
        return "Error: You must select at least one character set."

    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    
    return password

# Get user preferences
length = int(input("Enter the desired password length: "))
use_lowercase = input("Use lowercase letters? (yes/no): ").lower() == "yes"
use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == "yes"
use_digits = input("Use digits? (yes/no): ").lower() == "yes"
use_special_chars = input("Use special characters? (yes/no): ").lower() == "yes"

# Generate the password
password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
print("Generated Password:", password)
