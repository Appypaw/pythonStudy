tuple1 = (1, 2, 3, 4, 5)

"""
투플은 여러개의 아이템을 하나의 변수에 넣는거임. 투플은 순서가 정해져있고 못바꿈.
"""

print(tuple1)
#(1, 2, 3, 4, 5)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#3

thistuple = ("apple",)
print(type(thistuple))
#<class 'tuple'>
#투플 안에 아이템을 하나만 넣고싶다면 무조건 뒤에 , 붙여줘야함. 그래야지만 투플로 인정해줌.

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#('abc', 34, True, 40, 'male')
#투플은 다른 형태의 아이템들 섞어넣어도 괜찮음.

atuple = tuple(("apple", "banana", "cherry")) 
print(atuple)
#이렇게도 투플을 만들 수 있음.