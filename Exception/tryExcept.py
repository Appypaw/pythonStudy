try:                                #여기서 아래 있는 코드를 일단 실행해봄
    print(x)
except:                             #문제가 생기면 이걸 실행함
    print("에러가 발생했다!")

#에러가 발생했다!
#자바에서 자주보던 예외처리와 방식 똑같음. try ~catch와 비슷??한듯?? 검색해보기.

try:
  print(y)
except NameError:
  print("변수 y가 정의되지 않았습니다.")
except:
  print("그거 말고도 아무튼 문제가 생겼습니다.") 

#변수 y가 정의되지 않았습니다.
#NameError가 생겼을 때 예외처리도 따로 지정해줄 수 있음. 

try:
   print("Hello")
except:
   print("문제가 생겼습니다.")
else:
   print("문제가 없네요.")
#문제가 없네요.