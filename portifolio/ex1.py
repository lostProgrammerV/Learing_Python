from audioop import add


pwd = str(input("What's the master password ? "))

def view():
        with open('password.txt', 'r') as f:
            for line in r.readlines():
                print(line.rstrip())
def add():
 name = str(input("Account name: "))
 pwd = str(input("Password: "))
 
 with open('passwords.txt', 'a') as f:
    f.write(name + " | " + pwd)

while True:
    mode = str(input("Would you like to add a new password "))
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")





