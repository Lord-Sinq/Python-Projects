class Fraction:
    def __init__(self, num=0, den=1):
        g = self.__gcd__(num, den)
        self.__num = num // g
        self.__den = den // g
        if self.__den < 0:
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
        return str(self.__num) + '/' + str(self.__den)

    def __add__(self, other):
        newnum = self.__num * other.__den + self.__den * other.__num
        newden = self.__den * other.__den
        return self.__class__(newnum, newden)

    def __sub__(self, other):
        newnum = self.__num * other.__den - self.__den * other.__num
        newden = self.__den * other.__den
        return self.__class__(newnum, newden)

    def __mul__(self, other):
        return self.__class__(self.__num * other.__num, self.__den * other.__den)

    def __truediv__(self, other):
        return self.__class__(self.__num * other.__den, self.__den * other.__num)

    def __cmp__(self, other):
        a = self.__num * other.__den
        b = other.__den * self.__num
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    def __lt__(self, other):
        return (self.__num, self.__den) < (other.__num, other.__den)

    def __le__(self, other):
        return (self.__num, self.__den) <= (other.__num, other.__den)

    def __gt__(self, other):
        return (self.__num, self.__den) > (other.__num, other.__den)

    def __ge__(self, other):
        return (self.__num, self.__den) >= (other.__num, other.__den)

    def __eq__(self, other):
        return (self.__num, self.__den) == (other.__num, other.__den)

    def __ne__(self, other):
        return not (self == other)

def main():
    # Test the Fraction class
    frac1 = Fraction(1, 2)
    frac2 = Fraction(3, 4)

    print(f"frac1: {frac1}")
    print(f"frac2: {frac2}")

    frac3 = frac1 + frac2
    print(f"frac1 + frac2 = {frac3}")

    frac4 = frac1 - frac2
    print(f"frac1 - frac2 = {frac4}")

    frac5 = frac1 * frac2
    print(f"frac1 * frac2 = {frac5}")

    frac6 = frac1 / frac2
    print(f"frac1 / frac2 = {frac6}")


if __name__ == "__main__":
    main()

