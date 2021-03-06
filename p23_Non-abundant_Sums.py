"""

    Problem 23 Non-abundant sums

    A perfect number is a number for which the sum of its proper divisors
    is exactly equal to the number. For example, the sum of the proper
    divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
    is a perfect number.

    A number n is called deficient if the sum of its proper divisors is
    less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
    smallest number that can be written as the sum of two abundant numbers
    is 24. By mathematical analysis, it can be shown that all integers
    greater than 28123 can be written as the sum of two abundant numbers.
    However, this upper limit cannot be reduced any further by analysis
    even though it is known that the greatest number that cannot be
    expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as
    the sum of two abundant numbers.


"""
import time
start_timer = time.time()

num = 12
abundants = set()

while num < 28123:
    half = num / 2
    divisors_sum = 0
    for n in xrange(2, half + 1):
        if num % n == 0:
            divisors_sum += n
    if divisors_sum > num:
        abundants.add(num)
    num += 1

non_abundant_sum = 0
num = 0

while num < 28123:
    num += 1
    for abun in abundants:
        diff = num - abun
        if diff in abundants:
            break
    else:
        non_abundant_sum += num

stop_timer = time.time() - start_timer
print "Answer: " + str(non_abundant_sum)
print "Seconds: " + str(stop_timer)
