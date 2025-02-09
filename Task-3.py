import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase and lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Number check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")

    # Determine strength level
    if strength == 4:
        return "Strong password! ✅"
    elif strength == 3:
        return "Moderate password. Consider adding a special character or number."
    else:
        return "Weak password. Suggestions:\n" + "\n".join(feedback)

# Example usage
password = input("Enter a password to check: ")
print(check_password_strength(password))
