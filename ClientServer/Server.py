__author__ = 'AlejandroFrech'
import socket
import time
from FileManager import FileManager
from User import User
import requests


class Server:
    fm = FileManager()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 2222

    server_socket.bind((host, port))
    server_socket.listen(1)

    print('Awaiting connection...')
    client_socket, addr = server_socket.accept()

    print('Connection established...')
    current_time = time.ctime(time.time())
    msg = '[{}] You are connected to the server!'.format(current_time)
    client_socket.send(msg.encode('utf-8'))

    while True:
        client_data = client_socket.recv(1024)
        d = client_data.decode('utf-8')
        tokens = d.split("\n")
        if len(tokens) == 2:
            if tokens[1] == 'ShowUser':
                enc = fm.search(tokens[0])
                client_socket.send(enc.encode('utf-8'))
                continue
            if tokens[1] == 'DeleteUser':
                users = fm.getUsers()
                usersList = users.split("\n")
                for u in usersList:
                    if tokens[0] in u:
                        print(u)
                        usersList.remove(u)
                fm.reWriteFile()
                for u in usersList:
                    print(u)
                    fm.writeUser(u)
                enc = "YES"
                client_socket.send(enc.encode('utf-8'))
                continue
        if len(tokens) == 3:
            if tokens[1] == 'SendEamil':
                user = fm.search(tokens[0])
                userinfo = user.split(",")
                print(len(userinfo))
                if len(userinfo) != 6:
                    enc = "NOT"
                    client_socket.send(enc.encode('utf-8'))
                else:
                    me = "ClientServe@info.com"
                    you = tokens[2]
                    key = 'key-8tw489mxfegaqewx93in2xo449q5p3l0'
                    sandbox = 'app5dcaf6d377cc4ddcb696b827eabcb975.mailgun.org'
                    recipient = you
                    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
                    request = requests.post(request_url, auth=('api', key), data={
                        'from': me,
                        'to': you,
                        'subject': 'Contact Information',
                        'html': """\
                    <html>
                      <head></head>
                      <body>
                        <p>---------------ContactInfo-----------<br></p>
                        <p> Username :""" + userinfo[0] + """
                        <p> Name :""" + userinfo[1] + """</p>
                        <p>Email :""" + userinfo[2] + """</p>
                        <p>Identity Card :""" + userinfo[3] + """</p>
                        <p>Birth Date : """ + userinfo[4] + """</p>
                        <h2>Profile picture</h2>
                        <img src=""" + userinfo[5] + """ style="width:128px;height:128px;">
                      </body>
                     </html>
                    """
                    })
                    print('Status: {0}'.format(request.status_code))
                    print('Body:   {0}'.format(request.text))
                    if request.status_code == 200:
                        enc = "YES"
                    else:
                        enc = "NO"
                    client_socket.send(enc.encode('utf-8'))
                continue
        if client_data:
            fm.createFile()
            user = client_data.decode('utf-8')
            userinfo = user.split(",")
            usr = User(userinfo[0],userinfo[1],userinfo[2],userinfo[3],userinfo[4],userinfo[5])
            if usr.VerifyUser():
                enc = "YES"
                fm.writeUser(client_data.decode('utf-8'))
                print('[CLIENT] {}'.format(client_data.decode('utf-8')))
            else:
                enc = "NO"
            client_socket.send(enc.encode('utf-8'))
            continue
        print('Closing connection with the client...')
        client_socket.close()
