__author__ = 'AlejandroFrech'

import os


class FileManager:

    def createFile(self):
        try:
            temp = os.path.join(os.path.abspath('Data.txt'))
            file = open(temp, 'r')
            file.close()
        except:
            temp = os.path.join(os.path.abspath('Data.txt'))
            file = open(temp, 'w')
            file.close()

    def writeUser(self,User):
        fn = os.path.join(os.path.abspath('Data.txt'))
        file = open(fn, 'r+')
        file.seek(0, 2)
        file.write(User + '\n')
        file.close()

    def isUnique(self,parametro,pos):
        self.createFile()
        users=""
        users = self.getUsers();
        userlist = users.split("\n")
        if len(userlist)<=1:
            return True
        for usr in userlist:
            tokens=usr.split(",")
            if len(tokens) <= 1:
                return True
            if tokens[int(pos)] == parametro:
                return False
        return True

    def getUsers(self):
        self.createFile()
        users=""
        fn = os.path.join(os.path.abspath('Data.txt'))
        with open(fn, 'r') as inF:
            for line in inF:
                users+=line
        return users

    def reWriteFile(self):
        fn = os.path.join(os.path.abspath('Data.txt'))
        file = open(fn,'w')
        file.write(" ")
        file.close()

    def search(self,username):
        self.createFile()
        users=""
        users = self.getUsers();
        userlist = users.split("\n")
        for usr in userlist:
            tokens=usr.split(",");
            if tokens[0]==username:
                return usr
        return ' '