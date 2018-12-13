
class employees:
    def register(self,firstname,lastname,username,password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        f=open("employees.txt",'a')
        try:
            f.write("{} {} {} {}\n".format(self.firstname,self.lastname,self.username,self.password))
        except Exception as e:
            print("Error registering you\n")
            return 0
        else:
            print("Registration succefull\n")
            return 1
        finally:
            f.close()
    def login(self,username,password):
        self.username = username
        self.password = password
        f=open("employees.txt",'r')
        v=f.readlines()
        x=[]
        for i in v:
            f = []
            a, b, c, d = i.split(" ")
            f.append(c)
            f.append(d)
            x.append(f)
        c=[]
        c.append(self.username)
        s=self.password+'\n'
        c.append(s)
        if c in x:
            print("login successful\n")
            return 1
        else:
            print("Wrong username or password\n")
            return 0

a=int(input("Select:-\n1-Register\n2-Login\n"))
if a==1:
    firstname=input("Enter firstname\n")
    lastname=input("Enter lastname\n")
    username=input("Enter username\n")
    b = int(input("Select\n1-Generate password by computer\n2-Type in your self\n"))
    if b == 2:
        password = input("Enter password\n")
    elif b == 1:
        from password import pass_gen
        password = pass_gen(8)
        print("your password is {}".format(password))
    else:
        print("Wrong choice")
        quit()
    employee=employees()
    e = employee.register(firstname,lastname,username,password)
    if e == 1:
        from my_calculator import *
    else:
        quit()
elif a==2:
    username = input("Enter username\n")
    password = input("Enter password\n")
    #credentials=username+' '+password
    employee=employees()
    e=employee.login(username,password)
    if e== 1:
        from my_calculator import *
    else:
        quit()