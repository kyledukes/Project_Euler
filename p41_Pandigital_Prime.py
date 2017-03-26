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
    num_str == str(num)
    if '0' in num_str or \
            '1' not in num_str or \
            '2' not in num_str or \
            '3' not in num_str or \
            '4' not in num_str or \
            '5' not in num_str or \
            '6' not in num_str or \
            '7' not in num_str:
        continue
    digits_list = list(num_str)
    digits_set = set(num_str)
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







