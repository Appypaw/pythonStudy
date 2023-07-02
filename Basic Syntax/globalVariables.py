x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#전역변수. 함수 밖에서 설정된 변수는 어디에서도 사용할 수 있음.
#def는 함수를 정의하는 키워드. 

#Python is awesome

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

#Pythin is fantastic

print("Python is " + x) 

#함수 내부에서 x로 지정한 fantastic이 출력됨. = 함수 내부에서만 x = fantastic이고 외부에서는 전역함수인 awesome이 나옴.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

#Python is fantastic
# global 키워드를 함수 내부 블럭에서 사용하면 전역 함수에 덮어씌움.

