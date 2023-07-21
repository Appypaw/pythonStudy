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

