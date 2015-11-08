#!/usr/bin/python
__author__ = 'Neil Okhandiar'
import math
import itertools
import time
import multiprocessing


def g(x, a, total):
    if x < a:
        return total+1
    else:
        total = g(x-1, a, total) + g(x-a, a, total)
        return total


def f(x, a, memo):
    if x < a:
        return 1
    else:
        if x not in memo:
            memo[x] = f(x-1, a, memo) + f(x-a, a, memo)
        return memo[x]

def F(x):
    a = math.sqrt(x)
    return f(x, a, {})

# x < a  | return 1
# x >= a | return g(x-1) + g(x-a)
# Where is memo?
#  the input is x-1
#   if x-1 completes, then we can add it to the memo
#  and if it is in the memo, we can just return that
#     instead of doing a new calculation
#  same with x-a.

def func(x, a):
    stack = [x]
    memo = {}
    total = 0
    while stack:
        x = stack.pop()
        if x in memo:
            total+= memo[x]
        elif x < a:
            total+=1
        else:
            stack.append(x-a)
            stack.append(x-1)
        memo[x] = total
    return total


# so we just need to check if a prime is divisible by any prior prime
# since a prime is the lowest base number that could possibly act as multiple for any other number
# the SIEVE OF ATKINS is a modern improvement on this, but not implemented here.

# don't need to look at primes over half the current number's value
# because 2 is the lowest possible multiple..

# def primestill(x):
#     primelist = [2]
#     for i in range(3,int(x/2)):
#         isPrime = True
#         for prime in primelist:
#             if not i % prime:
#                 break
#         else:
#             primelist.append(i)
#     return primelist


# PRIME GENERATOR USING SIEVE OF ERATOSTHENES
# ORIGINAL AUTHOR: http://www.macdevcenter.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=2
# THEN MODIFIED BY: http://stackoverflow.com/a/3796442 
# COMMENTED BY ME
def gen_primes():
    compnumlist = {}  # composite number dict .... not primes
    yield 2
    # itertools.count makes an infinite generator
    # islice is just skipping every other number (since all evens are not prime, excluding 2
    # I think the only reasoning over xrange is that it lets
    # us go up infinitely 
    for num in itertools.islice(itertools.count(3), 0, None, 2):
        p = compnumlist.pop(num, None) # get dict[num], if not found, return None.
        if p is None:  # if its not in the dict, its a prime
            compnumlist[num**2] = num  # mark the num^2 as a not-prime
                                       # with its prime root
            yield num
        else:
            # x <- smallest (N*p)+num that wasn't known as composite
            # ie p+num, 2p+num, 3p+num ... Np+num
            # x is a known composite, with p as its first-found prime
            # since p is the first-found prime factor of num
            # so now we can mark it as a composite number

            # and since we're jumping by 2's (beginning at 3) to ignore even nums,
            # we know we're only dealing with odds, both for num and for primes
            # (who must be odd), so we can jump by 2p (2p+num, 4p+num, etc)
            # because odd*odd + odd = even, while even*odd + odd = odd. 
            # (odd*odd) = odd; odd + odd = even
            # (even*odd) = even; even+odd=odd
            x = num + 2*p
            while x in compnumlist:
                x += 2*p
            compnumlist[x] = p

def checkPrime(x, primelist):
    print(len(primelist))
    for i in primelist:
        if not x % i:
            return False, primelist
    else:
        primelist.append(i)
        return True, primelist

def getourprimes():
    primelist = []
    for i in gen_primes():
        if i < 10000000 and i > 10010000:  #10000000<p<10010000
            primelist.append(i)
    return primelist

def startfunc(x):
    a = math.sqrt(x)
    return func(x, a)


def g2(x, a, memo):
    if x < a:
        return 1
    else:
        if x in memo:
            return memo[x]
        else:
            y = g2(x-1, a, memo) + g2(x-a, a, memo)
            memo[x] = y
            return y

def G(x):
    a = math.sqrt(x)
    return g(x, a, 0)

def G2(x):
    a = math.sqrt(x)
    memo = {}
    return g2(x, a, memo)


print("Fully functional, but slow as shit when making the initial list of prime numbers")
print("Since well, its getting the primes of the first 10 million numbers...")
print("also the memoizer doesn't work correctly")
# avg = 0
# for i in range(1000):
#     s = time.time()
#     F(1000)
#     avg += time.time()-s
# print(avg/1000)
#
# avg = 0
# for i in range(1000):
#     s = time.time()
#     G(1000)
#     avg += time.time()-s
# print(avg)

total = 0
if __name__ == "__main__":
    # ourprimes = [90, 99, 100, 30]
    # s = time.time()
    # total = 0
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # def callback(result):
    #     global total
    #     total+= result
    # results = [pool.apply_async(startfunc,
    # for i in ourprimes:
    #     pool.apply_async(startfunc, args=(i,), callback=callback)
    # pool.close()
    # pool.join()
    # print(totalV)

    # print("multiprocess", time.time() - s)
    # s = time.time()
    # ourprimes = getourprimes()  # 10000000<p<10010000 
    # print("prime generation", time.time()-s)
    print startfunc(90)
    # s = time.time()
    # total = 0
    # ourprimes = [90]
    # for i in ourprimes:
    #     total += startfunc(i)
    # print(total)
    # print("single process", time.time() - s)




# print(primestill(100))
# s = time.time()
# print(F(1000))
# #print("Memo hits:", mc)
# print(time.time() - s)
#
# s = time.time()
# print(G2(1000))
# print(time.time() - s)
#
# s = time.time()
# print(G(90))
# print(time.time() - s)



