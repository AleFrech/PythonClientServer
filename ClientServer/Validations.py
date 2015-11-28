__author__ = 'AlejandroFrech'
import re
from FileManager import FileManager


class Validations:
    def VerifyEmail(self, string):
        fm = FileManager()
        match = re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', string)
        if match and fm.isUnique(string):
            return 1
        else:
            return -1

    def VerifyCedula(self, string):
        match = re.match(r'\d{4}-\d{4}-\d{5}', string)
        fm = FileManager()
        if match and  fm.isUnique(string):
            return 1
        else:
            return -1

    def VerifyDate(self, string):
        match = re.match(r'\d{2}-\d{2}-\d{4}', string)
        if match :
            return 1
        else:
            return -1
    def VerifyUser(self,string):
        fm = FileManager()
        if  fm.isUnique(string):
            return 1
        else:
            return -1