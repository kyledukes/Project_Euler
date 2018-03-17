"""

    Problem 41 Pandigital Prime
    
    We shall say that an n-digit number is pandigital if it makes use of
    all the digits 1 to n exactly once. For example, 2143 is a 4-digit
    pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?

"""
import math
import time
start_timer = time.time()

def isPrime(num):
    for n in xrange(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    else:
        return True
        
def permutations(s):
    if len(s) <= 1: 
        yield s
    else:
        for i in range(len(s)):
            for p in permutations(s[:i] + s[i+1:]):
                yield s[i] + p
                
def printPrimePermutation(num_str):          
    for i in permutations(num_str):
        if i[-1] in set(['3', '7', '1']):
            if isPrime(int(i)):
                print(i)
                return True

num_str = '987654321'
for i in range(len(num_str)):  
    if printPrimePermutation(num_str[i:]):
        break
        
stop_timer = time.time() - start_timer
print "Seconds: " + str(stop_timer)







