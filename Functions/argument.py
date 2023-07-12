def func(firstname, secondname):
    print(firstname + " " + secondname)

func("김", "민수")
#이 준재
#2개의 argument(인자)를 기대값으로 하고 받았을 때 정상적으로 작동함.

"""
def wrongFunc(fname, sname):
    print(fname + " " + sname)

func("김")
"""
#이러면 에러가 뜸. 왜냐? 2개의 인자를 기대했는데 하나밖에 나오지 않았으므로

def arbArg(*names):
    print("마지막 인물은 " + names[-1] + " 입니다.")

arbArg("김민수", "김영철", "임재준")
#마지막 인물은 임재준 입니다.
#얼마만큼의 인자를 받을지 모를 경우 Arbitrary Arguments, *args를 통해 다수의 인자를 받을 수 있음.
#이럴 경우에 투플 형식의 인자를 받게됨.

def key(person1, person2, person3):
    print("가장 직위가 높으신 분은 " + person1 + " 입니다.")

key(person1 = "사장님", person2 = "전무님", person3 = "상무님")
#가장 직위가 높으신 분은 사장님 입니다.
#key = value 를 이용해서도 사용할 수 있음.

def kwarg(**people):
    print("그 분의 성씨는 " + people["fname"] + " 이고 이름은 " + people["sname"] + " 입니다.")

kwarg(fname = "lee", sname = "jaejun")
#그 분의 성씨는 lee 이고 이름은 jaejun 입니다.