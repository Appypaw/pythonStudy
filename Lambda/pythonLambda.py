#람다란 자그마한 익명 함수를 말함.
#람다 함수는 어떠한 수의 인자수도 받을 수 있지만 오직 하나의 표현식만 내놓을 수 있음.

#기본 구조
#람다 인자 : 표현식

x = lambda a : a + 10
print(x(20))
#30

x = lambda a, b : a*b
print(x(5,7))
#35

x = lambda c, d, e : c*d-e
print(x(10,2,5))
#15

#그래서 람다식을 왜 쓰나요??
#람다식의 진가는 다른 함수 내부의 익명 함수로 쓸 때 보임.

def sample(n):
    return lambda a : a*n   #모르는 숫자를 곱해주며 하나의 인자값만을 받는 함수를 다음과 같이 정의해보자.

doubler = sample(2)

print(doubler(11)) 
#22