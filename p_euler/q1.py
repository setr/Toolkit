#!/usr/bin/python
import multiprocessing

def try1():
    n = 0
    total = 0
    while n < 1000:
        if not n % 3 or not n % 5:
            total += n
        n = n + 1
    print total

def try2():
    total = 0
    n = 0
    top = 1000
    bot5 = top / 5
    bot3 = top / 3 # because uneven division
    while n <= bot3:
        if n < bot5 and n % 3:
            total += n*5
        total += n*3
        n += 1
    print total

if __name__ == "__main__":
    try2()
