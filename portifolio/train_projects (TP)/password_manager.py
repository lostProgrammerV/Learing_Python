from audioop import add


master_pwd = str(input("What's the master password ? "))



def view():
        with open('password.txt', 'r') as f:
            for line in r.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:",user,"| Password:",passw)

def add():
 name = str(input("Account name: "))
 pwd = str(input("Password: "))
 
 with open('passwords.txt', 'a') as f:
    f.write(name + " | " + pwd)

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





