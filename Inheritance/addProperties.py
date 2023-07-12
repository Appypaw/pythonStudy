class Person:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def query(self):
        print("이름 : " + self.name)
        print("점수 : " + self.grade)

kim = Person("김민수", "A")
kim.query()

"""
이름 : 김민수
점수 : A
"""

class detail(Person):
    def __init__(self, name, grade, score):
        super().__init__(name, grade)
        self.score = score

    def query(self):
        super().query
        print("점수 :", self.score)

kim = detail("김민수", "B", 85)

kim.query()

"""
이름 : 김민수
점수 : A
점수 : 85
"""