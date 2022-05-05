from datetime import datetime
import random

"""
class Kor:
    def __init__(self, sugar, kozeppont =(0,0)):
        self.kozeppont = kozeppont
        self.sugar = sugar

    def terulet(self):
        return self.sugar * pow(3.14,2)

    def kerulet(self):
        return self.sugar *2*3.14

    def info (self):
        print(f'A(z) {self.sugar} egység sugarú, {self.kozeppont} középpontú kör területe {self.terulet():.2f} egység, kerülete {self.kerulet():.2f} egység')


kor1 = Kor(5, (2,6))
print(kor1)
print(type(kor1))
print(isinstance(kor1, Kor))
print(kor1.info())
print(kor1.terulet())

korok = []

for i in range (5):
    kor = Kor(random.randint(0,10))
    korok.append(kor)

korok[0].info()


class Negyzet:
    def __init__(self, aOldal, bOldal):
        self.aOldal = aOldal
        self.bOldal = bOldal

    def kerulet(self):
        return self.aOldal + self.bOldal

    def teruelt(self):
        return (2*(self.aOldal)) + (2*(self.bOldal))
        

class Taxi:
    ujTaxi = 0
    regiTaxi = 0

    def __init__(self, rendszam, osszKm, kovSzerv, szakaszKm, fogyasztas=6.0, tankL = 35):
        self.rendszam = rendszam
        self.osszKm = osszKm
        self.kovSzerv = kovSzerv
        self.szakaszKm = szakaszKm
        self.fogyasztas = fogyasztas
        self.tankL = tankL

        if osszKm < 100000:
            type(self).ujTaxi +=1
        else:
            type(self).regiTaxi +=1

    
    def visszaKm (self):
        return round(self.tankL / self.fogyasztas * 100 - self.szakaszKm)

    def szerviz (self):
        return self.kovSzerv - datetime.datetime.now().year

    @classmethod
    def flottaDb(cls):
        return cls.ujTaxi + cls.regiTaxi

    @staticmethod
    def flottaSzlogen():
        return "LogiTaxi bárhol, bármikor!"
        """

class Gepjarmu:
    
    def __init__(self, rendszam, osszKm, kovSzerv, szakaszKm):
        self.rendszam = rendszam
        self.osszKm = osszKm
        self.kovSzerv = kovSzerv
        self.szakaszKm = szakaszKm

    def szerviz (self):
        return self.kovSzerv - datetime.datetime.now().year

    def visszaKm(self):
        return 'Benzines vagy elektromos'

    class Taxi(Gepjarmu):
        def __init__(self, rendszam, osszKm, kovSzerv, szakaszKm, fogyasztas=6.0, tankL = 35):
            super().__init__(rendszam, osszKm, kovSzerv, szakaszKm)
            self.fogyasztas = fogyasztas
            self.tankL = tankL

            def visszaKm (self):
                return round(self.tankL / self.fogyasztas * 100 - self.szakaszKm)

    class Etaxi(Gepjarmu):
        def __init__(self, rendszam, osszKm, kovSzerv, szakaszKm, hatotav = 600):
            super().__init__(rendszam, osszKm, kovSzerv, szakaszKm)
            self.hatotav = hatotav

            def visszaKm(self):
                return self.hatotav - self.szakaszKm
                
            
print("szia")

