from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import shuffle, choice

def Generator():
    char_password = input("How many characters would you like for your new password? ")

    # Check Input Validation 
    while True:
        try:
            char_password = int(char_password)
            if char_password < 10:
                print("A strong password should consist of at least 10 characters.")
                char_password = input("How many characters would you like for your new password? ")
            else:
                break
        except ValueError:
            print("Please enter only numerical values!")
            char_password = input("How many characters would you like for your new password? ")

    shuffle(list(ascii_uppercase))
    shuffle(list(ascii_lowercase))
    shuffle(list(digits))
    shuffle(list(punctuation))

    # Generate password components
    new_password = []

    for letter in range(round(char_password * 0.03)):
        new_password.append(choice(list(ascii_uppercase[letter])))
        new_password.append(choice(list(ascii_lowercase[letter])))
        
    for digit_punct in range(round(char_password * 0.02)):
        new_password.append(choice(list(digits[digit_punct])))
        new_password.append(choice(list(punctuation[digit_punct])))
        
    # Fill the rest of the password length with random choices from all categories
    all_chars = list(ascii_uppercase) + list(ascii_lowercase) + list(digits) + list(punctuation)
    while len(new_password) < char_password:
        new_password.append(choice(all_chars))

    # Shuffle the final password list to ensure randomness
    shuffle(new_password)

    # Join the list into a single string
    new_password = "".join(new_password)

    return new_password
    
with open("password_generator.txt", 'a') as passwords:
    number_of_password = int(input("Number of passwords? "))
    for i in range(number_of_password):
        password = Generator()
        passwords.write(password + "\n" )

with open("password_generator.txt", 'r') as passwords:
    content = passwords.read()
    print(content.strip())