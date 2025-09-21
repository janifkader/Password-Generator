import string
import random

# Build Character Pool
print"Welcome to the Password Generator!"
print"Please select which types of characters to include in your password:"
use_letters = input ("Include letters? (y/n):").strip().lower()== 'y'
use_digits = input ("Include digts? (y/n):").strip().lower()== 'y'
use_symbols = input ("Include symbols? (y/n):").strip().lower()== 'y'

char_pool = ''
if use_letters:
    char_pool += string.ascii_letters # A-Z and a-z
if use_digits:
    char_pool += string.ascii_digits # 0-9
if use_symbols:
    char_pool += string.ascii_punctuation # Special Characters
if not char_pool:
print (" ❌  Error: You must select at least one type of character.") 
exit()
return char_pool


# Get Password Length
def generate_password(length, char_pool):
    return ''.join(random.choice(char_pool) for _ in range(length))

while True:
    try:
        length = int(input("Enter desired password length (8-25): "))
        if 8 <= length <= 25:
            break
        else:
            print(" ❌  Error: Length must be between 8 and 25.")
    except ValueError:
        print(" ❌  Error: Please enter a valid number.")
   password = generate_password(length, char_pool)
   (strength_label, emoji), suggestions = assess_strength(password)

   # Display Password and Strength
    print("\n ✅ Generated Password:", password)
    print(f" 🔒 Password Strength: {strength_label} {emoji}")

    if strength_label in ["Very Weak", "Weak", "Moderate"]:
        print(" 💡 Suggestions to improve your password:")
        for suggestion in suggestions:
            print(f"   - {suggestion}")

            regenerate = input("\nWould you like to generate a new, stronger password? (y/n): ").strip().lower()
            if regenerate == 'y':
                print("\n Restarting password generation...\n")
                # You can loop back to the start or just exit
                # For Now, just remind the user
                print("Please run the program again to generate a new password.")
                else:
                print("\n👍 Okay! Use the password with caution")
                else:
    print("\n🎉🎊 Great! Your password is strong. Awesome Job, Well done!!!")

    # Password Strength Function 
def assess_strength(password):
    score = 0
    reccomendations = []
    length = len(password)
    if any(c.islower() for c in password):
        score += 1
        else: reccomendations.append("Add lowercase letters")
    if any(c.isupper() for c in password):
        score += 1
        else: reccomendations.append("Add uppercase letters")
    if any(c.isdigit() for c in password):
        score += 1
        else: reccomendations.append("Add digits")
    if any(c in string.punctuation for c in password):
        score += 1
        else: reccomendations.append("Add symbols")
    if len(password) >= 12:
        score += 1
        else: reccomendations.append("Increase length to at least 12 characters")

        levels = { 
        0: ("Very Weak", "🔴"),
        1: ("Weak", "🟠"),
        2: ("Moderate", "🟡"),
        3: ("Strong", "🟢"),
        4: ("Very Strong", "🔵"),
        5: ("Excellent", "🌟")
        }
        return levels[score], reccomendations
    
    


