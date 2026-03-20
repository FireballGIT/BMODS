# area.py
pi = 3.14

class CalcuFunction:
    @staticmethod
    def circleArea(radius):
        r2 = radius ** 2
        return pi * r2

    @staticmethod
    def rectangularPrismArea(h, w, l):
        return l * w * h
