#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    A1 = Base()
    print(A1.id)

    A2 = Base()
    print(A2.id)

    A3 = Base()
    print(A3.id)

    A4 = Base(12)
    print(A4.id)

    A5 = Base()
    print(A5.id)
