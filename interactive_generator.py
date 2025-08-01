#!/usr/bin/env python3
"""
Interactive Password Generator
Simple command-line interface for generating secure passwords.
"""

from password_generator import generate_password, generate_multiple_passwords, PASSWORD_SIZE

def interactive_generator():
    """Interactive password generator with user input."""
    print("🔐 Interactive Password Generator")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Generate single password (default length)")
        print("2. Generate multiple passwords")
        print("3. Generate password with custom length")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            password = generate_password()
            print(f"\n✅ Generated password: {password}")
            
        elif choice == "2":
            try:
                count = int(input(f"How many passwords? (default: 5): ") or "5")
                passwords = generate_multiple_passwords(count)
                print(f"\n✅ Generated {count} passwords:")
                for i, pwd in enumerate(passwords, 1):
                    print(f"  {i}. {pwd}")
            except ValueError:
                print("❌ Invalid number. Please enter a valid integer.")
                
        elif choice == "3":
            try:
                length = int(input(f"Enter password length (minimum 4, current default: {PASSWORD_SIZE}): "))
                if length < 4:
                    print("❌ Password length must be at least 4 characters.")
                    continue
                password = generate_password(length)
                print(f"\n✅ Generated password ({length} chars): {password}")
            except ValueError:
                print("❌ Invalid length. Please enter a valid integer.")
                
        elif choice == "4":
            print("\n👋 Goodbye! Stay secure!")
            break
            
        else:
            print("❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    interactive_generator()
