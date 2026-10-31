#   The prime factors of 13195 are 5, 7, 13 and 29.
#
#   What is the largest prime factor of the number 600851475143 ?

import math

def is_prime(number):
    if(number == 1):
        return False
    
    if(number == 2):
        return True
    
    for i in range(2, math.floor(number/2)):
        if(number % i == 0):
            return False
        
    return True


dividend = 600851475143
dividers = []

for i in range(2, math.floor(dividend/2)):
    if(is_prime(i) and dividend % i == 0):
        dividers.append(i)
        dividend = dividend/i
    
    if(dividend == 1):
        break
largest_prime_factor = dividers.pop()

print(largest_prime_factor)    