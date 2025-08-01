#!/usr/bin/env python3
"""
Password Generator with specific requirements:
- At least one lowercase letter
- At least one uppercase letter  
- At least one digit
- At least one special character from "!@#$%&*()?"
- Configurable password length
"""

import random
import string

# Global variable for password size - easy to change
PASSWORD_SIZE = 12

def generate_password(length=PASSWORD_SIZE):
    """
    Generate a secure password with the following requirements:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one digit
    - At least one special character from "!@#$%&*()?"
    
    Args:
        length (int): Length of the password to generate
        
    Returns:
        str: Generated password meeting all requirements
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to meet all requirements")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%&*()?"
    
    # Ensure at least one character from each required category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password with random characters from all categories
    all_chars = lowercase + uppercase + digits + special_chars
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def generate_multiple_passwords(count=5, length=PASSWORD_SIZE):
    """
    Generate multiple passwords for selection.
    
    Args:
        count (int): Number of passwords to generate
        length (int): Length of each password
        
    Returns:
        list: List of generated passwords
    """
    return [generate_password(length) for _ in range(count)]

def main():
    """Main function to demonstrate the password generator."""
    print("🔐 Secure Password Generator")
    print("=" * 40)
    print(f"Password Length: {PASSWORD_SIZE} characters")
    print("Requirements:")
    print("  ✓ At least one lowercase letter")
    print("  ✓ At least one uppercase letter")
    print("  ✓ At least one digit")
    print("  ✓ At least one special character (!@#$%&*()?)")
    print("\n" + "=" * 40)
    
    # Generate a single password
    print("\n🎲 Generated Password:")
    password = generate_password()
    print(f"  {password}")
    
    # Generate multiple options
    print(f"\n📋 Multiple Options (length: {PASSWORD_SIZE}):")
    passwords = generate_multiple_passwords(5)
    for i, pwd in enumerate(passwords, 1):
        print(f"  {i}. {pwd}")
    
    # Demonstrate custom length
    custom_length = 16
    print(f"\n🔧 Custom Length Example ({custom_length} characters):")
    custom_password = generate_password(custom_length)
    print(f"  {custom_password}")

if __name__ == "__main__":
    main()
