import math

"""
Here the main idea is try to reduce the problem dimensionality
so we can iterate over the less degrees of freedom possible.
"""

def is_special_pythagorean(b, c):
    """
    The special pythagorean system tells us:
    a^2 + b^2 = c^2
    a + b + c = 1000

    a,b,c natural numbers

    Given this, we can isolate 'a' term in the first sentence
    and substitute in the second one to obtain the verification we want.
    """
    return math.sqrt(c**2 - b**2) + b + c == 1000

def find_b_c():
    """
    Based on the substitution we did in is_special_pythagorean method,
    we can isolate the 'c' term to iterate over just one dimension 'b'.
    """
    for b in range(1, 1000):
        c = (1000*b - b**2 - 500000)/(b - 1000)
        if int(c) == c:
            if is_special_pythagorean(b, c):
                return [b, int(c)]

[b, c] = find_b_c()
a = 1000 - b - c
print("Special Pythagorean Numbers:\na:", a,"b:", b, "c:", c)
print("Special Pythagorean Numbers Product: ", a*b*c)