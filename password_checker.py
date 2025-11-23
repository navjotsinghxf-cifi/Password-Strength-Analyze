import re

def check_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    return strength

def rating(score):
    if score <= 2:
        return "WEAK"
    elif score == 3:
        return "MEDIUM"
    else:
        return "STRONG"

password = input("Enter password: ")
score = check_strength(password)

print(f"\nPassword Strength: {rating(score)}")

if score < 5:
    print("\nSuggestions:")
    print("- Use uppercase letters")
    print("- Add numbers")
    print("- Add special characters")
    print("- Make it longer (12+ characters)")
