# A typical Login Screen by Albert Lehninger
import os
from random import randint

# Verschlüsseln
def encrypt(text, key):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789+-*/!?,._:;@"
    encrypted_data = ""
    for i in text:
        pos = characters.find(i)
        newpos = (pos + key)%48
        encrypted_data += characters[newpos]

    return encrypted_data

# Entschlüsseln
def decrypt(text, key):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789+-*/!?,._:;@"
    decrypted_data = ""
    for i in text:
        pos = characters.find(i)
        newpos = (pos - key)%48
        decrypted_data += characters[newpos]

    return decrypted_data

# Algorithmus, der die Email- Adresse und das Passwort erkennt
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

# Algorithmus, der checkt, ob der User bereits vorhanden ist, oder noch nicht
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


apprunning = True

while apprunning:
    key = 128
    os.system('cls')
    ja_nein = 'n'
    # Menu
    print("\nBitte mit Email - Addresse und Passwort einloggen -> '1' druecken !")
    print("Noch kein Account -> '2' druecken")
    choice = input()

    # Mit User einloggen
    if choice == "1":
        # Abfrage der Daten
        email = input("E- Mail: ")
        password = input("Password: ")
        # Gibt aus, ob ein User gefunden wurde
        with open("data.txt", "r")as f:
            print(exists(email, password, key))
        # Erneut starten ?
        ja_nein = input("zurueck zum Startbildschirm j/n : ")
        if ja_nein != 'j' and ja_nein != 'J':
            apprunning = False

    # neuen Benutzer einspeichern
    elif choice == "2":
        tryagain = True

        while tryagain:
            # Abfrage der neuen Daten
            print("E-Mail: ", end=(""))
            email = input()
            print("password: ", end=(""))
            password1 = input()
            print("confirm password: ", end=(""))
            password2 = input()
            # wird am File gespeichert
            if password1 == password2:
                tryagain = False
                with open("data.txt", "a")as f:
                    f.write("\n" + encrypt(email, key) + " " + encrypt(password1, key))
            else:
                print("Passwords are not equal!\n")
            # Erneut starten ?
            ja_nein = input("zurueck zum Startbildschirm j/n : ")
            if ja_nein != 'n' or ja_nein != 'N':
                apprunning = False
            else:
                apprunning = True
