class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

person = Person("준재준", 26)

print(person.name)
print(person.age)
print(person)
"""
준재준
26
준재준(26)
"""

class Study:
    def __init__(self, hour, minute, subject):
        self.hour = hour
        self.minute = minute
        self.subject = subject

    def __str__(self):
        return "{}시간 {}분동안 {}과목을 공부하였습니다.".format(self.hour, self.minute, self.subject)
    
day1 = Study(1, 30, "Python")
print(day1)
#1시간 30분동안 Python과목을 공부하였습니다.

#__str__()은 클래스 자체의 내용을 출력하고 싶을 때(__init__()으로 규정한) 씀.
