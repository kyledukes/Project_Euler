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

# starting from the largest pandigital number
num = 987654323

while True:
    n -= 2
    if '0' in str(num):
        continue
    digits_list = list(str(num))
    digits_set = set(str(num))
    if len(digits_set) != len(digits_list):
        continue
    ground_truth_digits = [str(i) for i in xrange(1, len(digits_list) + 1)]
    digits_list.sort()
    if digits_list != ground_truth_digits:
        continue
    for n in xrange(3, int(math.sqrt(num)) + 1, 2):
        if num % n == 0:
            break
    else:
        break
        
stop_timer = time.time() - start_timer
print "Answer: " + str(num)
print "Seconds: " + str(stop_timer)







