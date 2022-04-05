from audioop import add


pwd = str(input("What's the master password ? "))

class View:
    def view():
        pass

class Add:
    def add():
        name = str(input("Account name: "))

while True:
    mode = str(input("Would youi like to add a new password"))
    if mode == "q":
        break
    
    if mode == "view":
        View
    elif mode == "add":
        Add
    else:
        print("invalid mode")





