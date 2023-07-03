x = 1    # int 정수
y = 2.8  # float 실수
z = 1j   # complex 복소수. 공업수학 기억안남.. z=2+3j를 예시로 들었을 때 z는 실수부고 허수부가 3인 복소수임.

print(type(x))
print(type(y))
print(type(z))

'''
<class 'int'>
<class 'float'>
<class 'complex'>
'''

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#정수형에서 실수형으로 변경:
a = float(x)

#실수형이서 정수형으로 변경:
b = int(y)

#정수형에서 복소수형으로 변경
c = complex(x)


print(type(a))
print(type(b))
print(type(c)) 
print(a)
print(b)
print(c)

'''
<class 'float'>
<class 'int'>
<class 'complex'>
1.0
2
(1+0j)
'''