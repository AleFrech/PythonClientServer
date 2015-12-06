__author__ = 'AlejandroFrech'
from Validations import Validations


class User:
    def __init__(self, username, name, email, cedula, fecha, img):
        self.Username = username
        self.Name = name
        self.Email = email
        self.Cedula = cedula
        self.Fecha = fecha
        self.Img = img

    def VerifyUser(self):
        val = Validations()
        if not (val.VerifyUser(self.Username)):
            return False
        if not (val.VerifyEmail(self.Email)):
            return False
        if not (val.VerifyCedula(self.Cedula)):
            return False
        if not (val.VerifyDate(self.Fecha)) :
            return False
        return True

    def toString(self):
        return self.Username + ',' + self.Name + ',' + self.Email + ',' + self.Cedula + ',' + self.Fecha + ',' + self.Img
