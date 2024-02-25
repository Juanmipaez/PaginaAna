import random
import string

def create_password(psw_length):
    password=''
    for i in range(psw_length):
        random_character = random.choice(characters)
        password+=random_character
    print(password)

print('Welcome to password generator')
amount_of_passwords = int(input('Please enter the desired amount of passwords: '))
length_of_password = int(input('Please enter the desired length of the password: '))
print('Choose all you would like to apply: ')
print('1. Letters')
print('2. Digits')
print('3. Special Characters')
print('4. Exit')
characters = ''
while True:
    option = int(input('Please select your option:'))
    if (option==1):
        characters+=string.ascii_letters
    elif (option==2):
        characters+=string.digits
    elif(option==3):
        characters+=string.punctuation
    elif(option==4):
        break
    else:
        print('Please enter valid option')

for passwords in range(amount_of_passwords):
    create_password(length_of_password)


