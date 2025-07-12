import string

def check_password(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."

    # Check for at least one special character
    if not any(char in string.punctuation for char in password):
        return "Password must contain at least one special character."

    return "Password is strong!"

# Main program
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = check_password(user_password)
    print(result)
