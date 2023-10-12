import string
import random

# Obtain the desired password length from the user
password_length = int(input("Enter the length of the password: "))

print('''Choose a character set for the password from the following options:
	1. Digits
	2. Letters
	3. Special characters
	4. Exit''')

selected_characters = ""

# Obtain the character set for the password
while True:
    choice = int(input("Enter the corresponding number: "))
    if choice == 1:
        # Include letters in the character set
        selected_characters += string.ascii_letters
    elif choice == 2:
        # Include digits in the character set
        selected_characters += string.digits
    elif choice == 3:
        # Include special characters in the character set
        selected_characters += string.punctuation
    elif choice == 4:
        break
    else:
        print("Please choose a valid option!")

generated_password = []

for i in range(password_length):
    # Randomly select a character from the chosen character set
    random_character = random.choice(selected_characters)
    # Append the randomly selected character to the password
    generated_password.append(random_character)

# Print the generated password as a string
print("The randomly generated password is: " + "".join(generated_password))
