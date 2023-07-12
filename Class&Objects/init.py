class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Lee", "26")

print(p1.name)
print(p1.age)

"""
Lee
26
"""
#모든 클래스들은 __init()__ 이라는 함수고 잔재함. 항상 클래스가 초기화 될 때마다 실행되는 함수임.
