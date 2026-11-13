import string
def check_password_strength(password):
    score = 0
    feedback = []
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters (12 or more is better).")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include numbers (0-9).")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Include special characters (!, @, #, etc.).")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions to improve:")
        for suggestion in feedback:
            print("-", suggestion)
    else:
        print("Good! Your password meets all the basic checks.")
password = input("Enter a password to check: ")
check_password_strength(password)
