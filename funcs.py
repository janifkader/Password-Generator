import string
import random

# Build Character Pool
def create_char_pool(use_letters, use_digits, use_symbols, restrictions):
    char_pool = ''
    if use_letters:
        char_pool += string.ascii_letters # A-Z and a-z
    if use_digits:
        char_pool += string.digits # 0-9
    if use_symbols:
        char_pool += string.punctuation # Special Characters
    if not char_pool:
        print ("Error: You must select at least one type of character.")
    return "".join(set(char_pool) - set(restrictions))


# Get Password Length
def generate_password(pass_len, char_pool):
    return ''.join(random.choice(char_pool) for _ in range(pass_len))

    # Password Strength Function 
def assess_strength(password):
    score = 0
    recommendations = []
    length = len(password)
    if any(c.islower() for c in password):
        score += 1
    else:
        recommendations.append("Add lowercase letters")
    if any(c.isupper() for c in password):
        score += 1
    else:
        recommendations.append("Add uppercase letters")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        recommendations.append("Add digits")
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        recommendations.append("Add symbols")
    if length >= 12:
        score += 1
    else:
        recommendations.append("Increase length to at least 12 characters")
    levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent",
     }
    return levels[score], recommendations
    
    


