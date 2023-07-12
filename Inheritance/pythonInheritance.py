#부모 클래스는 상속당하는, 베이스 클래스라고도 부름
#자식 클래스는 다른 클래스로부터 상속하는 클래스. 파생된 클래스라고도 부름

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def printname(self):
        print("이름은 " + self.name + "입니다. 제 직무는 " + self.job + "입니다.")

me = Person("준재준", "DevOps")
me.printname()
#이름은 준재준입니다. 제 직무는 DevOps입니다.
#일단 부모 클래스 생성

class Boss(Person):
    pass

you = Boss("재준", "사장")
you.printname()
#이름은 재준입니다. 제 직무는 사장입니다.
#이렇게 하면 Boss 클래스는 Person 클래스를 그대로 가져옴.

class Boss(Person):
    def __init__(self, name, job):
        #프로퍼티 추가함.
        #__init__() 함수를 추가하는 순간 자식 클래스(Boss)는 더 이상 부모 클래스(Person)의 __init__() 함수를 상속하지 않음.
        #자식 클래스의 __init__()은 부모 클래스의 __init__() 상속을 오버라이딩함.
            Person.__init__(self, name, job)
            #이렇게 하면 성공적으로 init 함수를 넣고 부모 클래스의 init 상속을 유지할 수 있음.

class Boss(Person):
     def __init__(self, name, job):
          super().__init__(name, job)
#super()를 사용해서 부모의 모든 요소를 다 상속해서 가져올 수 있음.        

