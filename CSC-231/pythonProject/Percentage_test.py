from Fraction import Fraction

class Percentage(Fraction):
    def __init__(self, num=0, den=100):
        super().__init__(num, den)

    def __str__(self):
        percent = (self._Fraction__num / self._Fraction__den) * 100
        rounded = round(percent,2)
        return f"{rounded}%"

def main():
    Test1 = Percentage(76)
    Test2 = Percentage(83)
    Test3 = Percentage(81)

    Weight1 = Percentage(30)
    Weight2 = Percentage(30)
    Weight3 = Percentage(40)

    FinalGrade = Test1 * Weight1 + Test2 * Weight2 + Test3 * Weight3

    print('Final Grade =', str(FinalGrade))

if __name__ == "__main__":
    main()
