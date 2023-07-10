a = 10
b = 5000
if b > a:
  print("b는 a보다 큽니다.")
#b는 a보다 큽니다.

"""
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error 
"""
#이건 안됨. 파이썬은 다른 프로그래밍 언어들과 다르게 중괄호가 아닌 indentation(줄 시작할 때 여백)을 기준으로 스코프를 정의하기 때문에 안됨. print앞에 띄어쓰건 탭을 해야함.

a = 33
b = 33
if b > a:
  print("b는 a보다 큽니다.")
elif a == b:
  print("a와 b는 같습니다.")
#a와 b는 같습니다.
#elif는 else if인듯?? 아무튼 "만약 이전의 조건이 참이 아니라면 이 조건을 시도해본다."의 느낌.

a = 200
b = 33
if b > a:
  print("b는 a보다 큽니다.")
elif a == b:
  print("a와 b는 같습니다.")
else:
  print("a는 b보다 큽니다.")
#a는 b보다 큽니다.
#else는 if랑 elif가 아니면 작동함.

if a > b: print("a는 b보다 큽니다.")
#한줄에 다 쓰고싶으면 이렇게 :를 사용하여 쓸 수 있음.

a = 200
b = 33
c = 500
if a > b and c > a:
  print("두 조건 모두 참입니다.")
#두 조건 모두 참입니다.
#and 연산자 사용할 수 있음. and는 여러 개의 조건 모두 참이여야함.

a = 200
b = 33
c = 500
if a > b or a > c:
  print("적어도 둘 중 하나는 참입니다.")
#적어도 둘 중 하나는 참입니다.
#or는 여러 개의 조건중 하나만 참이여도 됨.

a = 33
b = 200
if not a > b:
  print("a는 b보다 크지 않습니다.")
#a는 b보다 크지 않습니다.
#not은 부정일 경우에 사용할 수 있음.

x = 41

if x > 10:
  print("10보다는 큽니다,")
  if x > 20:
    print("20보다도 큽니다.")
  else:
    print("20보다 크진 않습니다.") 
"""
10보다는 큽니다,
20보다도 큽니다.
"""
#Nested?? 아무튼 중첩 if문도 사용 가능함. 

a = 33
b = 200

if b > a:
  pass
#if문은 비워둘 수 없기 때문에 if 비슷한걸 쓰고싶지만 에러는 피하고 싶으면 pass 쓸 수 있음.

