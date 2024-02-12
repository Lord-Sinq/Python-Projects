'''
Lab_2 - Fractions / Percentage
Name: Sinclair DeYoung
Date: May 24, 2023
Discription: This Takes two fractions and gives the solutions for adding,
subtracting, multiplied, and divide : During Lab_2 i will be adding solutions
to <, >, <=, >=, ==, and !=
'''
def main():
    # lab_1
    '''
    holds all the values and arguments for the class below
    :return: then returns there answers
    '''
    f1 = Fraction(1,2)
    f2 = Fraction(3,4)
    print('Start of +,-,*,/. Section:')
    print("Adding Returns: " , f1 + f2)
    print('Subtracting Returns:', f1 - f2)
    print('Muiltiple Returns:', f1 * f2)
    print('Dividing Returns:', f1 / f2)
    # lab_2
    print('Start of the <,>,<=,>=,==,!=. Section:')
    print(f1, ' == ',f2, 'is', f1 == f2)
    print(f1, ' != ', f2, 'is', f1 != f2)
    print(f1, ' <= ', f2, 'is', f1 <= f2)
    print(f1, ' >= ', f2, 'is', f1 >= f2)
    print(f1, ' < ', f2, 'is', f1 < f2)
    print(f1, ' > ', f2, 'is', f1 > f2)

class Fraction:
    """
    lab_1
    takes in the numerator and denominator values used to
    evaluate fractions in python
    """
    def __init__(self, num=0, den=1):
        """
        Initializes a Fraction object with the given numerator and denominator.
        """
        g = self.__gcd__(num, den)
        self.__num = num // g
        self.__den = den // g
        if self.__den < 0:
            self.__num = -self.__num
            self.__den = -self.__den
    def __gcd__(self, num, den):
        """
        Computes the greatest common divisor of the numerator and denominator.
        """
        while num % den != 0:
            oldnum = num
            oldden = den
            num = oldden
            den = oldnum % oldden
        return den
    def get_num(self):
        """
        Returns the numerator of the fraction.
        """
        return self.__num
    def get_den(self):
        """
        Returns the denominator of the fraction.
        """
        return self.__den
    def set_num(self, num):
        """
        Sets the numerator of the fraction.
        """
        self.__num = num
    def set_den(self, den):
        """
        Sets the denominator of the fraction.
        """
        self.__den = den
    def getID(self):
        return self.__ID
    def getName(self):
        return self.__name
        # setters
    def setID(self, ID):
        self.__ID = ID
    def setName(self, name):
        self.__name = name
# used for checking certain arguments (+,-,*,/) and also sets the string
    def __str__(self):
        return str(self.__num)+'/'+str(self.__den)
    def __add__(self, other):
        newnum = self.__num*other.__den + self.__den * other.__num
        newden = self.__den * other.__den
        return self.__class__(newnum , newden)
    def __sub__(self, other):
        newnum = self.__num * other.__den - self.__den * other.__num
        newden = self.__den * other.__den
        return self.__class__(newnum , newden )
    def __mul__(self, other):
        return self.__class__(self.__num * other.__num, self.__den * other.__den)
    def __truediv__(self, other):
        return self.__class__(self.__num * other.__den,self.__den * other.__num)
# this is the start of lab_2
# checks each percentage and fraction for (<,>,<=,>=,==,!=)
    def __cmp__(self, other):
        a = self.__num * other.__den
        b = other.__den * self.__num
        if (a > b):
            return 1
        elif (a < b):
            return -1
        else:
            return 0
# the (<,>,<=,>=,==,!=)
    def __lt__(self, other):
        return self.__cmp__(other) < 0
    def __le__(self, other):
        return self.__cmp__(other) <= 0
    def __gt__(self, other):
        return self.__cmp__(other) > 0
    def __ge__(self, other):
        return self.__cmp__(other) >= 0
    def __eq__(self, other):
        return self.__cmp__(other) == 0
    def __ne__(self, other):
        return self.__cmp__(other) != 0
# call the main function
if __name__=="__main__":
    main()
