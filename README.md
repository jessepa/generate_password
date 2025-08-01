# Password Generator

A secure password generator that creates passwords meeting specific security requirements.

## Features

✅ **Security Requirements Met:**
- At least one lowercase letter (a-z)
- At least one uppercase letter (A-Z)  
- At least one digit (0-9)
- At least one special character from `!@#$%&*()?`

✅ **Configurable:**
- Global `PASSWORD_SIZE` variable for easy length adjustment (default: 12)
- Support for custom password lengths
- Multiple password generation

## Files

- `password_generator.py` - Main password generator module with demo
- `interactive_generator.py` - Interactive command-line interface

## Usage

### Basic Usage

```bash
python3 password_generator.py
```

This will display:
- A single generated password
- Multiple password options
- A custom length example

### Interactive Mode

```bash
python3 interactive_generator.py
```

This provides a menu-driven interface to:
1. Generate single passwords
2. Generate multiple passwords
3. Create passwords with custom lengths
4. Exit the program

### Programmatic Usage

```python
from password_generator import generate_password, generate_multiple_passwords

# Generate a single password with default length
password = generate_password()

# Generate password with custom length
long_password = generate_password(16)

# Generate multiple passwords
passwords = generate_multiple_passwords(5, 12)
```

## Configuration

To change the default password length, modify the `PASSWORD_SIZE` variable in `password_generator.py`:

```python
PASSWORD_SIZE = 16  # Change from 12 to 16 characters
```

## Security Notes

- Passwords are generated using Python's `random` module
- Characters are shuffled to avoid predictable patterns
- All character requirements are guaranteed to be met
- Minimum password length is 4 characters (to satisfy all requirements)

## Examples

Sample generated passwords:
```
d?7jlVBG)yCC     (12 characters)
GS6*A61Nm(W65ps( (16 characters)
@Z1f             (4 characters - minimum)
```

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)
