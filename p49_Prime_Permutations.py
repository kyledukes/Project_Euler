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

big_num = 9999
answer = ""

while len(answer) == 0:
    i = 0
    while True:
        i += 1
        i2 = i * 2
        mid_num = big_num - i
        min_num = big_num - i2
        nums = [big_num, mid_num, min_num]
        if min_num > 1000:
            big_digits = sorted(str(big_num))
            mid_digits = sorted(str(mid_num))
            min_digits = sorted(str(min_num))
            if big_digits == mid_digits == min_digits:
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
                    answer += str(min_num) + str(mid_num) + str(big_num)
        else:
            break
    big_num -= 2

stop_timer = time.time() - start_timer
print "Answer: " + answer
print "Seconds: " + str(stop_timer)












