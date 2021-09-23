
        

def register():
    db = open("database.txt", "r")
    username = input("Create username: ")
    password1 = input("Create password: ")
    password2 = input("confirm password: ")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    

    if password1 != password2:
        ptit("Passwords don't match!, restart")
        register()
    else:
        if len(password1)<=6:
            print("Password too short, restart")
            register()

        elif username in d:
            print("username exists already")
            register()
        else:
            db = open("database.txt", "a")
            db.write(username+", "+password1+"\n")
            print("success!")

def access():
    db = open("database.txt", "r")
    username = input("Enter username: ")
    password1 = input("Enter password: ")
    
    if not len(username or password1)<1:
        d = []
        f = []
        for i in db:
            a,b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        
        try:
            if data[username]:
                try:
                    if password1 == data[username]:
                        print("Login success")
                        print("Hi,",username)
                        purpose()
                    else:
                        print("Password or Username incorrect")
                except:
                    print("incorrect password of username")
            else:
                print("Username or password doesn't exist")
        except:
            print("Username or password doesn't exist")
    else:
        print("please enter a value")

def home(option=None):
    option = input("Login | Signup: ")
    option = option.lower()
    if option == 'login':
        access()
    elif option == 'signup':
        register()
    else:
        print("Option does not exist!")

home()