__author__ = 'AlejandroFrech'
import socket
import time
from FileManager import FileManager
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        tokens = d.split(",")
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
                user= fm.search(tokens[0])
                userinfo = user.split(" ")
                me = "ClientServe@info.com"
                you = tokens[2]
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Contact info"
                msg['From'] = me
                msg['To'] = you
                text = "Hi!\nHere is the Contact information you wanted:\n"
                html = """\
                <html>
                  <head></head>
                  <body>
                    <p>---------------ContactInfo-----------<br></p>
					<p> Username :"""+userinfo[0]+"""
					<p> Name :"""+userinfo[1]+"""</p>
					<p>Email :"""+userinfo[2]+"""</p>
					<p>Identity Card :"""+userinfo[3]+"""</p>
					<p>Birth Date : """+userinfo[4]+"""</p>
					<h2>Profile picture</h2>
					<img src="""+userinfo[5]+""" style="width:128px;height:128px;">
                  </body>
                 </html>
                """
                part1 = MIMEText(text, 'plain')
                part2 = MIMEText(html, 'html')
                msg.attach(part1)
                msg.attach(part2)
                s = smtplib.SMTP('localhost', 8080)
                s.sendmail(me, you, msg.as_string())
                s.quit()
                enc = "YES"
                client_socket.send(enc.encode('utf-8'))
                continue
        if client_data:
            fm.createFile()
            fm.writeUser(client_data.decode('utf-8'))
            print('[CLIENT] {}'.format(client_data.decode('utf-8')))
            continue
        print('Closing connection with the client...')
        client_socket.close()
