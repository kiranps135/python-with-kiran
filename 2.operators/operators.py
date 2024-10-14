"""
what is operators
"""

"""

Assignment

=

+=, -=, /=, //=, **=, %=

"""

a = 5

print(a)
# a = a + 10

# a += 10

# a -= 3

# a *= 3

# a **= 3

# a %= 3

a //= 3

print(a)


"""

Logical Operators

To check 2 or more conditions

AND

C1  C2  Result

F   F   F

F   T   F

T   F   F

T   T   T

OR

C1  C2  Result

F   F   F

F   T   T

T   F   T

T   T   T

NOT (Reverses the result)

"""

physics = 88

chemistry = 19


# print(physics >= 35 and chemistry >= 35)

# print(physics >= 35 or chemistry >= 35)

# print(not not physics >= 35)

# print(physics >= 35 and not chemistry >= 35)

print(not (not physics >= 35 and not chemistry >= 35))


# https://www.geeksforgeeks.org/precedence-and-associativity-of-operators-in-python/
