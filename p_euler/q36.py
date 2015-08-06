#!/usr/bin/python
import multiprocessing

# 0.400s execution on macbook pro 2015
# 3.9s exec for 10m
# 45s exec for 100m

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def base2conv(n):
    s = []
    if n == 0:
        # s = "0"
        s.append("0")
    else:
        while n != 0:
            s.append(str(n % 2))
            # s = s + str(n % 2)
            n = n / 2
    return "".join(s)

def dblbasepal(s, n):
    if s == s[::-1] and n == revnum(n) and s == s.lstrip("0"):
        return True
    else:
        return False

def revnum(n):
    reversed = 0
    while n != 0:
        temp = n % 10 # last digit
        n = n / 10
        reversed = (reversed * 10) + temp
    return reversed

def work(bot, top, queue):
    total = 0
    for n in xrange(bot, top+1):
        if n == revnum(n):  # can't be double base palindromic
                            # if base 10 aint palindromic
            bin = base2conv(n)
            if bin == bin.lstrip("0") and bin == bin[::-1]:
                total = total + n
        n = n + 1
    q.put(total)


if __name__ == '__main__':
    n = 0 
    total = 0
    totalnum = 1000000
    split = 10
    range = totalnum / split 

    q = multiprocessing.Queue()
    jobs = []

    for i in xrange(0, split):
        bottom = i*range
        top = (i+1)*range
        p = multiprocessing.Process(target=work, args=(bottom, top, q))
        jobs.append(p)
        p.start()

    for process in jobs:
        process.join()
    while not q.empty():
        total = total + q.get()
    print total

