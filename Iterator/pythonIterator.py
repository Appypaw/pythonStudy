#Iterator와 Iterable

#Iterable 객체 - 반복 가능한 객체 (예 : list, dictionaries, set, str, tuple..)

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
"""
apple
banana
cherry
"""
#하나씩 꺼내서 쓸 수 있음

mystr = "Cardiopulmonary"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
"""
C
a
r
d
i
o
"""
#하나씩 꺼내지는걸 확인할 수 있음