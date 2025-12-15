# Simple Random Password Generator for Beginners
import random
import string

print("Welcome to the Simple Password Generator!")

# Ask user for password length
while True:
    try:
        length = int(
            input("\nEnter the desired password length (minimum 4): "))
        if length < 4:
            print("Please choose a length of at least 4 for better security!")
        else:
            break
    except ValueError:
        print("Please enter a valid number!")

# Ask user what characters they want to include
print("\nChoose character types to include:")
use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols (!@#$ etc.)? (y/n): ").lower() == 'y'

# Build the character pool based on user choices
characters = ""

if use_letters:
    characters += string.ascii_letters    # A-Z and a-z
if use_numbers:
    characters += string.digits           # 0-9
if use_symbols:
    characters += string.punctuation      # !@#$%^&* etc.

# If user selected nothing, use a safe default
if not characters:
    print("You didn't choose anything! Using letters + numbers by default.")
    characters = string.ascii_letters + string.digits

# Generate the password
password = ''.join(random.choice(characters) for _ in range(length))

# Show the result
print("\n" + "="*40)
print(f"Your secure password is:")
print(f"{password}")
print("="*40)

# Bonus: Show password strength
strength = "Weak"
if length >= 12 and use_letters and use_numbers and use_symbols:
    strength = "Very Strong"
elif length >= 8 and use_letters and (use_numbers or use_symbols):
    strength = "Strong"

print(f"Password strength: {strength}")

# Ask if user wants another password
again = input("\nGenerate another password? (y/n): ")
if again.lower() == 'y':
    # Restart the program (simple way for beginners)
    exec(open(__file__).read())
