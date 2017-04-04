"""

    Problem 49 Prime Permutations
    
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three 
    terms are prime, and, (ii) each of the 4-digit numbers are 
    permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit 
    increasing sequence.

    What 12-digit number do you form by concatenating the three terms 
    in this sequence?

"""

import time
start_timer = time.time()

max_num = 9999
answer = ""

while not bool(answer):
    i = 0
    while True:
        i += 1
        i2 = i * 2
        med_num = max_num - i
        min_num = max_num - i2
        if min_num > 1000:
            max_digits = sorted(str(max_num))
            med_digits = sorted(str(med_num))
            min_digits = sorted(str(min_num))
            if max_digits == med_digits == min_digits:
                nums = [max_num, med_num, min_num]
                for n in nums:
                    half = n / 2
                    not_prime = 0
                    for j in xrange(2, half + 1):
                        if n % j == 0:
                            not_prime += 1
                            break
                    else:
                        continue
                    if not_prime > 0:
                        break
                else:
                    answer += str(min_num) + str(med_num) + str(max_num)
        else:
            break
    max_num -= 2

stop_timer = time.time() - start_timer
print "Answer: " + answer
print "Seconds: " + str(stop_timer)












