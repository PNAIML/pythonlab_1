import re

def password_strength_checker(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    if all([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria]):
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and (digit_criteria or special_char_criteria):
        return "Moderate"
    else:
        return "Weak"

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = password_strength_checker(password)
    print(f"Password strength: {strength}")
