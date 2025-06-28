import string
def check_strength(password):
    strength = 0
    length = len(password)

    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    return strength
