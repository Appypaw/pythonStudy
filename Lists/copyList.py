thislist = ["aaa", "bbb", "ccc"]
mylist = thislist.copy()
print(mylist)
#['aaa', 'bbb', 'ccc']
#copy() 메소드 써서 하면 됨.

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#['apple', 'banana', 'cherry']
#아님 list()메소드를 써도 된다.