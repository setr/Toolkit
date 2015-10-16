__author__ = 'Neil Okhandiar'
import math
import time


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

# def g(x, a, total):
#     if x < a:
#         return total+1
#     else:
#         total = g(x-1, a, total) + g(x-a, a, total)
#         return total
#         # return g(x-1, a) + g(x-a, a)

# x < a  | return 1
# x >= a | return g(x-1) + g(x-a)
# Where is memo?
#  the input is x-1
#   if x-1 completes, then we can add it to the memo
#  and if it is in the memo, we can just return that
#     instead of doing a new calculation
#  same with x-a.

def func(x, a):
    stack = []
    stack.append(x)
    memo = {}
    total = 0
    memocount = 0
    while stack:
        x = stack.pop(0)
        if x < a:
            total+=1
            memo[x+1] = total
            memo[x+a] = total
        else:
            if x in memo:
                memocount += 1
                total+= memo[x]
            else:
                stack.append(x-1)
                stack.append(x-a)
    return total


# every prime is indivisible
# so we just need to check if a prime is divisible by any prior prime
# since a prime is the lowest base number that could possibly act as multiple for any other number
# Apparently known as the SIEVE OF ERASTOSTHENES
# the SIEVE OF ATKINS is a modern improvement on this, but not implemented here.
def primestill(x):
    primelist = [2]
    for i in range(3,int(x/2)):
        isPrime = True
        for prime in primelist:
            if not i % prime:
                break
        else:
            primelist.append(i)
    return primelist

def checkPrime(x, primelist):
    print(len(primelist))
    for i in primelist:
        if not x % i:
            return False, primelist
    else:
        primelist.append(i)
        return True, primelist

def getourprimes():
    nums = list(range(10000000+1, 10010000-1)) #10000000<p<10010000
    print("getting main list")
    s= time.time()
    primelist = primestill(10000000+1)
    print("time:", time.time() - s)
    print("done")
    ourPrimes = []
    # if the number is not divisible by any prime number before it (who are each indivisible), then
    # this number must be prime.
    for i in nums:
        isPrime, primelist = checkPrime(i, primelist)
        if isPrime:
            ourPrimes.append(i)
    return ourPrimes



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

s = time.time()
ourprimes = getourprimes()
total = 0
for i in ourprimes:
    total += F(i)
print(total)
print(time.time() - s)

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



