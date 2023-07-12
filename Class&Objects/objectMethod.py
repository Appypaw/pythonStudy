class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("안녕하세요. 제 이름은 " + self.name + "입니다. 또한 제 나이는 " + self.age + "살 입니다.")

me = Person("준재준", "26")
Person.introduce(me)
#안녕하세요. 제 이름은준재준입니다. 또한 제 나이는 26살 입니다.

me.age = 30
#나이를 30으로 변경
del me.age
#나이를 삭제. 객체 프로퍼티
del me
#me를 삭제. 객체 자체를 지워버림.