# A typical Login Screen by Albert Lehninger
import os
from random import randint

# Encryption / Decryption
def encrypt_decrypt(text, key, choice):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789+-*/!?,._:;@"
    encrypted_data = ""
    for i in text:
        pos = characters.find(i)
        if choice == 'decrypt':
            newpos = (pos + key)%48
        elif choice == 'encrypt':
            newpos = (pos - key)%48
        else:
            print("Invalid Input!")
            return 0
        encrypted_data += characters[newpos]

    return encrypted_data

# Algorithm that formats and afterwards extracts the email or the password
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

# An Algorithm that compares the database(textfile) and the user input
def does_it_exist(email, password, key):
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
            if ((encrypt_decrypt(email,key,"encrypt")) == get_email(line[x])) and ((encrypt_decrypt(password,key,"encrypt")) == get_pw(line[x])):
                message = "logged in"
                count += 1
                break
        x += 1

    if count == 0:
        message = "\nUser not found!"

    return message


# Main
apprunning = True
while apprunning:
    key = 128
    os.system('cls')
    choice = 'n'
    # Menu
    print("To log in please press '1'!")
    print("To register please press '2'!")
    choice = input()

    # log in
    if choice == "1":
        # collects user data
        email = input("E- Mail: ")
        password = input("Password: ")
        # returns the current status 
        with open("data.txt", "r")as f:
            print(does_it_exist(email, password, key))
        # try again ?
        choice = input("back <- y/n : ")
        if choice != 'y' and choice != 'Y':
            apprunning = False

    # register a new user
    elif choice == "2":
        tryagain = True
        double_check = ""

        while tryagain:
            # collects new data
            print("E-Mail: ", end=(""))
            email = input()
            print("password: ", end=(""))
            password1 = input()
            print("confirm password: ", end=(""))
            password2 = input()

            # confirms the password
            if password1 == password2:
                # checks if the user already exists
                with open("data.txt", "r")as f:
                    double_check = does_it_exist(email, password1, key)
                    
                if double_check == "logged in":
                    print("User already exists!")
                    
                    if input("Try again? y/n \n") == "y" or input("Try again?") == "Y":
                        tryagain = True
                    else:
                        tryagain = False
                    
                else:
                    tryagain = False
                    with open("data.txt", "a")as f:
                        f.write("\n" + encrypt_decrypt(email, key,"encrypt") + " " + encrypt_decrypt(password1, key,"encrypt"))
            else:
                print("Passwords don't match!\n")
                if input("Try again?") == "y" or input("Try again?") == "Y":
                    tryagain = True
                else:
                    tryagain = False    

            # run again ?
            choice = input("back <- y/n : ")
            if choice != 'n' or choice != 'N':
                apprunning = False
            else:
                apprunning = True
