PassGuard 🔐

**A Simple Password Strength Checker and Generator**

**Overview**:
PassGuard is a Python-based password utility that evaluates the.slice of strength of a user-provided password and generates a secure alternative if needed. It checks for common weak passwords, analyzes character composition, assigns a strength score, and provides feedback to improve password security.
The project is designed to demonstrate basic cybersecurity principles such as password hygiene, entropy, and defensive programming.

**Features**:
Detects commonly used weak passwords
Scores passwords based on:
1.Length
2.Lowercase letters
3.Uppercase letters
4.Digits
5.Special characters

Provides improvement feedback when weaknesses are detected
Generates a random, secure password using letters, digits, and symbols

Technologies Used
Python 3
Built-in modules:
1. random
2. string

**How It Works**:-

1.The user enters a password.
2.The program checks whether it exists in a predefined list of common passwords.
3.If not common, the password is evaluated and given a score from 0 to 10.
4.Based on the score, the password is categorized as:
Very Weak
Weak
Medium
Strong
Very Strong
5.A secure password is generated and suggested to the user.

**Running the Program
Prerequisites**:-
Python 3 installed on your system
**Example Output:**:
Password strength score
Feedback on missing character types
Suggested strong password

**Possible Improvements**
:Prevent repeated characters in generated passwords
Use cryptographically secure random generation (secrets module)
Add a GUI or web interface
Store common passwords externally for scalability

**Disclaimer:**
This project is for educational purposes only and should not be used as a replacement for professional password management tools.

Author
Oishika
B.Tech Student, KIIT
