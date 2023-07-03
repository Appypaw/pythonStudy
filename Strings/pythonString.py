print("Hello")
print('Hello') # 둘 다 똑같음. "문자열" = '문자열'

'''
Hello
Hello
'''

a = "Hello" #문자열을 변수에 할당하기
print(a) 

'''
Hello
'''

a = """안녕하세요,
반갑습니다,
사실 안반갑습니다
파이썬은 자바보다 쉽습니다.""" #여러 줄의 문자열을 ''' 또는 """으로 지정할 수 있음
print(a) 

"""
안녕하세요,
반갑습니다,
사실 안반갑습니다
파이썬은 자바보다 쉽습니다.
"""


#Python에서 문자열은 배열로 취급됨.
a = "Hello, World!"
print(a[1]) #배열에서 'H' 다음의 'e'를 출력함. 배열은 0부터 시작!
"""
e
"""

#문자열 반복
for x in "banana":
  print(x)

"""
b
a
n
a
n
a
"""

#문자열 길이
a = "Hello, World!"
print(len(a)) #len은 length로 길이를 반환하는 함수?? 함수 맞나?
"""
13
"""

#문자열 확인
txt = "Python은 쉬워요!!"
print("Python" in txt)
"""
True
"""

txt = "Python은 재밌어요!"
if "재밌" in txt:
  print("네, Python은 재밌어요..")
"""
네, Python은 재밌어요..
"""