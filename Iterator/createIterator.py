class MyNumber():
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""
1
2
3
4
5
"""

class Newone():
    def __iter__(self):
        self.a = 100
        return self
    
    def __next__(self):
        x = self.a
        self.a -= 1
        return x
    
newClass = Newone()
newiter = iter(newClass)

print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))

"""
100
99
98
97
96
95
"""