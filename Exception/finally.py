try:
  print(x)
except:
  print("무언가 잘못됐습니다.")
finally:
  print("'try except'가 끝났습니다.") 
"""
무언가 잘못됐습니다.
'try except'가 끝났습니다.
"""
#finally블록은 만약 try block에서 에러가 나든 안나든 상관없이 출력함.

