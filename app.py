# A typical Login Screen by Albert Lehninger
import os
from random import randint

# Encryption done here: 
def encrypt(text, key): # Takes the Input and a key only the sender and the reciever gets
    characters = "abcdefghijklmnopqrstuvwxyz0123456789+-*/!?,._:;@"
    encrypted_data = ""
    for i in text:
        pos = characters.find(i)
        newpos = (pos + key)%48 # iterates over the characters string for 'key' - many times
        encrypted_data += characters[newpos]

    return encrypted_data

# Decryption
# The same as the encryption but now it iterates backwards 'key' - many times
def decrypt(text, key): 
    characters = "abcdefghijklmnopqrstuvwxyz0123456789+-*/!?,._:;@"
    decrypted_data = ""

    for i in text:
        pos = characters.find(i)
        newpos = (pos - key)%48
        decrypted_data += characters[newpos]

    return decrypted_data

# algorithm that extracts the user Email adress 
def get_email(f_contents):
    password_f = ""
    email_f = ""
    for x in range(0, len(f_contents), 1):
        if f_contents[x] == " ":
            x += 1
            while x != len(f_contents):
                password_f += f_contents[x]
                x += 1
            break
        else:
            email_f += f_contents[x]

    return email_f

# algorithm that extracts the user password
def get_pw(f_contents):
    password_f = ""
    email_f = ""
    for x in range(0, len(f_contents), 1):
        if f_contents[x] == " ":
            x += 1
            while x != len(f_contents):
                password_f += f_contents[x]
                x += 1
            break
        else:
            email_f += f_contents[x]

    return password_f

# An algorithm that iterates over the data-file that contains
# all the saved user data and compares to the input data from the keyboard
def exists(email, password, key):
    eof = True
    x = 0
    count = 0
    line = []
    message = ""
    while eof:
        line.append(f.readline())
        if len(line[x]) == 0:
            eof = False
            break
        else:
            if ((encrypt(email,key)) == get_email(line[x])) and ((encrypt(password,key)) == get_pw(line[x])):
                message = "\nlogged in"
                count += 1
                break
        x += 1

    if count == 0:
        print("User not found!")

    return message

# Main 
apprunning = True
while apprunning:
    key = 128 # This is the encryption/decryption key. This can be any value
    os.system('cls') # Clear prompt for carity
    yes_no = 'n'
    # Menu
    print("\nLog in -> press '1'!")
    print("Don not have an account yet? -> press '2'!")
    choice = input()

    # Log in :
    if choice == "1":
        # Reads data from the user
        email = input("Email: ")
        password = input("Password: ")
        # Lets you know if the account was found
        with open("data.txt", "r")as f:
            print(exists(email, password, key))
        # restart?
        yes_no = input("zurueck zum Startbildschirm j/n : ")
        if yes_no != 'j' and yes_no != 'J':
            apprunning = False

    # Register as a new user
    elif choice == "2":
        tryagain = True

        while tryagain:
            # Reads data from the user
            print("E-Mail: ", end=(""))
            email = input()
            print("password: ", end=(""))
            password1 = input()
            print("confirm password: ", end=(""))
            password2 = input()
            # saves the new data to a text file
            if password1 == password2:
                tryagain = False
                with open("data.txt", "a")as f:
                    f.write("\n" + encrypt(email, key) + " " + encrypt(password1, key))
            else:
                print("Passwords are not equal!\n")
            # restart ?
            yes_no = input("zurueck zum Startbildschirm j/n : ")
            if yes_no != 'n' or yes_no != 'N':
                apprunning = False
            else:
                apprunning = True
