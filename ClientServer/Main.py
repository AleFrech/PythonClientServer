__author__ = 'AlejandroFrech'
from User import User
from Client import Client

s, msg = Client().iniciateClient()

while True:
    print("---------------MENU--------------------")
    print("1) Add User")
    print("2) Show User")
    print("3) Delete User")
    print("4) Send user to Email")
    print("5) Exit...")

    print("")
    p = input("Choose Option :")
    p = int(p)
    if p >= 6:
        break
    if p == 1:
        username = input("Enter Username : ")
        name = input("Enter Name : ")
        email = input("Enter Email : ")
        cedula = input("Enter Identity Card : ")
        fecha = input("Enter Birth Date :")
        imagen = input("Enter Profile pic Url : ")
        usr = User(username, name, email, cedula, fecha, imagen)
        s.send(usr.toString().encode('utf-8'))
        enc = s.recv(1024)
        res = enc.decode('utf-8')
        if res == "YES":
            s.send(usr.toString().encode('utf-8'))
            print("User succsesfully added!!!\n")

        else:
            print("Error!!!!!!!!!")

    elif p == 2:
        username = input("Enter the Username to display : ")
        username += "\n"+"ShowUser"
        s.send(username.encode('utf-8'))
        enc = s.recv(1024)
        res = enc.decode('utf-8')
        if res != " ":
            tokens = res.split(",")
            print("----User Info--------")
            print("Username : "+tokens[0])
            print("Name : "+tokens[1])
            print("Email : "+tokens[2])
            print("Identity Card : "+tokens[3])
            print("Birth Date  : "+tokens[4])
        elif res:
            print('Not such user in our database')
    elif p == 3:
        username = input("Enter Username to delete : ")
        username += "\n"+"DeleteUser"
        s.send(username.encode('utf-8'))
        enc = s.recv(1024)
        res = enc.decode('utf-8')
        if res=="YES":
            print("User succesfully deleted!!!!!!")
        else:
            print("Error!!!!")
    elif p == 4:
        username = input("Enter name of username to send info : ")
        email = input("Enter the email to send contact info : ")
        username += "\n"+"SendEamil"
        username+="\n"+email
        s.send(username.encode('utf-8'))
        enc = s.recv(1024)
        res = enc.decode('utf-8')
        if res == "YES":
            print("Susccesfully sent email!!!!!!")
        elif res == "NOT":
            print('Error Contact not Found!!!!')
