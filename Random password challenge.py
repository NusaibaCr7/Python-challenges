import random
import string

def generate_password(length):
    if length<6:
        return "Password length must be at least of 6 characters"
    
    lowerCase_char = string.ascii_lowercase
    upperCase_char = string.ascii_uppercase
    digits = string.digits
    special_char = string.punctuation
    
    password = [random.choice(lowerCase_char), random.choice(upperCase_char), random.choice(digits), random.choice(special_char)]
    random.shuffle(password)
    return ''. join(password)

password_length = random.randint(6,10)
password = generate_password(password_length)
print(f"Generate Password: {password}")