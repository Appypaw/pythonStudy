x = 5
y = 9
print(x)
print(y)
# 5
# 9

x = 4  # x는 이제 정수형
y = "Sally" # y는 이제 문자형
print(x)
print(y)
# 4
# Sally

x = str(3) # x는 '3' (문자열)
y = int(3) # y는 3 (정수)
z = float(3) # z는 3.0 (실수)
print(x)
print(y)
print(z)
#3
#3
#3.0

x = 5
y = "John"
print(type(x))  #정수라고 알려줌
print(type(y))  #문자열이라고 알려줌
#<class 'int'>
#<class 'str'>

x = "John"
# 위랑 아래랑 같음.
x = 'John'

a = 4
A = "Sally"
#A는 a에 덮어쓰기 하지 않음. 대문자랑 소문자 구분함 