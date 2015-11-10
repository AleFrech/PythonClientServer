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
        if val.VerifyUser(self.Username)==-1:
            print("Username ya existe!!!!!")
            return False
        if val.VerifyEmail(self.Email) == -1:
            print("Email no valido o existente!!!")
            return False
        if val.VerifyCedula(self.Cedula) == -1:
            print("Cedula  no valida o existente!!!")
            return False
        if val.VerifyDate(self.Fecha) == -1:
            print("Fecha no valida!!!")
            return False
        return True

    def toString(self):
        return self.Username+','+self.Name+','+self.Email+','+self.Cedula+','+self.Fecha+','+self.Img