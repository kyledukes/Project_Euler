"""

    Problem 41 Pandigital Prime
    
    We shall say that an n-digit number is pandigital if it makes use of
    all the digits 1 to n exactly once. For example, 2143 is a 4-digit
    pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?

"""

import time
start_timer = time.time()

num = 987654321

ground_truth = ['9','8','7','6','5','4','3','2','1']


while True:
    digits_list = list(str(num))
    if '0' in digits_list:
        continue
    ground_truth_digits = ground_truth[-len(digits_list):]
    digits_list.sort()
    digits_list.reverse()
    if digits_list != ground_truth_digits:
        continue
    for n in xrange(2, num/2):
        if num % n == 0:
            break
    else:
        break
    num -= 2
        
stop_timer = time.time() - start_timer
print "Answer: " + str(num)
print "Seconds: " + str(stop_timer)







