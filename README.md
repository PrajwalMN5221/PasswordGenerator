# PasswordGenerator
# Random Password Generator

This is a simple Python script that generates a random password based on user-defined length. It utilizes the `random` library to ensure the password is strong and includes a mix of lowercase letters, uppercase letters, numbers, and symbols.

## Features
- Generates a secure random password
- Includes lowercase, uppercase, numbers, and symbols
- User-defined password length
- Simple and easy to use

## Prerequisites
Ensure you have Python installed on your system. This script runs on Python 3.

## Usage
1. Clone or download this script to your local machine.
2. Open a terminal or command prompt and navigate to the script location.
3. Run the script using the command:
   ```sh
   python script.py
   ```
4. Enter the desired password length when prompted.
5. The generated password will be displayed on the screen.

## Code Explanation
- Import the `random` module.
- Define character sets (lowercase, uppercase, numbers, and symbols).
- Concatenate all character sets into a single variable.
- Prompt the user to enter the desired password length.
- Use `random.sample()` to generate a unique and randomized password of the specified length.
- Print the generated password.

## Example Output
```sh
Enter length of the PassWord:
10
A3b!c9D#e7
```

## Notes
- The password length should be at least 4 to ensure a mix of all character types.
- `random.sample()` ensures no repeating characters within the generated password.

