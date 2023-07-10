thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry']
#remove 메소드로 삭제 가능. remove(지울거)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#['apple', 'cherry']
#pop 메소드로 삭제 가능. pop은 remove와 다르게 인덱스 번호로 삭제함. 
#딱히 번호 지정 안하고 pop() 해버리면 그냥 맨 마지막 인덱스 삭제함. 

thislist = ["apple", "banana", "cherry"]
thislist.pop(-1)
print(thislist)
#['apple', 'banana'] 
#-1 결과. 마지막 인덱스 삭제함.

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#['banana', 'cherry']
#del도 pop과 마찬가지로 인덱스로 삭제함. 근데 이건 메소드가 아니라 키워드.

thislist = ["apple", "banana", "cherry"]
del thislist 
#리스트 자체를 삭제해버림.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#[]
#이건 리스트는 살려두는데 리스트 내부의 아이템을 다 지워버림.