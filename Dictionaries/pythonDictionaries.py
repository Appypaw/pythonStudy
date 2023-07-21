thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#딕셔너리는 키-값으로 데이터를 저장함. K-V
#딕셔너리는 정렬되고 바꿀 수 있으며 복사를 허용하지 않는 컬렉션임.

#해쉬 테이블로 구성되어 있음.


print(thisdict["brand"])
#Ford

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) 
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#복제를 허용하지 않기 때문에 year키에 대한 값은 가장 마지막에 작성된걸 덮어쓰기함.

print(len(thisdict))
#3

#딕셔너리 내부의 얼마나 많은 값이 있는지 len함수로 확인함.

thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 
#딕셔너리는 실수, 불린, 정수, 배열과 같은 여러개의 데이터 타입을 포함할 수 있음.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) 
#<class 'dict'>
#타입은 딕셔너리로 나옴.

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 
#{'name': 'John', 'age': 36, 'country': 'Norway'}
#dict() 생성자를 이용하여 딕셔너리를 생성할 수 있음.

