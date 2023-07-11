x = (1,2,3,4,5)
y = list(x)
y[-1] = 6
x = tuple(y)

print(x)
#(1, 2, 3, 4, 6)
#투플은 한 번 만들면 바꿀 수 없지만 리스트로 변환한 다음 값을 수정하고 다시 투플로 변환할 수 있음.

thistuple = ("a", "b", "c")
a = list(thistuple)
a.append("d")
thistuple = tuple(a)
print(thistuple)
#('a', 'b', 'c', 'd')
#추가는 이렇게