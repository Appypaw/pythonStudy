thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#['apple', 'banana', 'cherry', 'orange']
#append()메소드를 사용하면 아이템을 추가할 수 있음. append(넣을 아이템)

cats = ["cheese", "moomoo", "yuja"]
animals = ["hippo", "dog", "cactus"]
animals.extend(cats)
print(animals)
#['hippo', 'dog', 'cactus', 'cheese', 'moomoo', 'yuja']
#extend를 사용하면 리스트를 통째로 다른 리스트에 추가할 수 있음. 넣음당할리스트.extend(넣을리스트)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#['apple', 'banana', 'cherry', 'kiwi', 'orange']
#이터러블을 넣을 수 있음. 