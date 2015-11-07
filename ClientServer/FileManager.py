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
            file.write('0\n')
            file.close()

    def writeUser(self,User):
        fn = os.path.join(os.path.abspath('Data.txt'))
        file = open(fn, 'r+')
        file.seek(0, 2)
        file.write(User + '\n')
        file.close()

    def isUnique(self,parametro):
        self.createFile()
        fn = os.path.join(os.path.abspath('Data.txt'))
        with open(fn, 'r') as inF:
            for line in inF:
                if parametro in line:
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
        fn = os.path.join(os.path.abspath('Data.txt'))
        with open(fn, 'r') as inF:
            for line in inF:
                if username in line:
                    return line
        return ' '