"""

    Problem 37 Truncatable Primes

    The number 3797 has an interesting property. Being prime itself, it is possible 
    to continuously remove digits from left to right, and remain prime at each stage: 
    3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right 
    and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

import math
import time
start_timer = time.time()

def prime(number):
    for n in xrange(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
            break
    else:
        return True
        
# starting from the smallest truncatable prime
num = 23

allowed_first_digits = {2, 3, 5, 7}
allowed_last_digits = {3, 7}

amount_of_trunc_primes = 0
truncatable_primes_sum = 0

while amount_of_trunc_primes < 11:
    num_str = str(num)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    if first_digit in allowed_first_digits and last_digit in allowed_last_digits:
        num_length = len(num_str)
        for i in xrange(num_length - 1):
            truncate_left_to_right = int(num_str[i:num_length])
            if not prime(truncate_left_to_right):
                break
        else:
            for i in xrange(num_length - 1):
                truncate_right_to_left = int(num_str[0:num_length - i])
                if not prime(truncate_right_to_left):
                    break
            else:
                truncatable_primes_sum += num
                amount_of_trunc_primes += 1
    num += 1

stop_timer = time.time() - start_timer
print "Answer: " + str(truncatable_primes_sum)
print "Seconds: " + str(stop_timer)







