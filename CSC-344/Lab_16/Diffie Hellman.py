"""
Name: Sinclair DeYoung
Date: 08-11-2023
Section: CSC-344
"""
import random

def main():
    p = random.randint(100,1000)
    g = random.randint(100,1000)
    a = random.randint(100,1000)
    b = random.randint(100,1000)

    A = (g**a)%p
    B = (g**b)%p
    SA = (B**a)%p
    SB = (A**b)%p

    print(f"values\np: {p}\ng: {g}\nA: {A}\nB: {B}\nSA: {SA}\nSB: {SB}")

if __name__ == "__main__":
    main()