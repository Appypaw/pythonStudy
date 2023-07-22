thisdict = {
    "brand": "Hyundai",
    "model": "Sonata",
    "year" : 2000
}

x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
#Sonata
#Sonata

#thisdict["키"]를 통해 접근 가능. .get("키")를 통해서도 가능.

y = thisdict.keys()
print(y)
#dict_keys(['brand', 'model', 'year'])
#키들만 가져올 수 있음.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) 

car["color"] = "red"

print(x) 
#dict_values(['Ford', 'Mustang', 1964, 'red'])

#color키에 대한 red밸류가 추가된것을 확인할 수 있음.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("네, 'model' 키는 딕셔너리 안에 존재합니다. ") 
  #네, 'model' 키는 딕셔너리 안에 존재합니다.

  