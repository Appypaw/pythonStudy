i = 1           #정수 i = 1 선언
while i < 6:    #6보다 값이 작을때까진
  print(i)      #i를 출력함
  i += 1        #i를 1씩 더함
"""
1
2
3
4
5
"""

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 
"""
1
2
3
"""
# 마지막에 i+=1을 넣지 않으면 2까지만 나옴. 

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
"""
1
2
4
5
6
"""
#continue를 사용하면 현 상태를 잠시 멈추고 다음 과정으로 넘어갈 수 있음.

k = 3
while k < 15:
  print(k)
  k += 1
else:
  print("끝!")
"""
1
2
3
1
2
4
5
6
3
4
5
6
7
8
9
10
11
12
13
14
끝!
"""
#else로 더 이상 참이 아닐 때 결과를 출력할 수 있음.