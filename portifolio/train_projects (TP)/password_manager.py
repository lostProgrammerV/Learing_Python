#Install: pip install cryptography, ahead test
from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = str(input("What's the master password ? "))
key = load_key() + master_pwd.encode()
fer = Fernet(key)

#That part of the code stay in comment form bcs, load_key make some and better.
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def view():
        with open('password.txt', 'r') as f:
            for line in r.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:",user,"| Password:",
                fer.decrypt(passw.encode()).decode())

def add():
 name = str(input("Account name: "))
 pwd = str(input("Password: "))
 
 with open('passwords.txt', 'a') as f:
    f.write(name + " | " + fer.encrypt(pwd.encode()) + "\n")

while True:
    mode = str(input("""Would you like to add a new password 
    v(to view), a(to add) and q(to quit)"""))
    if mode == "q":
        break
    
    if mode == "view" or "v":
        view()
    elif mode == "add" or "a":
        add()
    else:
        print("invalid mode")