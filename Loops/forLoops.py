#for 루프는 시퀀스 형태의 데이터를 순회하면서 각 요소에 대해 반복접으로 작업을 수행하는데 사용함.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
"""
apple
banana
cherry
"""

for i in range(1, 5):
    print(i)
"""
1
2
3
4
"""
# 숫자 범위 순회하며 작업 수행하기
# i는 for문 내부에서 선언한 변수고 range(1, 5)는 1부터 4까지의 숫자 범위를 의미함.
# for문의 실행 흐름에서 각 반복마다 숫자가 하나씩 꺼내져서 i가 하나씩 할당됨. 첫번째 루프에서는 1, 두번째 루프에선 2, 세번째 루프에선 3,, 이런식.

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
#문자열같은 경우 그 문자열에 있는 문자 하나하나 반복함.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
"""
apple
banana
"""
#break를 사용하면 루프문을 깨고 나올 수 있음. 근데 break하기 전에 print(x)가 먼저 작동하므로 banana는 포함임. banana가 나오면!! 멈추는거임.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#apple
#이건 print(x)하기 전에 이미 banana가 나오면 멈춘다고 나와있으므로 banana는 미포함임.

for x in range(6):
  print(x)
"""
0
1
2
3
4
5
"""
#range()함수는 0부터 시작해서 1(기본값)씩 올린 뒤 특정 숫자에서 멈춤.

for x in range(2, 6):
  print(x)
"""
2
3
4
5
"""
#6는 미포함임.

for x in range(2, 30, 3):
  print(x)
"""
2
5
8
11
14
17
20
23
26
29
"""
#range(시작숫자, 끝날숫자, 점점 올라갈 숫자 단위) 3씩 올라감.

for x in range(6):
  print(x)
else:
  print("루프 끝") 
"""
0
1
2
3
4
5
루프 끝
"""
#else:를 사용하면 반복이 끝날 경우 무엇을 실행할 지 지정해줄 수 있음.

adj = ["맛있는", "알찬", "큰"]
fruits = ["사과", "배", "고양이"]
for a in adj:
  for b in fruits:
    print(a, b)
"""
맛있는 사과
맛있는 배
맛있는 고양이
알찬 사과
알찬 배
알찬 고양이
큰 사과
큰 배
큰 고양이
"""
#다중  for문 사용 가능.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 
"""
apple
banana
cherry
"""
#리스트의 인덱스 번호만큼 반복하는 반복문.

