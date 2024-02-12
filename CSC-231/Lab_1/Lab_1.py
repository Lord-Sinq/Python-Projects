'''
Lab_1 - Fractions
Name: Sinclair DeYoung
Date: May 23, 2023
Discription: This Takes two fractions and gives the solutions for adding,
subtracting, multiplied, and divide.
'''
def main():
    f1 = Fraction(1,2)
    f2 = Fraction(3,4)
    f3 = f1 + f2
    f4 = f1 - f2
    f5 = f1 * f2
    f6 = f1 / f2
    print(f3)
    print(f4)
    print(f5)
    print(f6)
class Fraction:
    def __init__(self, num=0, den=1):
        g = self.__gcd__(num, den)
        self.__num = num // g
        self.__den = den // g
        if (self.__den < 0):
            self.__num = -self.__num
            self.__den = -self.__den
    def __gcd__(self, num, den):
        while num % den != 0:
            oldnum = num
            oldden = den
            num = oldden
            den = oldnum % oldden
        return den
    def __str__(self):
        return str(self.__num)+'/'+str(self.__den)
    def __add__(self, other):
        newnum = self.__num*other.__den + self.__den * other.__num
        newden = self.__den * other.__den
        return Fraction(newnum , newden)
    def __sub__(self, other):
        newnum = self.__num * other.__den - self.__den * other.__num
        newden = self.__den * other.__den
        return Fraction(newnum , newden )
    def __mul__(self, other):
        return Fraction(self.__num * other.__num, self.__den * other.__den)
    def __truediv__(self, other):
        return Fraction(self.__num * other.__den,self.__den * other.__num)
if __name__=="__main__":
    main()
