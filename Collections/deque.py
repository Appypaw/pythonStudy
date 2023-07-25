from collections import deque

#deque(데크? 디큐?)는 double-ended queue의 줄임말로 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료구조를 의미한다.

#list와 비슷해서 list에 쓰이는 메소드들을 많이 쓸 수 있음.

a = ['a', 'b', 'c']
a.append('d')

print(a)
#['a', 'b', 'c', 'd']

deq = deque(['b', 'c', 'd'])
deq.append('e')
print(deq)
#deque(['b', 'c', 'd', 'e'])

deq.appendleft('a')
print(deq)
#deque(['a', 'b', 'c', 'd', 'e'])

a.extend('lnv')

b = ['a', 'b', 'c']
b.append('lnv')

print("a.extend('lnv') >> ", a)
print("b.append('lnv') >> ", b)

#append는 통째로 넣기(예 : [1,2,3]을 넣으면 리스트 끝에 [1,2,3]이라는 리스트를 아예 통쨰로 넣음)
#extend는 각각의 요소로 넣기(예 : lnv를 넣으면 l, n, v 따로 넣음)

