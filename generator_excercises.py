#Generator Excercises
import math
#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.

def primes_gen():
    n = 2
    while True:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                break
        else:
            yield n
        n += 1
        
        

gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')
# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------
print()
#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.

def unique_letters(word):
    n = 0
    cleaned_word = ""
    for letter in word:
        if letter in word and letter not in cleaned_word:
            cleaned_word += letter
    while n < len(cleaned_word):
        yield cleaned_word[n]
        n += 1

for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o