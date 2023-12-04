import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko(0)

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(7)
    joukko.lisaa(4)
    joukko.lisaa(5)
    joukko.poista(4)
    
    

    print(joukko.to_int_list())


if __name__ == "__main__":
    main()
