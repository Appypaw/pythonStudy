tuple = ("a", "b", "c")

(a, b, c) = tuple

print(a)
print(b)
print(c)
"""
a
b
c
"""

alphabets = ("a", "b", "c", "d")

(first, second, third, fourth) = alphabets

print(first)
print(second)
print(third)
print(fourth)
"""
a
b
c
d
"""

apbets = ("a", "b", "c", "d")

(fst, snd, *rest) = apbets
print(fst)
print(snd)
print(rest)
"""
a
b
['c', 'd']
"""