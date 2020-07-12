def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


def product(array):
    result = 1
    for item in array:
        result *= item
    return result



"""
Arguments: 
    bitlength - at least the bit length of n.
    n - an integer (optional).  

Returns:
    n (with padding zeros if needed) with only one bit flipped.

This is a cyclic functions, which means that if you run this function multiple time 
you'll eventually get to the original n.
"""
def greyCode(bitLength,n = None):
    n = (1 << bitLength) - 1 if not n else n
    a = [n]
    r = []
    while n != 0:
        i = 0
        for i in range(bitLength):
            k = n ^ (1 << i)
            if k not in a:
                n = k
                a.append(k)
                r.append(i+1)
                break
    return r


"""
Sieve of eratosthenes.
Returns all primes for 2 to n (exclusive).
"""
def sieve(n):
    nums = range(2,n)

    for i in nums:
        if i == 0:
            continue
        for j in range(2*i-2,n-2,i):
            if nums[j] != 0:
                nums[j] = 0

    return [num for num in nums if num]


"""
Miller–Rabin primarity test
"""
import random

def isPrime(n):
    numOfRounds = 40
    if n <= 3:
        return n > 1

    if n % 2 == 0:
        return False

    k = 0
    m = n-1
    while (m % 2 == 0):
        m >>= 1
        k += 1
    
    for i in range(numOfRounds):
        a = random.randrange(2,n-1)
        x = pow(a,m,n)
        if x == 1 or x == n-1:
            continue
        for j in range(k-1):
            x = pow(x,2,n)
            if x == n-1:
                break
        else:
            return False
    return True


"""
Returns the gcd of two numbers. 
This functions handles also 0 for each or both of the arguments
"""
def gcd(a,b):
    return gcd(b,a % b) if a % (b or 1) else (b or a)


"""
Returns the gcd of two or more numbers using a gcd function.
"""
def batchGcd(nums):
    result = nums[0]
    for n in nums:
        result = gcd(result,n)
    return result


"""
Returns the gcd of two or more numbers recursively, without any external function.
"""
def batchGcdR_recursive(nums): 
    m = nums[-1]
    result = [m]+[n % m for n in nums if n % m] if m else nums[:-1]
    return batchGcd(result) if len(result) > 1 else result[0]



"""
Returns all prime factors of n
"""
def factors(n):
    factors = []
    i = 2
    while n > 1:
        while not isPrime(i):
            i += 1
        if (n % i == 0):
            factors.append(i)
            while (n % i == 0):
                n /= i
        i = i+1
    return factors



def Josephus_permutation(n,k):
    array = [i for i in range(n)]
    i = -1
    while len(array) > 1:
        print(array)
        i = (i + k) % len(array)
        del array[i]
        i -= 1
    
    return array[0]




def isRightTruncablePrime(n):
    while isPrime(n):
        n = int(n/10)
    return n == 0


import math
def isLeftTruncablePrime(n):
    while isPrime(n):
        a = 10**int(math.log(n)/math.log(10))
        while n >= a:
            n -= a
    isLeft = n == 0


