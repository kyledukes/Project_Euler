"""

    Problem 42  Coded Triangle Numbers

    The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); 
    so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its alphabetical 
    position and adding these values we form a word value. For example, the word value 
    for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we 
    shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
    containing nearly two-thousand common English words, how many are triangle words?

"""

import string
import time
start_timer = time.time()

f = open("p42_words.txt", "r")
words_string = f.read()
f.close()

upper_alphabet = string.uppercase
lower_alphabet = string.lowercase
letter_scores = {}

for upper_letter, lower_letter in zip(upper_alphabet, lower_alphabet):
    letter_scores[upper_letter] = upper_alphabet.index(upper_letter) + 1
    letter_scores[lower_letter] = lower_alphabet.index(lower_letter) + 1

triangle_numbers = set()
num = 0

while len(triangle_numbers) < 18:
    num += 1
    triangle_number = sum(xrange(num + 1))
    triangle_numbers.add(triangle_number)

words_list = words_string.split(",")
triangle_words = []

for w in words_list:
    word = w.strip('"')
    word_score = 0
    for letter in word:
        word_score += letter_scores[letter]
    if word_score in triangle_numbers:
        triangle_words.append(word)

stop_timer = time.time() - start_timer
print "Answer: " + str(len(triangle_words))
print "Seconds: " + str(stop_timer)








