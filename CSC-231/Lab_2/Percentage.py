'''
Lab_2 - Percentage
Name: Sinclair DeYoung
Date: May 24, 2023
Discription: This takes grades from test and multiple them with their
weights and gives then answer accordingly.
'''
from Fraction import Fraction
class Percentage(Fraction):
    '''
    takes the test grades and sends them through the Fraction.py file to
    __init__ in the Fraction class
    '''
    def __init__(self, num=0, den=100):
        super().__init__(num, den)
    def __str__(self):
        percent = (self.getNum / self.getDen) * 100
        rounded = round(percent,2)
        return f"{rounded}%"

def main():
    '''
    takes test grades and pairs them with the weight of the grade
    :return: the percentage of your final grade.
    '''
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
